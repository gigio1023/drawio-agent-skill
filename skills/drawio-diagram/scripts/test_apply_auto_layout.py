from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import xml.etree.ElementTree as ET

from apply_auto_layout import restore_adaptive_colors


class RestoreAdaptiveColorsTests(unittest.TestCase):
    def test_restores_full_document_models(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "diagram.drawio"
            path.write_text(
                '<mxfile><diagram><mxGraphModel><root/></mxGraphModel></diagram></mxfile>',
                encoding="utf-8",
            )
            self.assertEqual(restore_adaptive_colors(path), 1)
            model = next(ET.parse(path).getroot().iter("mxGraphModel"))
            self.assertEqual(model.get("adaptiveColors"), "auto")

    def test_restores_bare_model(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "diagram.drawio"
            path.write_text("<mxGraphModel><root/></mxGraphModel>", encoding="utf-8")
            self.assertEqual(restore_adaptive_colors(path), 1)
            self.assertEqual(
                ET.parse(path).getroot().get("adaptiveColors"),
                "auto",
            )


if __name__ == "__main__":
    unittest.main()
