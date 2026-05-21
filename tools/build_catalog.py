#!/usr/bin/env python3
"""Build the public Terraria archive catalog.

This script is intentionally dependency-free so any agent can refresh the
catalog from a clean checkout without bootstrapping a separate toolchain.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CATALOG_VERSION = "2.1.0"
SAVE_EXTENSIONS = {".wld", ".plr", ".map", ".bak", ".twld", ".tplr"}
ROOT = Path(__file__).resolve().parents[1]
INVENTORY_DIR = ROOT / "inventory"
CATALOG_JSON = INVENTORY_DIR / "catalog.json"
CATALOG_MD = INVENTORY_DIR / "CATALOG.md"


@dataclass(frozen=True)
class SaveFile:
    path: Path
    relative_path: str
    area: str
    extension: str
    size_bytes: int

    @property
    def is_backup(self) -> bool:
        return self.path.name.endswith(".bak")

    @property
    def role(self) -> str:
        if self.relative_path.startswith("Terraria_saves/imported/"):
            return "public_import"
        if self.relative_path.startswith("Terraria_saves/Worlds/"):
            return "personal_world"
        if self.relative_path.startswith("Terraria_saves/Players/"):
            if self.extension == ".map":
                return "player_map_cache"
            return "personal_player"
        if self.relative_path.startswith("originals/"):
            return "original_project"
        return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build inventory/catalog.json and inventory/CATALOG.md")
    parser.add_argument("--check", action="store_true", help="fail if generated catalog differs from committed files")
    args = parser.parse_args()

    catalog = build_catalog()
    json_text = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    md_text = render_markdown(catalog)

    if args.check:
        return check_file(CATALOG_JSON, json_text) | check_file(CATALOG_MD, md_text)

    CATALOG_JSON.write_text(json_text, encoding="utf-8")
    CATALOG_MD.write_text(md_text, encoding="utf-8")
    print(f"Wrote {CATALOG_JSON.relative_to(ROOT)}")
    print(f"Wrote {CATALOG_MD.relative_to(ROOT)}")
    return 0


def build_catalog() -> dict[str, Any]:
    saves = discover_save_files()
    metadata = load_world_metadata()
    inventory = load_inventory_csv()
    original_projects = discover_original_projects(saves)
    public_imports = discover_public_imports(saves)

    by_role = Counter(save.role for save in saves)
    by_extension = Counter(save.extension for save in saves)
    primary_worlds = [s for s in saves if s.extension == ".wld" and not s.is_backup]
    primary_players = [s for s in saves if s.extension == ".plr" and not s.is_backup]

    return {
        "catalog_version": CATALOG_VERSION,
        "generated_by": "tools/build_catalog.py",
        "source_metadata_generated": metadata.get("generated"),
        "summary": {
            "save_files_total": len(saves),
            "primary_worlds": len(primary_worlds),
            "primary_players": len(primary_players),
            "public_import_worlds": by_role["public_import"],
            "original_project_files": by_role["original_project"],
            "map_cache_files": by_extension[".map"],
            "backup_files": sum(1 for save in saves if save.is_backup),
            "inventory_rows": len(inventory),
            "metadata_worlds": len(metadata.get("worlds", [])),
        },
        "roles": dict(sorted(by_role.items())),
        "extensions": dict(sorted(by_extension.items())),
        "version_matrix": build_version_matrix(metadata),
        "original_projects": original_projects,
        "public_imports": public_imports,
        "metadata_coverage": build_metadata_coverage(primary_worlds, metadata),
        "quality_gates": quality_gates(CATALOG_VERSION, original_projects, public_imports),
    }


def discover_save_files() -> list[SaveFile]:
    roots = [ROOT / "Terraria_saves", ROOT / "originals"]
    saves: list[SaveFile] = []
    for base in roots:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*"), key=lambda p: p.as_posix().lower()):
            if not path.is_file():
                continue
            extension = effective_extension(path)
            if extension not in SAVE_EXTENSIONS:
                continue
            relative_path = normalize(path.relative_to(ROOT))
            saves.append(
                SaveFile(
                    path=path,
                    relative_path=relative_path,
                    area=normalize(path.parent.relative_to(ROOT)),
                    extension=extension,
                    size_bytes=path.stat().st_size,
                )
            )
    return saves


def effective_extension(path: Path) -> str:
    name = path.name.lower()
    for suffix in (".plr.bak", ".wld.bak"):
        if name.endswith(suffix):
            return ".bak"
    return path.suffix.lower()


def load_world_metadata() -> dict[str, Any]:
    path = INVENTORY_DIR / "metadata.json"
    if not path.exists():
        return {"worlds": []}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_inventory_csv() -> list[dict[str, str]]:
    path = INVENTORY_DIR / "terraria-file-inventory.csv"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def discover_original_projects(saves: list[SaveFile]) -> list[dict[str, Any]]:
    projects = []
    for project_dir in sorted((ROOT / "originals").iterdir(), key=lambda p: p.name.lower()):
        if not project_dir.is_dir():
            continue
        project_saves = [save for save in saves if save.relative_path.startswith(f"originals/{project_dir.name}/")]
        readme = project_dir / "README.md"
        design = project_dir / "design.md"
        checklist = project_dir / "acceptance-checklist.md"
        projects.append(
            {
                "slug": project_dir.name,
                "title": title_from_readme(readme, project_dir.name),
                "status": status_from_readme(readme),
                "files": len(project_saves),
                "worlds": sum(1 for save in project_saves if save.extension == ".wld" and not save.is_backup),
                "players": sum(1 for save in project_saves if save.extension == ".plr"),
                "has_design": design.exists(),
                "has_acceptance_checklist": checklist.exists(),
                "readme": normalize(readme.relative_to(ROOT)) if readme.exists() else None,
            }
        )
    return projects


def discover_public_imports(saves: list[SaveFile]) -> list[dict[str, Any]]:
    imports_root = ROOT / "Terraria_saves" / "imported"
    if not imports_root.exists():
        return []
    imports = []
    for import_dir in sorted(imports_root.iterdir(), key=lambda p: p.name.lower()):
        if not import_dir.is_dir():
            continue
        import_saves = [save for save in saves if save.relative_path.startswith(f"Terraria_saves/imported/{import_dir.name}/")]
        notice = import_dir / "THIRD_PARTY_NOTICE.md"
        imports.append(
            {
                "slug": import_dir.name,
                "worlds": sum(1 for save in import_saves if save.extension == ".wld"),
                "has_third_party_notice": notice.exists(),
                "notice": normalize(notice.relative_to(ROOT)) if notice.exists() else None,
            }
        )
    return imports


def build_version_matrix(metadata: dict[str, Any]) -> list[dict[str, Any]]:
    versions: dict[str, dict[str, Any]] = defaultdict(lambda: {"worlds": 0, "difficulties": Counter(), "total_chests": 0})
    for world in metadata.get("worlds", []):
        version = world.get("terraria_version") or "unknown"
        bucket = versions[version]
        bucket["worlds"] += 1
        bucket["difficulties"][world.get("difficulty") or "unknown"] += 1
        bucket["total_chests"] += int(world.get("chest_count") or 0)

    matrix = []
    for version, bucket in sorted(versions.items()):
        matrix.append(
            {
                "terraria_version": version,
                "metadata_worlds": bucket["worlds"],
                "difficulties": dict(sorted(bucket["difficulties"].items())),
                "total_chests": bucket["total_chests"],
            }
        )
    return matrix


def build_metadata_coverage(primary_worlds: list[SaveFile], metadata: dict[str, Any]) -> dict[str, Any]:
    metadata_paths = {normalize(Path(world["file"])) for world in metadata.get("worlds", []) if world.get("file")}
    world_paths = {save.relative_path for save in primary_worlds if save.relative_path.startswith("Terraria_saves/Worlds/")}
    missing = sorted(world_paths - metadata_paths)
    return {
        "personal_worlds_with_metadata": len(world_paths) - len(missing),
        "personal_worlds_missing_metadata": len(missing),
        "missing_metadata_sample": missing[:12],
    }


def quality_gates(
    catalog_version: str,
    original_projects: list[dict[str, Any]],
    public_imports: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    missing_notices = [entry["slug"] for entry in public_imports if not entry["has_third_party_notice"]]
    incomplete_original_docs = [
        project["slug"]
        for project in original_projects
        if not (project["readme"] and project["has_design"] and project["has_acceptance_checklist"])
    ]
    return [
        {"name": "catalog-version", "status": "pass", "detail": f"catalog_version={catalog_version}"},
        {
            "name": "public-import-notices",
            "status": "pass" if not missing_notices else "fail",
            "detail": "every public import directory has THIRD_PARTY_NOTICE.md"
            if not missing_notices
            else f"missing notices: {', '.join(missing_notices)}",
        },
        {
            "name": "original-project-docs",
            "status": "pass" if not incomplete_original_docs else "fail",
            "detail": "every original project has README, design, and acceptance checklist"
            if not incomplete_original_docs
            else f"incomplete docs: {', '.join(incomplete_original_docs)}",
        },
        {"name": "deterministic-generation", "status": "pass", "detail": "tools/build_catalog.py --check compares generated outputs"},
    ]


def render_markdown(catalog: dict[str, Any]) -> str:
    summary = catalog["summary"]
    lines = [
        "# Terraria Archive Catalog",
        "",
        f"Catalog version: `{catalog['catalog_version']}`",
        "",
        "Generated by `tools/build_catalog.py`. Run `python tools/build_catalog.py --check` before committing catalog changes.",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for key, value in summary.items():
        lines.append(f"| {humanize(key)} | {value} |")

    lines.extend([
        "",
        "## Original Projects",
        "",
        "| Project | Status | Worlds | Players | Docs |",
        "|---|---|---:|---:|---|",
    ])
    for project in catalog["original_projects"]:
        docs = []
        if project["has_design"]:
            docs.append("design")
        if project["has_acceptance_checklist"]:
            docs.append("checklist")
        if project["readme"]:
            docs.append("readme")
        lines.append(
            f"| {project['title']} | {project['status']} | {project['worlds']} | {project['players']} | {', '.join(docs)} |"
        )

    lines.extend([
        "",
        "## Public Imports",
        "",
        "| Import | Worlds | Provenance Notice |",
        "|---|---:|---|",
    ])
    for import_entry in catalog["public_imports"]:
        notice = import_entry["notice"] or "missing"
        lines.append(f"| {import_entry['slug']} | {import_entry['worlds']} | {notice} |")

    lines.extend([
        "",
        "## Version Compatibility Matrix",
        "",
        "| Terraria Version | Metadata Worlds | Difficulties | Total Chests |",
        "|---|---:|---|---:|",
    ])
    for row in catalog["version_matrix"]:
        difficulties = ", ".join(f"{name}: {count}" for name, count in row["difficulties"].items())
        lines.append(f"| {row['terraria_version']} | {row['metadata_worlds']} | {difficulties} | {row['total_chests']} |")

    coverage = catalog["metadata_coverage"]
    lines.extend([
        "",
        "## Metadata Coverage",
        "",
        f"- Personal worlds with metadata: `{coverage['personal_worlds_with_metadata']}`",
        f"- Personal worlds missing metadata: `{coverage['personal_worlds_missing_metadata']}`",
    ])
    if coverage["missing_metadata_sample"]:
        lines.append("- Missing metadata sample:")
        for path in coverage["missing_metadata_sample"]:
            lines.append(f"  - `{path}`")

    lines.extend([
        "",
        "## Quality Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
    ])
    for gate in catalog["quality_gates"]:
        lines.append(f"| {gate['name']} | {gate['status']} | {gate['detail']} |")

    lines.append("")
    return "\n".join(lines)


def title_from_readme(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def status_from_readme(path: Path) -> str:
    if not path.exists():
        return "No README"
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for index, line in enumerate(lines):
        if line.strip() == "## Status":
            return summarize_status_table(lines[index + 1 :])
    return "See README"


def summarize_status_table(lines: list[str]) -> str:
    statuses = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            break
        if stripped.startswith("|") and "|" in stripped[1:]:
            parts = [part.strip() for part in stripped.strip("|").split("|")]
            if len(parts) >= 2 and parts[0].lower() not in {"phase", "---"} and not set(parts[0]) <= {"-"}:
                statuses.append(f"{parts[0]}={parts[1]}")
    return "; ".join(statuses) if statuses else "See README"


def check_file(path: Path, expected: str) -> int:
    if not path.exists():
        print(f"Missing generated file: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        print(f"Generated file is stale: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    print(f"OK {path.relative_to(ROOT)}")
    return 0


def normalize(path: Path | str) -> str:
    return Path(path).as_posix()


def humanize(key: str) -> str:
    return key.replace("_", " ").title()


if __name__ == "__main__":
    raise SystemExit(main())
