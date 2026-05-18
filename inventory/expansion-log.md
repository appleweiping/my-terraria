# Expansion Log

## 2026-05-15

### Repository Operating Rules

- Added `AGENTS.md` so future agents know how to expand this archive responsibly.
- Key rule: do not import unlicensed third-party binary saves into the public GitHub repo.
- Key rule: original saves must be complete, creative, and useful; toy/demo saves are not acceptable.

### External Source Research

- Added `external-sources/2026-05-15-source-scan.md`.
- Result: GitHub has some save repositories, but the visible candidates were mostly unlicensed personal backups with weak quality signals.
- Stronger candidate surface: CurseForge / community map pages, where download counts, update dates, and install instructions are visible.
- No third-party binary save was imported in this pass because redistribution permission was not yet confirmed.

### Original Save Project

- Added `originals/astral-forge-vault/`.
- Generated `Astral_Forge_Vault.wld` as a vanilla Terraria 1.4.x large master `getfixedboi` seed/base world using `TerrariaServer.exe`.
- SHA-256: `304430452459C2060A601FA521705BBB5CE4112E46A6B8CBB0047C4D5BB1370B`
- Ran a TEdit-library builder pass that modifies the actual `.wld`.
- Upgraded world SHA-256: `41297118448C50E43DD640A98E989A8D4290010B8614D9EA710D2639130CA544`
- Status: programmatically upgraded ultimate-map v0.1, not final handcrafted release.
- Added aerial command hub, vault library, class sanctums, universal arena, farm matrix, transit spine, and named chest caches.
- Completion standard lives in `originals/astral-forge-vault/acceptance-checklist.md`.

### Astral Forge Vault v1.0 Completion Pass

- Rebuilt the actual `.wld` with valid chest/sign tile entities.
- Final saved world read-back check: title `Astral Forge Vault - Ultimate Archive`, spawn `(4200,430)`, 634 chests, 46 signs.
- Added crafting core, valid in-world labels, and paired character files.
- Added five paired characters:
  - `Astral_Warden.plr`
  - `Nebula_Archivist.plr`
  - `Vortex_Curator.plr`
  - `Stardust_Keeper.plr`
  - `Solar_Courier.plr`
- Each paired character was saved and read back through TEdit's player loader with 20 valid inventory items.
- Final world SHA-256: `E375627D06E640508E32E49DCEF7D5230C6C148A5C4BF1861E296CCE14672F99`

### CurseForge Popular Map Import

- Added `external-sources/2026-05-15-curseforge-imports.md`.
- Downloaded and hashed 10 high-signal CurseForge map/source candidates across adventure, all-items/storage, arena, starter, and building/showcase categories.
- Public GitHub/LFS imports with source notices:
  - `Terraria_saves/imported/story-of-red-cloud/the-story-of-red-cloud.wld`
  - `Terraria_saves/imported/all-boss-battle-arenas/All Boss Battle Arenas Expert.wld`
  - `Terraria_saves/imported/compact-all-items-hub-master/SUNV-XTRA-All-ITEMS-HUB-1.4.5-Master.wld`
- Private-only local backups, not pushed because source pages showed All Rights Reserved:
  - Builder's Workshop
  - Ztorage Zystem
  - The Shimmer Lands
  - Khaiostomization
  - Scopey 1.4.5 All Items
  - Starter World 1.4.4.9 Master
  - The Kingdom

## 2026-05-18

### Adventure/Story Map Research

- Added `external-sources/2026-05-18-adventure-map-research.md`.
- Researched Terraria adventure maps across GitHub, CurseForge, and Terraria Community Forums for redistribution-compatible licenses.
- Finding: The adventure map ecosystem is dominated by Steam Workshop (not redistributable) and CurseForge maps with All Rights Reserved or unverifiable licenses.
- CurseForge individual pages returned HTTP 403, blocking license verification for most candidates (Skyblock Challenge, Ultirraria, World of Terra, etc.).
- Only one new PUBLIC-compatible adventure map file identified: The Story of Red Cloud Xelvaa Remix from GitHub.

### New Public Import

- Imported `Terraria_saves/imported/story-of-red-cloud-xelvaa-remix/the-story-of-red-cloud-xelvaa-remix.wld`
  - Source: https://github.com/timhjersted/tsorcDownload/blob/1.4.4/the-story-of-red-cloud-xelvaa-remix.wld
  - Author: Tim Hjersted (vibrent) / Xelvaa (remixer)
  - License basis: CurseForge Public Domain marking + GitHub README explicit remix permission + companion mod GPL-3.0
  - Size: 9,821,896 bytes
  - SHA-256: `3f6751970eed40c81772fe3f961c640975a32d4207b8d488c0a94b742655aaeb`
  - Note: Requires tsorcRevamp tModLoader mod for intended gameplay experience
  - THIRD_PARTY_NOTICE.md created alongside the file
