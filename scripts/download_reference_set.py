#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1] / "data" / "references"
USER_AGENT = "Mozilla/5.0 (compatible; drawio-diagram-skill/1.0)"

REFERENCE_SET = {
    "openai": [
        ("introducing-agentkit", "https://openai.com/index/introducing-agentkit/"),
        ("introducing-4o-image-generation", "https://openai.com/index/introducing-4o-image-generation/"),
        ("practical-guide-to-building-agents", "https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf"),
    ],
    "anthropic": [
        ("mozilla-firefox-security", "https://www.anthropic.com/news/mozilla-firefox-security"),
        ("building-agents-sdk", "https://claude.com/blog/building-agents-with-the-claude-agent-sdk"),
        ("emotion-concepts-function", "https://www.anthropic.com/research/emotion-concepts-function"),
    ],
    "vercel": [
        ("self-driving-infrastructure", "https://vercel.com/blog/self-driving-infrastructure"),
        ("fluid-compute", "https://vercel.com/blog/fluid-how-we-built-serverless-servers"),
        ("workflow-builder", "https://vercel.com/blog/workflow-builder-build-your-own-workflow-automation-platform"),
        ("ai-gateway", "https://vercel.com/ai-gateway"),
        ("integration-image-guidelines", "https://vercel.com/docs/integrations/create-integration/integration-image-guidelines"),
    ],
}


class ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[str] = []
        self.meta_images: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "img":
            src = attrs_dict.get("src")
            if src:
                self.images.append(src)
        if tag == "meta":
            prop = attrs_dict.get("property") or attrs_dict.get("name")
            if prop in {"og:image", "twitter:image"}:
                content = attrs_dict.get("content")
                if content:
                    self.meta_images.append(content)


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def sanitize_filename(url: str) -> str:
    parsed = urlparse(url)
    name = Path(parsed.path).name or "index"
    if "." not in name:
        name += ".html"
    return re.sub(r"[^A-Za-z0-9._-]", "-", name)


def is_likely_image(url: str) -> bool:
    path = urlparse(url).path.lower()
    return any(path.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"])


def collect_images(base_url: str, html_text: str) -> list[str]:
    parser = ImageParser()
    parser.feed(html_text)
    ordered: list[str] = []
    for raw in parser.meta_images + parser.images:
        full = urljoin(base_url, raw)
        if full not in ordered and is_likely_image(full):
            ordered.append(full)
    return ordered[:6]


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def main() -> int:
    manifest: dict[str, list[dict[str, object]]] = {}

    for vendor, entries in REFERENCE_SET.items():
        manifest[vendor] = []
        vendor_root = ROOT / vendor
        vendor_root.mkdir(parents=True, exist_ok=True)

        for slug, url in entries:
            item_root = vendor_root / slug
            item_root.mkdir(parents=True, exist_ok=True)
            record: dict[str, object] = {"slug": slug, "url": url, "files": []}

            try:
                raw = fetch(url)
                suffix = ".pdf" if url.lower().endswith(".pdf") else ".html"
                main_path = item_root / f"source{suffix}"
                write_bytes(main_path, raw)
                record["files"].append(str(main_path))

                if suffix == ".html":
                    html_text = raw.decode("utf-8", errors="ignore")
                    image_urls = collect_images(url, html_text)
                    downloaded_images: list[str] = []
                    for i, image_url in enumerate(image_urls, start=1):
                        try:
                            image_raw = fetch(image_url)
                            ext = Path(urlparse(image_url).path).suffix or ".img"
                            image_path = item_root / f"image-{i}{ext}"
                            write_bytes(image_path, image_raw)
                            downloaded_images.append(str(image_path))
                        except Exception as image_exc:  # noqa: BLE001
                            downloaded_images.append(f"ERROR:{image_url}:{image_exc}")
                    record["files"].extend(downloaded_images)
            except Exception as exc:  # noqa: BLE001
                record["error"] = str(exc)

            manifest[vendor].append(record)

    manifest_path = ROOT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
