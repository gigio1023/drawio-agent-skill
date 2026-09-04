from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from validate_svg import validate_svg


class ValidateSvgTests(unittest.TestCase):
    def test_accepts_svg_with_positive_viewbox_and_unique_ids(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "valid.svg"
            path.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 10">'
                '<rect id="node" width="20" height="10"/></svg>',
                encoding="utf-8",
            )
            self.assertEqual(validate_svg(path), [])

    def test_rejects_missing_viewbox_and_duplicate_ids(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.svg"
            path.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg">'
                '<g id="same"/><g id="same"/></svg>',
                encoding="utf-8",
            )
            self.assertEqual(
                validate_svg(path),
                ["SVG has no viewBox", "duplicate ids: same"],
            )


if __name__ == "__main__":
    unittest.main()
