# Starter Academy

## Overview

Starter Academy is an original training-world project for onboarding a new Terraria player without turning the save into a generic all-items warehouse. Its purpose is to teach progression, safety habits, crafting, exploration, and early-to-mid-game combat through a curated world and three paired characters.

## Scope

- Tutorial hub for the first several hours of play
- Guided rooms for movement, mining, crafting, housing, fishing, potion setup, and basic wiring
- Combat practice lanes for early bosses and event preparation
- Progression vaults that unlock conceptually by game stage rather than dumping every item at spawn
- Three paired characters: Fresh Start, Mid-Game Guide, and Mentor
- Vanilla-compatible `.wld` + `.plr` files already present in this project directory

## Status

| Phase | Status |
|-------|--------|
| World file | Present |
| Paired characters | Present |
| Design document | Reconstructed |
| Acceptance checklist | Reconstructed |
| QA readback | Pending |
| In-game walkthrough | Pending |

## File Structure

```
originals/starter-academy/
  Starter Academy.wld       — Training world save
  Fresh Start.plr           — Beginner baseline character
  Mid-Game Guide.plr        — Mid-progression reference character
  Mentor.plr                — Teaching / demonstration character
  design.md                 — Reconstructed design specification
  acceptance-checklist.md   — QA checklist for future verification
  README.md                 — This file
```

## Restore Instructions

1. Copy `Starter Academy.wld` into `Documents/My Games/Terraria/Worlds/`.
2. Copy the three `.plr` files into `Documents/My Games/Terraria/Players/`.
3. Open the world first with `Fresh Start.plr` to validate the beginner path.
4. Use `Mid-Game Guide.plr` and `Mentor.plr` to inspect later-stage rooms and teaching examples.
5. Record QA findings in `acceptance-checklist.md` before claiming the project complete.

## Notes

- These documents were reconstructed after the save files already existed, so the next version should prioritize world readback and in-game screenshot validation.
- Do not present Starter Academy as fully QA-complete until the checklist is verified against the actual `.wld` contents.
