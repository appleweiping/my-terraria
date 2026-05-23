# Naming Conventions

> Canonical rules for file and directory naming in this archive. All new additions must follow these conventions. Existing files are grandfathered but should be migrated on next edit.

---

## 1. Save Files (`.wld`, `.plr`, `.map`, `.bak`)

### Personal Saves

Personal saves retain their original in-game names as assigned by the player. No renaming is applied.

```
Terraria_saves/
  Players/
    Astral Warden.plr
    Nebula Archivist.plr
  Worlds/
    Astral Forge Vault.wld
    My World.wld
```

### Public Imports

Imported saves use a **kebab-case slug** derived from the original title. The slug is:
- All lowercase
- Words separated by hyphens
- No special characters, parentheses, or version numbers in the slug itself
- Version or variant info goes in the directory name only if needed for disambiguation

```
Terraria_saves/imported/
  story-of-red-cloud/
    The Story of Red Cloud.wld        ← original filename preserved
    THIRD_PARTY_NOTICE.md
  compact-all-items-hub-master/
    SUNV XTRA All Items Hub 1.4.5 Master.wld
    THIRD_PARTY_NOTICE.md
```

### Original Projects

Original project worlds and characters use **Title Case** matching the project name exactly.

```
originals/
  astral-forge-vault/
    Astral Forge Vault.wld
    Astral Warden.plr
    Nebula Archivist.plr
```

---

## 2. Directory Names

| Context | Convention | Example |
|---------|-----------|---------|
| Original project root | `kebab-case` | `boss-rush-colosseum/` |
| Public import root | `kebab-case` | `story-of-red-cloud/` |
| Documentation subdirs | `kebab-case` | `external-sources/` |
| Tool subdirs | `kebab-case` | `tools/` |

---

## 3. Documentation Files

| File | Convention | Notes |
|------|-----------|-------|
| Project README | `README.md` | Always uppercase, always at project root |
| Design document | `design.md` | Lowercase, in project directory |
| Acceptance checklist | `acceptance-checklist.md` | Lowercase, in project directory |
| Provenance notice | `THIRD_PARTY_NOTICE.md` | Uppercase, in import directory |
| Catalog | `CATALOG.md` | Uppercase, in `inventory/` |
| Roadmap | `ROADMAP.md` | Uppercase, in `docs/` |
| Research logs | `YYYY-MM-DD-topic-slug.md` | Date-prefixed, in `external-sources/` |

---

## 4. Metadata Sidecar Files

Per-save metadata files use the same base name as the save file with a `.meta.json` extension.

```
Terraria_saves/Worlds/
  Astral Forge Vault.wld
  Astral Forge Vault.meta.json     ← sidecar metadata
```

See [`docs/metadata-spec.md`](metadata-spec.md) for the full schema.

---

## 5. Version Tags

When archiving multiple versions of the same save, append a version suffix:

```
story-of-red-cloud-v1.4.4/
story-of-red-cloud-v1.4.5/
```

Do not use version numbers in the base slug — only in the directory name when disambiguation is needed.

---

## 6. Prohibited Patterns

- No spaces in directory names (use hyphens)
- No uppercase in directory names (use lowercase)
- No version numbers in import slugs (use directory suffix if needed)
- No `_` underscores in new directory names (legacy `Terraria_saves/` is grandfathered)
- No special characters: `()[]{}@#$%^&*`
