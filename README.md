# My Terraria Archive

A source-traceable Terraria save archive: local player/world backups, curated third-party imports, and original non-toy save projects built to be restored, inspected, extended, and versioned.

This is not a screenshot gallery or a loose pile of downloads. The repository is maintained as an archive project: binary saves are stored with Git LFS, third-party sources are recorded with provenance and hashes, and future expansion rules live in `AGENTS.md`.

## What Is Inside

| Area | Purpose | Contents |
|---|---|---|
| `Terraria_saves/Players/` | User/player archive | Local `.plr`, `.map`, and `.bak` player data backed up from this machine. |
| `Terraria_saves/Worlds/` | User/world archive | Local `.wld` and `.bak` worlds, including all-item maps, farms, builds, challenge worlds, and existing personal saves. |
| `Terraria_saves/imported/` | Public third-party imports | Curated external saves whose source pages show redistribution-compatible licenses, each with a `THIRD_PARTY_NOTICE.md`. |
| `originals/astral-forge-vault/` | Original flagship project | A vanilla 1.4.x large master `getfixedboi` world upgraded with an archive hub, arenas, farms, transit, labels, chests, and paired characters. |
| `inventory/` | Audit layer | File inventory, analysis, hashes, restore guidance, and expansion log. |
| `external-sources/` | Source research | Candidate scans, import decisions, download provenance, source URLs, file ids, and SHA-256 records. |
| `private-imports/` | Local-only private cache | High-signal third-party saves with restrictive or unclear redistribution terms. This path is intentionally ignored by Git. |

## Current Public Import Set

These are real `.wld` files tracked with Git LFS, not placeholder documentation.

| Save | Type | Source license observed | Path |
|---|---|---|---|
| The Story of Red Cloud | Adventure / RPG world | Public Domain | `Terraria_saves/imported/story-of-red-cloud/the-story-of-red-cloud.wld` |
| All Boss Battle Arenas Expert | Boss arena / combat utility | Creative Commons Attribution-NonCommercial 3.0 Unported | `Terraria_saves/imported/all-boss-battle-arenas/All Boss Battle Arenas Expert.wld` |
| SUNV XTRA All Items Hub 1.4.5 Master | Compact all-items hub | GNU General Public License version 3 | `Terraria_saves/imported/compact-all-items-hub-master/SUNV-XTRA-All-ITEMS-HUB-1.4.5-Master.wld` |

See `external-sources/2026-05-15-curseforge-imports.md` for source URLs, authors, file ids, sizes, SHA-256 hashes, and the private/public import decision for the full CurseForge batch.

## Local Private Backup Set

The following real third-party save files were downloaded to `D:\Terraria_doc\private-imports\2026-05-15-curseforge` on the archive machine:

| Save | Category | Local status |
|---|---|---|
| Builder's Workshop | canonical all-items worlds | Private-only local backup, not pushed while the repo is public. |
| Ztorage Zystem | storage worlds plus matching players | Private-only local backup, not pushed while the repo is public. |
| The Shimmer Lands | visual all-items hub | Private-only local backup, not pushed while the repo is public. |
| Khaiostomization | building/customization showcase | Private-only local backup, not pushed while the repo is public. |
| Scopey 1.4.5 All Items | current-version all-items world | Private-only local backup, not pushed while the repo is public. |
| Starter World 1.4.4.9 Master | starter/progression utility | Private-only local backup, not pushed while the repo is public. |
| The Kingdom | building/settlement world | Private-only local backup, not pushed while the repo is public. |

Those files are intentionally excluded by `.gitignore` because this GitHub repository is currently public and the source pages showed All Rights Reserved. If this repository is made private, they can be promoted into a private Git LFS area in source-by-source commits while preserving notices and hashes.

## Original Flagship: Astral Forge Vault

`originals/astral-forge-vault/` is the first original save project in the archive.

- World: `Astral_Forge_Vault.wld`
- Terraria profile: vanilla 1.4.x, large master, `getfixedboi` seed base
- Final read-back title: `Astral Forge Vault - Ultimate Archive`
- Final read-back spawn: `(4200,430)`
- Final read-back content markers: 634 chests, 46 signs
- Paired characters:
  - `Astral_Warden.plr`
  - `Nebula_Archivist.plr`
  - `Vortex_Curator.plr`
  - `Stardust_Keeper.plr`
  - `Solar_Courier.plr`

The design, validation checklist, and restore notes are in `originals/astral-forge-vault/README.md`, `design.md`, and `acceptance-checklist.md`.

## Restore Guide

1. Install Git LFS before cloning:

   ```powershell
   git lfs install
   git clone https://github.com/appleweiping/my-terraria.git
   cd my-terraria
   git lfs pull
   ```

2. Copy world files into the Terraria worlds folder:

   ```powershell
   Copy-Item -LiteralPath "Terraria_saves\Worlds\*.wld" -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Worlds" -Force
   ```

3. Copy player files into the Terraria players folder:

   ```powershell
   Copy-Item -LiteralPath "Terraria_saves\Players\*.plr" -Destination "$env:USERPROFILE\Documents\My Games\Terraria\Players" -Force
   ```

4. For imported or original subprojects, copy the specific `.wld` and `.plr` files from their project folders into the same Terraria `Worlds` and `Players` restore locations.

Back up existing Terraria saves before overwriting files in the live game folder.

## Verification

Useful checks:

```powershell
git lfs status
git lfs ls-files
Get-FileHash -Algorithm SHA256 -LiteralPath "path\to\save.wld"
```

The archive's maintained records live in:

- `inventory/terraria-file-inventory.csv`
- `inventory/terraria-file-analysis.md`
- `inventory/expansion-log.md`
- `external-sources/2026-05-15-curseforge-imports.md`

## Expansion Rules

Future agents should follow `AGENTS.md`:

- Search broadly: GitHub, CurseForge, Steam Workshop, official forums, and known community map pages.
- Prefer high-signal saves: popular, novel, complete, actively maintained, well-documented, or structurally different from the current archive.
- Preserve complete save sets: `.wld`, `.plr`, `.map`, `.bak`, `.twld`, `.tplr`, archives, readmes, mod lists, and source notes when they belong together.
- Use Git LFS for binary save files.
- Keep source provenance and SHA-256 hashes for every import.
- Do not present toy/demo saves as final original work.

## Licensing

Repository text and original project material use the root `LICENSE` unless a file says otherwise.

Third-party saves keep their original source-page license or permission status and are not relicensed as MIT by this repository. See `THIRD_PARTY_NOTICES.md` and each imported save's `THIRD_PARTY_NOTICE.md`.

