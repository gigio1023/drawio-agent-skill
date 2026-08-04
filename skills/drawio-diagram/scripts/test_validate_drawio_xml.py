from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = Path(__file__).with_name("validate_drawio_xml.py")
VALID_XML = """\
<mxfile>
  <diagram name="Page-1">
    <mxGraphModel adaptiveColors="auto">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="box" value="Box" style="rounded=1;html=1;" vertex="1" parent="1">
          <mxGeometry x="20" y="20" width="120" height="60" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""


def run_validator(xml: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "fixture.drawio"
        path.write_text(xml, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(path)],
            check=False,
            capture_output=True,
            text=True,
        )


class ValidateDrawioXmlTest(unittest.TestCase):
    def test_valid_required_attributes_pass(self) -> None:
        result = run_validator(VALID_XML)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK: fixture.drawio", result.stdout)

    def test_missing_adaptive_colors_fails(self) -> None:
        result = run_validator(VALID_XML.replace(' adaptiveColors="auto"', ""))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('must set adaptiveColors="auto"', result.stderr)

    def test_cell_style_without_html_fails(self) -> None:
        result = run_validator(VALID_XML.replace("rounded=1;html=1;", "rounded=1;"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("style must include html=1", result.stderr)


if __name__ == "__main__":
    unittest.main()
