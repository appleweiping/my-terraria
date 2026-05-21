# Starter Academy Acceptance Checklist

This checklist is intentionally strict because original projects must not be treated as toy/demo saves. Mark items only after verifying the actual `.wld` or `.plr` files, preferably with both metadata readback and an in-game walkthrough.

## World Integrity

- [ ] `Starter Academy.wld` exists and is tracked through Git LFS.
- [ ] World opens in vanilla Terraria 1.4.4+ without crashing.
- [ ] Spawn point is safe, enclosed or clearly protected, and has basic navigation signage.
- [ ] No required tutorial route depends on private mods or untracked files.
- [ ] Restore instructions in `README.md` are accurate.

## Spawn Hub

- [ ] Hub has a bed/spawn setup or clearly explains the intended spawn behavior.
- [ ] Hub includes labeled access to each academy section.
- [ ] Starter chest contents are useful but not all-items-map excessive.
- [ ] Crafting basics are visible near the hub.
- [ ] Signs explain the recommended first route for `Fresh Start.plr`.

## Tutorial Sections

- [ ] Movement/safety section teaches fall damage, platforms, ropes, and basic hazard recovery.
- [ ] Mining/crafting section shows early ore and crafting-station progression.
- [ ] Housing/NPC section contains at least one valid example and one failure-mode explanation.
- [ ] Combat section supports safe practice with at least one early-boss-style arena.
- [ ] Exploration/biome section explains hazards and resource goals.
- [ ] Mid-game transition section explains hardmode preparation and storage upgrades.

## Paired Characters

- [ ] `Fresh Start.plr` loads and has beginner-appropriate gear.
- [ ] `Mid-Game Guide.plr` loads and has mid-progression reference gear.
- [ ] `Mentor.plr` loads and has teaching/recovery tools without trivializing the beginner path.
- [ ] Character names and roles are documented in `README.md` and `design.md`.

## Documentation

- [x] `README.md` exists.
- [x] `design.md` exists.
- [x] `acceptance-checklist.md` exists.
- [ ] In-world signage is verified against the design document.
- [ ] Screenshots or map renders are captured for catalog/display use.
- [ ] Any deviations from the reconstructed design are recorded here.

## Catalog Readiness

- [ ] `python tools/build_catalog.py` includes Starter Academy in `inventory/CATALOG.md`.
- [ ] `python tools/build_catalog.py --check` passes after catalog generation.
- [ ] `inventory/catalog.json` reflects the world/player counts for this project.
- [ ] README status is updated from reconstructed/pending to verified after QA.

## Final Status

Current status: **documentation reconstructed; QA pending**.

Do not mark Starter Academy as complete until every unchecked item above has been verified.
