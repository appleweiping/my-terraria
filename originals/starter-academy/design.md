# Starter Academy Design

## Thesis

Starter Academy should make Terraria less opaque for a new or returning player by teaching practical progression in the world itself. It is not an all-items map. It is a guided training environment that preserves discovery while removing the most frustrating early-game uncertainty.

## Audience

- New players who need a safe world for learning core systems
- Returning players who want a quick refresher on crafting, NPC housing, boss preparation, and exploration patterns
- Archive users who want an original utility world distinct from all-item hubs and boss arenas

## Design Principles

1. **Teach by doing**: every room should demonstrate an action the player can repeat elsewhere.
2. **Avoid item dumping**: provide staged kits and examples, not every possible item.
3. **Keep vanilla compatibility**: no mods, no external dependency, no private assets.
4. **Make recovery easy**: clear spawn hub, safe storage, and obvious routing back to tutorial sections.
5. **Document inside and outside the save**: signs in-world plus this repository documentation.

## World Layout

### Spawn Hub

- Safe spawn room with bed, guide signs, starter storage, crafting basics, and exit routes.
- Labeled teleport or path network to each academy section.
- Starter chest should contain low-risk basics only: torches, rope, recall/magic mirror equivalent, basic potions, and simple tools.

### Section 1: Movement and Safety

- Platforming lane for jump height, fall damage, ropes, grappling, and safe descent.
- Trap demonstration corridor with visible wiring and reset instructions.
- Lava/water/honey safety examples with warning signs.

### Section 2: Mining and Crafting

- Ore progression display from early to mid-game.
- Crafting station gallery: work bench, furnace, anvil, loom, sawmill, bottle, cooking pot, tinkerer station.
- Example recipes grouped by purpose: tools, armor, mobility, potions, building.

### Section 3: Housing and NPCs

- Valid starter housing templates.
- Invalid housing examples with signs explaining why they fail.
- Pylon / biome placement notes where compatible with the target version.

### Section 4: Combat Basics

- Early boss practice lane for King Slime / Eye of Cthulhu style movement.
- Buff station with constrained potion set.
- Weapon style mini-gallery: melee, ranged, magic, summoner.

### Section 5: Exploration and Biomes

- Safe tunnels to surface, underground, desert/snow/jungle analog areas where present.
- Signposts explaining biome hazards and useful resources.
- Fishing pond examples with crates/bait notes.

### Section 6: Mid-Game Transition

- Hardmode preparation checklist area.
- Contained demo of altars, evil biome spread warning, arena preparation, and storage upgrades.
- Mid-game reference storage for the `Mid-Game Guide` character.

## Paired Characters

| Character | Role | Expected Use |
|---|---|---|
| Fresh Start | Beginner baseline | Walk the academy from spawn with minimal assumptions |
| Mid-Game Guide | Mid-progression reference | Demonstrate post-basic gear, crafting, and boss prep |
| Mentor | Teaching / admin | Inspect sections, demonstrate mechanics, recover from mistakes |

## Completion Bar

Starter Academy is complete only when:

- The world loads in vanilla Terraria.
- Spawn hub and all academy sections are reachable.
- Signage explains what to do without requiring this README.
- Paired characters load and have role-appropriate gear.
- Acceptance checklist is verified against the actual world and players.
- At least one visual documentation pass exists in `docs/` or future catalog assets.

## Known Gaps for Next QA Pass

- Read back world metadata from the `.wld` file and confirm section/chest/sign counts.
- Launch in Terraria and walk the full Fresh Start route.
- Capture screenshots for catalog display.
- Update this design if the actual saved world differs from the reconstructed plan.
