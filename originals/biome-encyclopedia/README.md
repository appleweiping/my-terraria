# Biome Encyclopedia

**Original Project #2** in the Terraria Save Archive (`D:\Terraria_doc`)

---

## Overview

A single Large Master-mode world containing artificially constructed versions of every vanilla Terraria 1.4.x biome. Each biome is built in a standardized section with labeled signs, item displays, NPC housing, and mechanics explanations. A central teleporter hub connects all 30 biome sections.

This is an educational/reference world — not a storage vault (that's Project #1, Astral Forge Vault).

## Contents

| File | Purpose |
|------|---------|
| `Biome Encyclopedia.wld` | World file — 11 MB, 8400×2400, 599 chests, 200 signs |
| `Biome Scholar.plr` | Journey mode exploration character |
| `Biome Warden.plr` | Master mode combat validation character |
| `Biome Encyclopedia.meta.json` | Metadata sidecar |
| `design.md` | Full technical design document |
| `acceptance-checklist.md` | Completion criteria (~266 checkpoints) |
| `README.md` | This file |

## Paired Characters

| Character | Mode | Role |
|-----------|------|------|
| Biome Scholar | Journey | Exploration, observation, research duplication |
| Biome Warden | Master | Spawn testing, combat validation, drop verification |

## Current Status

**Phase**: Complete ✅

- [x] Design document written
- [x] Acceptance checklist defined
- [x] World generated (11 MB, 8400×2400)
- [x] All 30 biome sections constructed
- [x] Central hub with 30-pad teleporter network
- [x] 599 chests stocked with biome drops and reference blocks
- [x] 200 signs with biome mechanics explanations
- [x] Characters created and equipped (Biome Scholar + Biome Warden)

## Restore Instructions

Once world and character files exist:

1. Copy the `.wld` file to:
   ```
   Documents\My Games\Terraria\Worlds\
   ```

2. Copy both `.plr` files (+ `.plr.bak`) to:
   ```
   Documents\My Games\Terraria\Players\
   ```

3. Launch Terraria 1.4.4.9 (vanilla, no mods)

4. Select either character and load the Biome Encyclopedia world

5. Use the teleporter hub at spawn to navigate to any biome section

## Relationship to Archive

```
D:\Terraria_doc\
├── originals\
│   ├── astral-forge-vault\    ← Project #1: Storage/archive hub
│   └── biome-encyclopedia\    ← Project #2: This project
└── saves\
    └── biome-encyclopedia\    ← World + character files (when created)
```

## Key Design Decisions

- **150% block count targets**: Every section exceeds minimum biome detection threshold by 50% for reliability
- **200-tile section width**: Exceeds the 170-tile scan rectangle, ensuring biome triggers regardless of player position within section
- **Non-corruptible barriers**: Wood/ash walls between sections prevent biome spread
- **Natural dungeon preserved**: Dungeon section built around world-gen dungeon (required for natural walls)
- **Ocean at world edges**: Cannot be relocated (position-based detection)

## Version

- Terraria: 1.4.4.9 (vanilla)
- World size: Large (8400 × 2400)
- Difficulty: Master
