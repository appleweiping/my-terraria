# Boss Rush Colosseum

## Overview

A purpose-built Master Mode combat world with optimized arenas for every Terraria boss and invasion event. Each arena is specifically engineered for its target encounter with correct dimensions, platform layouts, buff stations, and pre-stocked summon items. Includes full class loadout rooms and 5 paired characters (one per class + utility).

## Scope

- **24 arenas** covering all bosses and major events
- **4 arena sections**: Pre-Hardmode, Hardmode, Endgame, Events
- **Central hub** with trophy hall, buff stations, and class loadout rooms
- **Full teleporter network** connecting all arenas
- **7 NPCs** strategically housed for combat support
- **5 paired characters**: Melee Champion, Ranger Ace, Mage Supreme, Summoner Lord, Arena Master
- **World size**: Large, Master Mode, post-Moon Lord

## Status

| Phase | Status |
|-------|--------|
| Design document | ✅ Complete |
| Acceptance checklist | ✅ Complete (90/90) |
| World construction | ✅ Complete |
| Character creation | ✅ Complete (5 characters) |
| Testing/QA | ✅ Complete |

## File Structure

```
originals/boss-rush-colosseum/
  Boss Rush Colosseum.wld   — World file (Git LFS)
  Boss Rush Colosseum.meta.json — Metadata sidecar
  Melee Champion.plr        — Paired character (Git LFS)
  Ranger Ace.plr            — Paired character (Git LFS)
  Mage Supreme.plr          — Paired character (Git LFS)
  Summoner Lord.plr         — Paired character (Git LFS)
  Arena Master.plr          — Paired character (Git LFS)
  design.md                 — Full design specification
  acceptance-checklist.md   — 90-point verification checklist
  README.md                 — This file
```

## Restore Instructions

1. Build the world using the design document as specification
2. World must be progressed to post-Moon Lord state (or flags set via builder tool)
3. Artificial biomes must be created for biome-specific bosses (Crimson, Jungle underground, Hallow, Snow, Ocean)
4. Follow the recommended build order in Technical Notes
5. Verify against the acceptance checklist (all 90 points)
6. Create all 5 paired characters with specified loadouts
7. Place world file (.wld) and player files (.plr) in Terraria save directory:
   - World: `Documents/My Games/Terraria/Worlds/`
   - Players: `Documents/My Games/Terraria/Players/`

## Dependencies

- Terraria version 1.4.4+ (for all bosses including Deerclops, Queen Slime, Empress)
- No mods required — all vanilla content
- World must support Master Mode difficulty
- Builder tool needs ability to set world progression flags (Hardmode, post-Plantera, post-Golem, post-Moon Lord)
