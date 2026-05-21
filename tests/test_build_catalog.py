import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_build_catalog_module():
    spec = importlib.util.spec_from_file_location("build_catalog", ROOT / "tools" / "build_catalog.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class BuildCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build_catalog = load_build_catalog_module()

    def test_catalog_contains_required_archive_sections(self):
        catalog = self.build_catalog.build_catalog()

        self.assertEqual(catalog["catalog_version"], "2.1.0")
        self.assertEqual(catalog["summary"]["public_import_worlds"], 4)
        self.assertGreaterEqual(catalog["summary"]["metadata_worlds"], 40)
        self.assertEqual(len(catalog["original_projects"]), 5)
        self.assertGreaterEqual(
            {project["slug"] for project in catalog["original_projects"]},
            {"astral-forge-vault", "starter-academy", "wiring-masterclass"},
        )

    def test_quality_gates_reflect_public_archive_requirements(self):
        catalog = self.build_catalog.build_catalog()
        gates = {gate["name"]: gate for gate in catalog["quality_gates"]}

        self.assertEqual(gates["public-import-notices"]["status"], "pass")
        self.assertEqual(gates["original-project-docs"]["status"], "pass")
        self.assertEqual(gates["deterministic-generation"]["status"], "pass")

    def test_markdown_render_includes_version_matrix_and_starter_academy(self):
        markdown = self.build_catalog.render_markdown(self.build_catalog.build_catalog())

        self.assertIn("## Version Compatibility Matrix", markdown)
        self.assertIn("Starter Academy", markdown)
        self.assertIn("1.4.4.9", markdown)


if __name__ == "__main__":
    unittest.main()
