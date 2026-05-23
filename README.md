<p align="center">
  <img src="docs/banner.png" alt="My Terraria" width="720" />
</p>

<p align="center">
  <strong>Source-traceable Terraria save archive with curated imports, original projects, and a full programmatic generation engine.</strong>
</p>

<p align="center">
  <a href="https://github.com/appleweiping/my-terraria/blob/main/LICENSE"><img src="https://img.shields.io/github/license/appleweiping/my-terraria?style=for-the-badge" alt="License" /></a>
  <a href="https://git-lfs.github.com/"><img src="https://img.shields.io/badge/Git%20LFS-enabled-blue?style=for-the-badge&logo=git" alt="Git LFS" /></a>
  <a href="https://store.steampowered.com/app/105600/Terraria/"><img src="https://img.shields.io/badge/Terraria-1.4.x-green?style=for-the-badge&logo=steam" alt="Terraria" /></a>
  <a href="https://github.com/appleweiping/my-terraria/actions"><img src="https://img.shields.io/github/actions/workflow/status/appleweiping/my-terraria/ci.yml?style=for-the-badge&label=CI" alt="CI" /></a>
</p>

---

## What Is This?

A structured, version-controlled archive of Terraria save data — personal worlds, players, curated third-party imports, and original flagship builds. Every binary is stored via Git LFS, every import carries full provenance, and every expansion follows documented governance rules.

This is not a download folder. It is an engineered collection with:

- **Programmatic generation** — worlds and characters built from JSON specs via TerrariaAgentFramework
- **Curatorial standards** — quality tiers, acceptance checklists, and provenance for every import
- **Automated integrity** — CI checks catalog consistency, LFS pointers, and provenance on every commit
- **Full documentation** — design docs, build logs, metadata sidecars, and naming conventions

---

## Numbers

| Metric | Count |
|--------|------:|
| Personal worlds | 44 |
| Personal players | 54 |
| Public imports | 5 |
| Original projects | 5 |
| Paired characters | 17 |
| Tracked binary files | 330+ |
| Framework version | v2.1 |

---

## Showcase

<p align="center">
  <img src="docs/showcase-1.png" alt="World showcase" width="720" />
</p>

<p align="center">
  <img src="docs/showcase-2.png" alt="Build showcase" width="720" />
</p>

<p align="center">
  <img src="docs/showcase-3.png" alt="Archive showcase" width="720" />
</p>

---

## Original Projects

Five purpose-built worlds that exist nowhere else. Each has a design document, acceptance checklist, and paired characters.

| Project | Status | Worlds | Characters | Purpose |
|---------|--------|-------:|----------:|---------|
| **Astral Forge Vault** | ✅ Complete | 1 | 5 | Ultimate storage hub — 634 chests, `getfixedboi` seed |
| **Biome Encyclopedia** | ✅ Complete | 1 | 2 | All 30 biomes — hub, teleporter network, 599 chests, 200 signs |
| **Boss Rush Colosseum** | ✅ Complete | 1 | 5 | Every boss arena, optimized layouts, full summon chests |
| **Wiring Masterclass** | ✅ Complete | 1 | 2 | 6-section wiring reference from basics to hoik engines |
| **Starter Academy** | ✅ Complete | 1 | 3 | New player progression guide with 3 checkpoint characters |

### Astral Forge Vault

The repository's flagship — a purpose-built archive hub world for maximum utility and completeness.

| Property | Value |
|----------|-------|
| Profile | Vanilla 1.4.x, Large, Master mode |
| Seed | `getfixedboi` base |
| Chests | 634 |
| Signs | 46 |
| Paired characters | 5 (Astral Warden, Nebula Archivist, Vortex Curator, Stardust Keeper, Solar Courier) |

---

## Public Import Collection

| Save | Category | License | Tier |
|------|----------|---------|------|
| The Story of Red Cloud | Adventure / RPG | Public Domain | S |
| The Story of Red Cloud — Xelvaa Remix | Adventure / Dark Souls | Public Domain | S |
| All Boss Battle Arenas Expert | Boss arena / Combat | CC BY-NC 3.0 | A |
| SUNV XTRA All Items Hub 1.4.5 Master | Compact all-items | GPL-3.0 | S |
| A Link to Terraria | Adventure / Zelda recreation | AGPLv3 | S |

Full provenance records in `external-sources/`. Every import has a `THIRD_PARTY_NOTICE.md` and a `.meta.json` sidecar.

---

## TerrariaAgentFramework (v2.1)

A C# CLI and library that generates Terraria worlds and characters from JSON specifications. Designed for AI agents to create game content programmatically.

### Capabilities

| Module | What It Does |
|--------|-------------|
| `WorldBuilder` | Load/create worlds, set title/size/difficulty/spawn |
| `PlayerBuilder` | Create characters with full loadouts, god mode, prefixes |
| `BiomeFactory` | 15 biome section generators with correct block thresholds |
| `StructureFactory` | Arenas, storage vaults, NPC housing, farms, crafting hubs |
| `ArchitectureFactory` | Castle, sky palace, pagoda, treehouse, dome, pyramid, colosseum, etc. |
| `TerrainFactory` | Mountains, lakes, caves, floating islands, waterfalls, lava rivers, crystal caverns |
| `ItemLookup` | Fuzzy name-to-ID resolution for all tiles, walls, and items |
| `AstralForgeBuilder` | Specialized builder for the Astral Forge Vault flagship world |
| `BiomeEncyclopediaBuilder` | Specialized builder for the Biome Encyclopedia — all 30 biomes |
| `WorldMetadataExtractor` | Extracts metadata (name, size, difficulty, chest count, SHA-256) from .wld files |

### Agent Modules

| Module | What It Does |
|--------|-------------|
| `TerrariaGameAgent` | Connects to Terraria server via protocol, controls player with A* pathfinding |
| `TerrariaAgentMod` | tModLoader mod exposing TCP command server — 12 commands, 8 building patterns |

### Quick Start

```powershell
$dotnet = "D:\Terraria_doc\.work\dotnet\dotnet.exe"
$proj   = "D:\Terraria_doc\.work\TerrariaAgentFramework\TerrariaAgentFramework.csproj"

# Generate a world from spec
& $dotnet run --project $proj -- --spec Specs/boss-rush-colosseum.json --output D:\output\

# Create a god-mode melee character
& $dotnet run --project $proj -- --player "Solar Warden" --class melee --god --output player.plr
```

### JSON Spec Example

```json
{
  "title": "Boss Rush Colosseum",
  "size": "Large",
  "difficulty": "Master",
  "hub": { "type": "celestial" },
  "structures": [
    { "type": "boss_arena", "x": 1000, "y": 500, "params": { "tiers": "8" } },
    { "type": "storage_vault", "x": 4200, "y": 300, "params": { "chests": "30" } }
  ],
  "architecture": [
    { "type": "colosseum", "x": 5000, "y": 500 }
  ],
  "teleporterNetwork": true,
  "players": [
    {
      "name": "Melee Champion",
      "maxStats": true,
      "godMode": true,
      "armor": ["Solar Flare Helmet", "Solar Flare Breastplate", "Solar Flare Leggings"],
      "weapons": ["Zenith", "Solar Eruption", "Daybreak"],
      "items": [{ "name": "Celestial Sigil", "stack": 99 }]
    }
  ]
}
```

See [`docs/agent-framework-api.md`](docs/agent-framework-api.md) for the complete API reference.

---

## Repository Structure

```
my-terraria/
├── .github/workflows/ci.yml     # CI: catalog check, LFS validation, provenance
├── Terraria_saves/
│   ├── Players/                 # 54 personal player files (.plr via Git LFS)
│   ├── Worlds/                  # 44 personal world files (.wld via Git LFS)
│   └── imported/                # 5 public third-party imports with provenance
│       ├── story-of-red-cloud/
│       ├── story-of-red-cloud-xelvaa-remix/
│       ├── all-boss-battle-arenas/
│       ├── compact-all-items-hub-master/
│       └── a-link-to-terraria/  # AGPLv3 — .wld pending manual download
├── originals/                   # 5 original flagship projects
│   ├── astral-forge-vault/      # ✅ Complete — ultimate storage hub
│   ├── biome-encyclopedia/      # ✅ Complete — all 30 biomes, 599 chests, 200 signs
│   ├── boss-rush-colosseum/     # ✅ Complete — every boss arena
│   ├── starter-academy/         # ✅ Complete — new player progression guide
│   └── wiring-masterclass/      # ✅ Complete — wiring reference
├── inventory/
│   ├── CATALOG.md               # Human-readable archive catalog (auto-generated)
│   └── catalog.json             # Machine-readable catalog
├── external-sources/            # Provenance records and import research logs
├── docs/
│   ├── ROADMAP.md               # Expansion roadmap with phase tracking
│   ├── agent-framework-api.md   # TerrariaAgentFramework complete API reference
│   ├── naming-conventions.md    # File and directory naming rules
│   └── metadata-spec.md         # .meta.json sidecar schema
├── tools/
│   └── build_catalog.py         # Catalog generator (dependency-free Python)
├── tests/
│   └── test_build_catalog.py    # Unit tests for catalog tooling
├── AGENTS.md                    # Governance for automated contributors
├── CLAUDE.md                    # Multi-agent collaboration config
└── CONTEXT.md                   # Domain context for agent handoffs
```

---

## Catalog and Validation

The v2.1 catalog layer generates a deterministic public inventory summary, original-project matrix, public-import provenance table, version compatibility matrix, and quality gates:

```powershell
python tools/build_catalog.py
python tools/build_catalog.py --check
```

Outputs:

- `inventory/CATALOG.md` — human-readable archive catalog
- `inventory/catalog.json` — machine-readable catalog for future automation

CI runs `--check` on every push to verify catalog consistency.

---

## Quick Start

```powershell
# Clone with LFS
git lfs install
git clone https://github.com/appleweiping/my-terraria.git
cd my-terraria
git lfs pull

# Restore worlds to Terraria
Copy-Item "Terraria_saves\Worlds\*.wld" `
    -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Worlds" -Force

# Restore players to Terraria
Copy-Item "Terraria_saves\Players\*.plr" `
    -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Players" -Force

# Run catalog check
python tools/build_catalog.py --check
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Expansion roadmap — content pillars, quality tiers, phase tracking |
| [`docs/agent-framework-api.md`](docs/agent-framework-api.md) | TerrariaAgentFramework complete API reference |
| [`docs/naming-conventions.md`](docs/naming-conventions.md) | Canonical naming rules for files and directories |
| [`docs/metadata-spec.md`](docs/metadata-spec.md) | `.meta.json` sidecar schema with examples |
| [`AGENTS.md`](AGENTS.md) | Governance rules for automated contributors |
| [`CONTEXT.md`](CONTEXT.md) | Domain context and current project state |

---

## Contributing

Contributions must follow the expansion protocol in [`AGENTS.md`](AGENTS.md):

1. Search broadly (GitHub, CurseForge, Steam Workshop, forums)
2. Prefer high-signal saves (popular, novel, complete, well-documented)
3. Use Git LFS for all binary save files
4. Record full provenance (source URL, author, SHA-256, license)
5. Respect licensing — only redistribution-compatible saves go public
6. Add a `.meta.json` sidecar for every new save (see [`docs/metadata-spec.md`](docs/metadata-spec.md))

---

## License

Original content licensed under [`LICENSE`](LICENSE). Third-party saves retain their original licenses — see [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and per-import `THIRD_PARTY_NOTICE.md` files.
