# 2026-05-15 External Terraria Save Source Scan

## Goal

Find high-quality external Terraria saves that could expand this archive beyond the user's existing all-item maps, class characters, farms, buildings, and local backups.

## Findings

### GitHub

GitHub contains some Terraria save repositories, but the strongest search results were generally small, unlicensed, personal backup repos rather than high-reputation curated save releases.

Representative examples found by GitHub API search:

| Repository | Signal | License | Import decision |
|---|---:|---|---|
| `Healixzero/Terraria_Saves` | 1 star; old personal character/world saves | none | Do not import without permission. Low quality signal. |
| `Dylanfg123/Terraria` | 0 stars; one world save | none | Do not import without permission. Low quality signal. |
| `Tiryth/Terraria` | 0 stars; players plus one world | none | Do not import without permission. Low quality signal. |
| `mbarila/Worlds` | 0 stars; world backups / tModLoader files | none | Do not import without permission. Low quality signal. |
| `Terrariaslime/chinese-terraria-map` | 0 stars; tModLoader/chinese item map | none | Do not import without permission. Niche/modded. |
| `lazington/TMM-Playthrough` | 0 stars; playthrough world snapshots | none | Do not import without permission. Personal playthrough. |

### CurseForge And Community Distribution

CurseForge appears to be a stronger source surface for high-quality Terraria maps than GitHub. It has map categories, download counts, update dates, and install instructions.

High-signal examples:

| Source | Public signal | Why it matters | Import decision |
|---|---:|---|---|
| The Story of Red Cloud | about 194K downloads; long-running adventure map/mod; 18 dungeons; 20-30+ hour playthrough | Distinct from this archive because it is a full adventure/RPG-style map, not an all-item or backup set. | Candidate only until redistribution terms are confirmed. |
| CurseForge Terraria Maps index | shows high-download map categories including all-item/storage, adventures, multiplayer, arenas, and survival maps | Good discovery surface for future imports. | Use for candidate discovery and provenance. |
| Ztorage_Zystem / all-items style maps | listed around 339K downloads in CurseForge search result | Strong all-item/storage-map signal; likely overlaps with current archive but may be more systematic. | Candidate only until license/permission is confirmed. |

## Import Protocol

For each candidate:

1. Record source URL, author, project title, version, update date, download count, and required game/mod version.
2. Check whether redistribution into this public GitHub repo is allowed.
3. If redistribution is unclear, do not commit the binary files. Keep an install note instead.
4. If redistribution is allowed, import the complete save set under `Terraria_saves/imported/<source-slug>/` or merge into `Players` / `Worlds` only when names are collision-safe.
5. Update `inventory/` with source, hashes, file roles, and restore notes.
6. Commit by source, not as one giant mixed batch.

## Current Decision

No third-party binary save was imported in this pass because the visible high-signal candidates require explicit license/permission review. The repository now records the protocol so future agents do not copy unlicensed save files casually.

## Source URLs

- https://www.curseforge.com/terraria/maps
- https://www.curseforge.com/terraria/maps/story-red-cloud
- https://terraria.wiki.gg/wiki/Command-line_parameters
- https://terraria.wiki.gg/wiki/Guide:Setting_up_a_Terraria_server

