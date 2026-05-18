# Wiring Masterclass

## Overview

A comprehensive educational Terraria world that teaches the complete wiring and logic system — from basic switches through logic gates, practical machines, pixel displays, hoik exploits, and fully automated systems. Designed as an interactive reference library where every concept is demonstrated with working examples and clear sign-based explanations.

## Scope

- **6 sections** covering all wiring topics from beginner to advanced
- **60+ individual demonstrations**, each self-contained and resettable
- **Central hub** with color-coded teleporter network
- **6 NPCs** (Mechanic, Steampunker, Cyborg, Goblin Tinkerer, Wizard, Nurse)
- **2 paired characters**: Wire Wizard (tools) and Trap Master (combat/traps)
- **World size**: Large, Journey Mode

## Status

| Phase | Status |
|-------|--------|
| Design document | Complete |
| Acceptance checklist | Complete |
| World construction | Not started |
| Character creation | Not started |
| Testing/QA | Not started |

## File Structure

```
originals/wiring-masterclass/
  design.md                 — Full design specification
  acceptance-checklist.md   — 80-point verification checklist
  README.md                 — This file
```

## Restore Instructions

1. Build the world using the design document as specification
2. Follow the recommended build order in the Technical Notes section
3. Verify against the acceptance checklist (all 80 points)
4. Create both paired characters with specified loadouts
5. Place world file (.wld) and player files (.plr) in Terraria save directory:
   - World: `Documents/My Games/Terraria/Worlds/`
   - Players: `Documents/My Games/Terraria/Players/`

## Dependencies

- Terraria version 1.4.4+ (for all wiring components and Journey Mode)
- No mods required — all vanilla mechanics
- Builder tool needs access to all item IDs for chest stocking and character inventory
