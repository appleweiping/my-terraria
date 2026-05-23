# Per-Save Metadata Specification

> Schema for `.meta.json` sidecar files. Every save in the archive should eventually have one. The catalog generator (`tools/build_catalog.py`) reads these files to build the version compatibility matrix and metadata coverage stats.

---

## File Location

Sidecar files live alongside the save file they describe:

```
Terraria_saves/Worlds/My World.wld
Terraria_saves/Worlds/My World.meta.json
```

For imported saves, the sidecar goes inside the import directory:

```
Terraria_saves/imported/story-of-red-cloud/
  The Story of Red Cloud.wld
  The Story of Red Cloud.meta.json
  THIRD_PARTY_NOTICE.md
```

---

## Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "title": "TerrariaSaveMeta",
  "type": "object",
  "required": ["schema_version", "save_type", "terraria_version", "sha256"],
  "properties": {

    "schema_version": {
      "type": "string",
      "description": "Metadata schema version. Current: '1.0'",
      "example": "1.0"
    },

    "save_type": {
      "type": "string",
      "enum": ["world", "player"],
      "description": "Whether this describes a .wld or .plr file"
    },

    "terraria_version": {
      "type": "string",
      "description": "Terraria version string the save was last opened in",
      "example": "1.4.4.9"
    },

    "sha256": {
      "type": "string",
      "description": "SHA-256 hex digest of the save file at time of archival",
      "example": "a3f2c1..."
    },

    "archived_date": {
      "type": "string",
      "format": "date",
      "description": "ISO 8601 date when this save was added to the archive",
      "example": "2026-05-15"
    },

    "tier": {
      "type": "string",
      "enum": ["S", "A", "B", "personal", "original"],
      "description": "Quality tier per ROADMAP section 2. Use 'personal' for personal saves, 'original' for originals."
    },

    "description": {
      "type": "string",
      "description": "One-line description of the save's purpose or content"
    },

    "world": {
      "type": "object",
      "description": "World-specific fields (only for save_type=world)",
      "properties": {
        "name": { "type": "string" },
        "size": { "type": "string", "enum": ["small", "medium", "large"] },
        "difficulty": { "type": "string", "enum": ["classic", "expert", "master", "journey"] },
        "seed": { "type": "string", "description": "World seed if known" },
        "special_seed": { "type": "string", "description": "Named special seed (e.g. 'getfixedboi', 'for the worthy')" },
        "hardmode": { "type": "boolean" },
        "post_moonlord": { "type": "boolean" },
        "chest_count": { "type": "integer" },
        "sign_count": { "type": "integer" },
        "npc_count": { "type": "integer" },
        "corruption_type": { "type": "string", "enum": ["corruption", "crimson", "both"] },
        "notes": { "type": "string" }
      }
    },

    "player": {
      "type": "object",
      "description": "Player-specific fields (only for save_type=player)",
      "properties": {
        "name": { "type": "string" },
        "difficulty": { "type": "string", "enum": ["classic", "mediumcore", "hardcore", "journey"] },
        "hp": { "type": "integer" },
        "mana": { "type": "integer" },
        "class": { "type": "string", "enum": ["melee", "ranged", "mage", "summoner", "mixed", "utility"] },
        "progression_stage": { "type": "string", "description": "e.g. 'pre-hardmode', 'post-plantera', 'post-moonlord'" },
        "paired_world": { "type": "string", "description": "Name of the world this character is designed for" },
        "notes": { "type": "string" }
      }
    },

    "compatibility": {
      "type": "object",
      "description": "Version compatibility test results",
      "additionalProperties": {
        "type": "string",
        "enum": ["ok", "untested", "broken"],
        "description": "Load test result for a given Terraria version"
      },
      "example": {
        "1.4.4.9": "ok",
        "1.4.5.x": "untested"
      }
    },

    "source": {
      "type": "object",
      "description": "Provenance fields (for imported saves only)",
      "properties": {
        "url": { "type": "string", "format": "uri" },
        "author": { "type": "string" },
        "license": { "type": "string" },
        "retrieved_date": { "type": "string", "format": "date" }
      }
    }

  }
}
```

---

## Minimal Example (personal world)

```json
{
  "schema_version": "1.0",
  "save_type": "world",
  "terraria_version": "1.4.4.9",
  "sha256": "a3f2c1d4e5b6...",
  "archived_date": "2026-05-15",
  "tier": "personal",
  "description": "Main survival world, post-Moon Lord",
  "world": {
    "name": "My World",
    "size": "large",
    "difficulty": "expert",
    "hardmode": true,
    "post_moonlord": true,
    "chest_count": 412
  }
}
```

## Full Example (public import)

```json
{
  "schema_version": "1.0",
  "save_type": "world",
  "terraria_version": "1.4.4.9",
  "sha256": "b7c8d9e0f1a2...",
  "archived_date": "2026-05-15",
  "tier": "S",
  "description": "Iconic adventure/RPG campaign with Dark Souls-inspired difficulty",
  "world": {
    "name": "The Story of Red Cloud",
    "size": "large",
    "difficulty": "expert",
    "hardmode": true,
    "post_moonlord": false,
    "notes": "Requires tsorcRevamp tModLoader mod v1.4.4"
  },
  "compatibility": {
    "1.4.4.9": "ok",
    "1.4.5.x": "untested"
  },
  "source": {
    "url": "https://github.com/timhjersted/tsorcDownload",
    "author": "Tim Hjersted",
    "license": "Public Domain",
    "retrieved_date": "2026-05-15"
  }
}
```

---

## Tooling

The catalog generator reads `.meta.json` files automatically when present. Fields not in the sidecar are omitted from the catalog rather than causing errors — the schema is additive.

To validate a sidecar against this spec:

```bash
python tools/build_catalog.py --check
```

The `--check` flag validates all discovered `.meta.json` files for required fields and enum values.
