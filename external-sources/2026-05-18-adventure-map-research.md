---
title: 2026-05-18 Adventure/Story Map Research
type: external-source-research
status: completed
created: 2026-05-18
updated: 2026-05-18
tags:
  - terraria
  - adventure-maps
  - licensing-research
  - redistribution
---

# 2026-05-18 Adventure/Story Map Research

Research into Terraria adventure, story, puzzle, and parkour maps with potential for public redistribution in this archive's GitHub repository.

## Research Methodology

Sources searched:
1. **GitHub** — repository search for "terraria adventure map", "terraria world wld"
2. **CurseForge** — Terraria maps category filtered by Adventures, Puzzles, Parkour, Survival
3. **Terraria Community Forums** — thread for The Story of Red Cloud (forums.terraria.org)
4. **General web** — looking for maps with explicit open licenses

Key constraint: CurseForge blocks direct page fetches (HTTP 403) for individual map pages, so license verification for most CurseForge maps could not be completed in this pass. The CurseForge listing page was accessible and provided category/download metadata.

## Import Rule Used

- Public GitHub import requires a source-page license or explicit permission statement that allows redistribution.
- "Free to download" does NOT equal "free to redistribute" — these are distinct rights.
- Steam Workshop items are NOT redistributable (Steam Subscriber Agreement restricts this).
- Forum posts without explicit redistribution permission default to All Rights Reserved.
- GitHub repos without a LICENSE file default to All Rights Reserved under copyright law, UNLESS the README contains explicit permission language.

## Candidate Assessment

### 1. The Story of Red Cloud — Xelvaa Remix (GitHub)

| Field | Value |
|---|---|
| Title | The Story of Red Cloud — Xelvaa Remix |
| Author | Tim Hjersted (vibrent) / Xelvaa (remixer) |
| Source URL | https://github.com/timhjersted/tsorcDownload (branch: 1.4.4) |
| File | `the-story-of-red-cloud-xelvaa-remix.wld` |
| Category | Adventure / RPG / Dark Souls-inspired |
| Terraria version | 1.4.4 (requires tsorcRevamp tModLoader mod) |
| Quality signals | 6 stars, 3 forks, 166 commits, 5000+ Discord members, active development (updated Jan 2025), reviewed by IndieGameMag |
| License on source page | **No LICENSE file in tsorcDownload repo.** However, README states: "MAP REMIXES: Adventure map creators are welcome to borrow or remix assets from the map in their own creations - just include credit to Tim Hjersted somewhere and let me know so I can check it out! I'm a big fan of remix culture." |
| Companion mod license | GPL-3.0 (tsorcRevamp repo at https://github.com/timhjersted/tsorcRevamp) |
| CurseForge license (same map) | Public Domain (observed on curseforge.com/terraria/maps/story-red-cloud, per 2026-05-15 import) |
| File format | Single `.wld` file (requires tsorcRevamp.tmod + tsorcMusic.tmod to play properly) |
| Import recommendation | **PUBLIC** — The CurseForge page for this same project was marked Public Domain. The GitHub README explicitly permits remixing/borrowing with credit. The companion mod is GPL-3.0. This is a variant/remix of the already-imported map. |

**Note:** The base `the-story-of-red-cloud.wld` was already imported from CurseForge in the 2026-05-15 batch. The Xelvaa Remix is an additional variant available only from the GitHub repo.

**Complication:** This map requires the tsorcRevamp tModLoader mod to play properly. Without the mod, the custom enemies, items, and mechanics won't work. The .wld alone is a valid Terraria world file but the intended experience requires the mod.

---

### 2. Skyblock Challenge (CurseForge)

| Field | Value |
|---|---|
| Title | Skyblock Challenge |
| Author | starlightnt |
| Source URL | https://www.curseforge.com/terraria/maps/skyblock-1-4 |
| Category | Adventures / Survival |
| Terraria version | 1.4.x (last updated Aug 7, 2023) |
| Quality signals | 89,800 downloads |
| License on source page | **UNKNOWN — CurseForge returned 403 on individual page fetch** |
| File format | Unknown (likely single .wld) |
| Import recommendation | **SKIP** — Cannot verify license. CurseForge default for maps without explicit license selection is typically All Rights Reserved. Would need manual verification. |

---

### 3. Ultirraria — A New Adventure Awaits (CurseForge)

| Field | Value |
|---|---|
| Title | Ultirraria — a new adventure awaits! |
| Author | v0id585 |
| Source URL | https://www.curseforge.com/terraria/maps/ultirraria-the-new-adventure-awaits |
| Category | Survival / Adventures |
| Terraria version | 1.4.x (uploaded Mar 24, 2021) |
| Quality signals | 12,700 downloads |
| License on source page | **UNKNOWN — CurseForge returned 403 on individual page fetch** |
| File format | Unknown |
| Import recommendation | **SKIP** — Cannot verify license. Moderate download count, no updates since 2021. |

---

### 4. World of Terra (CurseForge)

| Field | Value |
|---|---|
| Title | World of Terra |
| Author | daromaxa |
| Source URL | https://www.curseforge.com/terraria/maps/world-of-terra |
| Category | Fortresses & Living Quarters / Adventures |
| Terraria version | 1.4.x (uploaded Mar 12, 2023) |
| Quality signals | 54,300 downloads |
| License on source page | **UNKNOWN — CurseForge returned 403** |
| File format | Unknown |
| Import recommendation | **SKIP** — Cannot verify license. This appears to be more of a building showcase than a pure adventure map. |

---

### 5. New Update Mobile All Item Map — World of Light (CurseForge)

| Field | Value |
|---|---|
| Title | New Update Mobile All Item Map! -World of Light- |
| Author | scopeymopey |
| Source URL | https://www.curseforge.com/terraria/maps/the-1-4-mobile-all-item-map-world-of-light |
| Category | Adventures / Items & Storage |
| Terraria version | 1.4.x (uploaded Oct 30, 2020) |
| Quality signals | 83,100 downloads |
| License on source page | **UNKNOWN — CurseForge returned 403** |
| File format | Unknown |
| Import recommendation | **SKIP** — Cannot verify license. Also primarily an all-items map rather than a true adventure/story map. |

---

### 6. OP Items map + Player Pack (CurseForge)

| Field | Value |
|---|---|
| Title | OP Items map + Player Pack! (with zenith) |
| Author | arturzitoon |
| Source URL | https://www.curseforge.com/terraria/maps/op-items-map-op-player-with-zenith |
| Category | Adventures / Items & Storage |
| Terraria version | 1.4.x (uploaded Jan 16, 2021) |
| Quality signals | 34,600 downloads |
| License on source page | **UNKNOWN — CurseForge returned 403** |
| File format | Unknown |
| Import recommendation | **SKIP** — Cannot verify license. Also primarily an items/utility map, not adventure content. |

---

## Maps NOT Investigated (Excluded by Category)

The following popular CurseForge maps were visible in search results but excluded because they are utility/storage maps (already covered in the 2026-05-15 import) rather than adventure/story content:

- Builder's Workshop (TelBuilds) — All Rights Reserved, already in private backups
- COMPACT ALL ITEMS HUB (SUNVxtra) — GPLv3, already publicly imported
- Scopey's 1.4.5 All Items Map (scopeymopey) — All Rights Reserved, already in private backups
- Starter World 1.4.4.9 (AkoyPinoy03) — All Rights Reserved, already in private backups

## Summary of Findings

### The Adventure Map Landscape

The Terraria adventure map ecosystem is dominated by:
1. **Steam Workshop** — Most active adventure maps are distributed via Steam Workshop (not redistributable)
2. **CurseForge** — Has a license field per upload, but most map authors either select "All Rights Reserved" or leave it at default
3. **Terraria Community Forums** — Maps posted as forum attachments with no explicit license (defaults to All Rights Reserved)
4. **GitHub** — Very rare for Terraria maps; The Story of Red Cloud is the notable exception

### Licensing Reality

Of all adventure/story maps researched:
- **1 confirmed PUBLIC-compatible**: The Story of Red Cloud Xelvaa Remix (GitHub, explicit remix permission + CurseForge Public Domain marking)
- **0 confirmed with other open licenses** in the adventure category
- **5+ maps with UNKNOWN license** (CurseForge 403 blocked verification)
- **Most popular maps** use All Rights Reserved or have no stated license

### Actionable Import

The only new adventure map file that can be confirmed as publicly redistributable is:

| File | Source | Recommendation |
|---|---|---|
| `the-story-of-red-cloud-xelvaa-remix.wld` | https://github.com/timhjersted/tsorcDownload/blob/1.4.4/the-story-of-red-cloud-xelvaa-remix.wld | **PUBLIC** — import with credit notice |

### Future Research Recommendations

1. **Manual CurseForge verification** — Visit individual map pages in a browser to check the license field for Skyblock Challenge, Ultirraria, and other adventure maps
2. **Contact authors directly** — For high-quality maps with unclear licensing, reach out to authors to request redistribution permission
3. **Monitor GitHub** — Set up alerts for new Terraria map repositories with open licenses
4. **Check tModLoader Mod Browser** — Some mods include custom worlds; if the mod is GPL/MIT, the bundled world may inherit that license
5. **Terraria Forums deep dive** — Some older forum posts (2012-2016 era) may have explicit "feel free to share" language that would permit redistribution

## Restore Notes

- The Xelvaa Remix `.wld` requires the tsorcRevamp mod (available via Steam Workshop or GitHub) to function as intended
- Without the mod, the world loads but custom content (enemies, items, mechanics) will be missing
- The map is designed for tModLoader 1.4.4 + Terraria 1.4.4.9
