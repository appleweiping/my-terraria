```
╔══════════════════════════════════════════════════════════════════════════════╗
║  *  .    *       .   *    .        *   .       *    .   *       .    *     ║
║     .        *        .       *         .   *      .        *       .      ║
║  .     *  .       *      .        *  .      .   *     .  *      .     *    ║
║─────────────────────────────────────────────────────────────────────────────║
║                    ▓▓▓▓▓                                                   ║
║                  ▓▓▓▓▓▓▓▓▓          ┌────────────┐                        ║
║                ▓▓▓▓▓▓▓▓▓▓▓▓▓        │ ^^  ┌──┐  │                        ║
║              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │     │  │  │    /\                  ║
║                  ║║║║║║              │ oo  │  │  │   /  \                 ║
║                  ║║║║║║              │     └──┘  │  / /\ \                ║
║     ___          ║║║║║║              └──┬────┬───┘ / /  \ \               ║
║    [___]         ║║║║║║                 │    │    /________\              ║
║    |   |                                │    │       ║║                    ║
║                                                                            ║
║          ♦♦♦  MY TERRARIA  --  Source-Traceable Save Archive  ♦♦♦          ║
║                                                                            ║
║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║████████████████████████████████████████████████████████████████████████████║
╚══════════════════════════════════════════════════════════════════════════════╝
     Tree ^        Guide NPC ^        House ^         Pine Tree ^
     Chest: [___]                     Slime: /\
```

# My Terraria

**A source-traceable Terraria save archive with curated imports, original projects, and automated tooling.**

<!-- Badges (CI/CD placeholders) -->
<!-- ![Build Status](https://img.shields.io/github/actions/workflow/status/appleweiping/my-terraria/ci.yml?branch=main) -->
<!-- ![LFS Verified](https://img.shields.io/badge/Git%20LFS-verified-blue) -->
<!-- ![License](https://img.shields.io/github/license/appleweiping/my-terraria) -->

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Overview

This repository is a structured, version-controlled archive of Terraria save data — personal worlds, personal players, curated third-party imports, and original flagship builds. Every binary is stored via Git LFS, every import carries full provenance (source URL, author, file ID, SHA-256 hash, license), and every expansion follows documented governance rules.

The goal is not to collect saves indiscriminately. It is to maintain a high-signal archive where any save can be traced back to its origin, restored to a live Terraria installation in minutes, and extended by human or automated contributors without ambiguity about licensing or integrity.

The archive currently holds **72 personal worlds**, **91 personal players**, **3 public third-party imports** with verified redistribution rights, **7 private-only saves** excluded from the public repository due to license restrictions, and **1 original flagship project** — the Astral Forge Vault — built from scratch as a large-scale master-mode archive hub.

```
┌─────────────────────────────────────────────────────┐
│  << ARCHIVE INVENTORY >>                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [W] Worlds:      72 personal + 4 original          │
│  [P] Players:     91 personal + 12 original         │
│  [I] Imports:     3 public, 7 private               │
│  [*] Projects:    1 original flagship               │
│  [F] Framework:   v2.0 (TerrariaAgent)              │
│  [#] Integrity:   Git LFS + SHA-256                 │
│                                                     │
│  Status: VERIFIED -- All hashes match               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Architecture

```
my-terraria/
├── Terraria_saves/
│   ├── Players/              # 91 personal player files (.plr, .map, .bak)
│   ├── Worlds/               # 72 personal world files (.wld, .bak)
│   └── imported/             # Public third-party imports (Git LFS)
│       ├── story-of-red-cloud/
│       ├── all-boss-battle-arenas/
│       └── compact-all-items-hub-master/
├── originals/
│   └── astral-forge-vault/   # Original flagship project
├── inventory/                # File inventory, analysis, hashes, restore guidance
├── external-sources/         # Source research, provenance records, import decisions
├── private-imports/          # .gitignored — license-restricted local backups
├── .work/                    # .gitignored — local tooling and automation
│   ├── scripts/
│   │   ├── verify-lfs.ps1       # LFS pointer integrity verification
│   │   ├── hash-check.ps1       # SHA-256 hash validation against records
│   │   └── build-astral-forge.ps1  # Astral Forge Vault build/rebuild
│   ├── AstralForgeBuilder/      # C# world builder project
│   ├── dotnet/                  # Local .NET SDK
│   └── Terraria-Map-Editor/     # TEdit (local copy)
├── docs/
│   └── ROADMAP.md            # Project roadmap and planned milestones
├── AGENTS.md                 # Governance rules for automated contributors
├── CLAUDE.md                 # Multi-agent collaboration configuration
├── CONTEXT.md                # Domain context for agent handoffs
├── THIRD_PARTY_NOTICES.md    # Aggregated third-party license notices
└── LICENSE                   # Repository license (original content)
```

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Archive Contents

| Category | Count | Storage | Notes |
|----------|------:|---------|-------|
| Personal worlds | 72 | Git LFS | All-item maps, farms, builds, challenge worlds |
| Personal players | 91 | Git LFS | `.plr`, `.map`, `.bak` player data |
| Public imports | 3 | Git LFS | Full provenance, redistribution-compatible |
| Private imports | 7 | Local only | `.gitignored`, All Rights Reserved sources |
| Original projects | 1 | Git LFS | Astral Forge Vault (flagship) |

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Featured: Astral Forge Vault

The Astral Forge Vault is the repository's original flagship project — a purpose-built archive hub world designed for maximum utility and completeness.

| Property | Value |
|----------|-------|
| World file | `originals/astral-forge-vault/Astral_Forge_Vault.wld` |
| Profile | Vanilla 1.4.x, Large, Master mode |
| Seed | `getfixedboi` base |
| Title | Astral Forge Vault - Ultimate Archive |
| Spawn | `(4200, 430)` |
| Chests | 634 |
| Signs | 46 |
| Paired characters | 5 |

### Paired Characters

| Character | File |
|-----------|------|
| Astral Warden | `Astral_Warden.plr` |
| Nebula Archivist | `Nebula_Archivist.plr` |
| Vortex Curator | `Vortex_Curator.plr` |
| Stardust Keeper | `Stardust_Keeper.plr` |
| Solar Courier | `Solar_Courier.plr` |

Design documentation, validation checklist, and restore notes are located in the `originals/astral-forge-vault/` directory.

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Original Projects Showcase

```
┌──────────────────────────────────────────────────────────────────┐
│  << ORIGINAL BUILDS >>                                           │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [=] Astral Forge Vault    -- Ultimate storage archive hub       │
│  [B] Biome Encyclopedia    -- Every biome documented & labeled   │
│  [W] Wiring Masterclass    -- Logic gates & mechanism demos      │
│  [X] Boss Rush Colosseum   -- Every boss, arena-optimized        │
│  [>] Starter Academy       -- New player progression guide       │
│                                                                  │
│  Status: 1 complete, 4 planned (see ROADMAP.md)                  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Public Import Collection

All imports are real `.wld` files tracked with Git LFS. Each carries a `THIRD_PARTY_NOTICE.md` with source attribution.

| Save | Category | License | Path |
|------|----------|---------|------|
| The Story of Red Cloud | Adventure / RPG | Public Domain | `Terraria_saves/imported/story-of-red-cloud/` |
| All Boss Battle Arenas Expert | Boss arena / Combat utility | CC BY-NC 3.0 | `Terraria_saves/imported/all-boss-battle-arenas/` |
| SUNV XTRA All Items Hub 1.4.5 Master | Compact all-items hub | GPL-3.0 | `Terraria_saves/imported/compact-all-items-hub-master/` |

Full provenance records (source URLs, authors, file IDs, sizes, SHA-256 hashes, and import decisions) are maintained in `external-sources/2026-05-15-curseforge-imports.md`.

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Terraria Agent Framework (v2.0)

Generate worlds and characters from simple descriptions:

```
$ dotnet run -- --spec my-world.json --output ./

[*] Loading base world template...
[*] Placing 15 biome sections...
[*] Building castle at (1000, 400)...
[*] Creating teleporter network...
[*] Generating 5 paired characters...
[*] Validating chest inventory (634 chests)...
[*] Computing SHA-256 integrity hash...
[*] Done. Output: My_Epic_World.wld (11.3 MB)
```

```
┌──────────────────────────────────────────────────────────────────┐
│  << FRAMEWORK CAPABILITIES >>                                    │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [+] Programmatic world generation from JSON specs               │
│  [+] Automated NPC housing placement & validation                │
│  [+] Chest inventory population (all 5450+ items)                │
│  [+] Teleporter network wiring                                   │
│  [+] Biome painting & block placement                            │
│  [+] Character creation with loadouts                            │
│  [+] SHA-256 integrity verification on output                    │
│                                                                  │
│  Built on: .NET 8 + TEdit core libraries                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Quick Start / Restore Guide

### Prerequisites

- [Git LFS](https://git-lfs.github.com/) installed and initialized
- Terraria (Steam or GOG) installed on the target machine

### Clone and Restore

```powershell
# 1. Clone with LFS support
git lfs install
git clone https://github.com/appleweiping/my-terraria.git
cd my-terraria
git lfs pull

# 2. Verify LFS integrity
.\tools\verify-lfs.ps1

# 3. Restore worlds to Terraria
Copy-Item "Terraria_saves\Worlds\*.wld" `
    -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Worlds" -Force

# 4. Restore players to Terraria
Copy-Item "Terraria_saves\Players\*.plr" `
    -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Players" -Force
```

For imported or original subprojects, copy the specific `.wld` and `.plr` files from their project folders into the same Terraria `Worlds` and `Players` directories.

> **Warning:** Back up your existing Terraria saves before overwriting files in the live game folder.

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Tooling

Automated scripts in `.work/scripts/` support archive maintenance and validation. The `.work/` directory is gitignored (local tooling only), but the scripts are documented here for reproducibility.

| Script | Purpose |
|--------|---------|
| `verify-lfs.ps1` | Validates that all binary save files are properly tracked by Git LFS. Use `-Fix` to auto-stage missing files. |
| `hash-check.ps1` | Compares current file SHA-256 hashes against provenance records. Use `-UpdateInventory` to export results. |
| `build-astral-forge.ps1` | Builds and runs the AstralForgeBuilder C# project. Use `-Clean` for fresh builds. |

Run from the repository root:

```powershell
.\.work\scripts\verify-lfs.ps1
.\.work\scripts\hash-check.ps1
.\.work\scripts\build-astral-forge.ps1 -Clean
```

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Contributing / Expansion

Contributions — whether from human collaborators or automated agents — must follow the expansion protocol defined in `AGENTS.md`. Key principles:

1. **Search broadly.** GitHub, CurseForge, Steam Workshop, official forums, and known community map pages are all valid sources.
2. **Prefer high-signal saves.** Popular, novel, complete, actively maintained, well-documented, or structurally different from the current archive.
3. **Preserve complete save sets.** Include `.wld`, `.plr`, `.map`, `.bak`, `.twld`, `.tplr`, archives, readmes, mod lists, and source notes when they belong together.
4. **Use Git LFS** for all binary save files without exception.
5. **Record full provenance.** Source URL, author, file ID, SHA-256 hash, and observed license for every import.
6. **Respect licensing.** Only saves with redistribution-compatible licenses enter the public repository. All Rights Reserved saves remain in `private-imports/`.

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Governance

This repository is governed by strict rules defined in [`AGENTS.md`](AGENTS.md). The governance model covers:

- Permitted and prohibited actions for automated contributors
- Import criteria and quality thresholds
- Provenance and hash verification requirements
- Commit message conventions and branch policies

Multi-agent collaboration is supported through [`CLAUDE.md`](CLAUDE.md) and [`CONTEXT.md`](CONTEXT.md), which provide domain context, handoff protocols, and coordination rules for concurrent agent sessions.

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## Roadmap

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for planned milestones, including:

- CI pipeline for automated LFS and hash verification
- Expanded import coverage from additional community sources
- World metadata extraction and searchable index
- Automated backup scheduling integration

<!-- Terraria Divider -->
▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓░▒░▓

## License

Original content (text, scripts, project files) is licensed under the terms specified in [`LICENSE`](LICENSE).

Third-party saves retain their original licenses as observed on their source pages. They are **not** relicensed by this repository. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and each import's individual `THIRD_PARTY_NOTICE.md` for details.

```
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██████████████████████████████████████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                         -- End of the World --
              "You were slain by the Dungeon Guardian."
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
██████████████████████████████████████████████████████████████████████████████████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```
