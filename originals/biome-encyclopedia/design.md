# Biome Encyclopedia — Design Document

**Project**: Biome Encyclopedia  
**Type**: Original world (educational/reference)  
**Version**: Terraria 1.4.4.9 (vanilla)  
**Difficulty**: Master  
**World Size**: Large (8400 × 2400 tiles)  
**Seed**: TBD (generated fresh, then terraformed)  
**Last Updated**: 2026-05-18

---

## 1. Concept

A single large world artificially constructed to contain every vanilla Terraria biome in a standardized, visitable format. The world functions as a living encyclopedia — a player teleports to any biome section and finds:

- The biome's defining blocks and walls placed at or above detection thresholds
- Native enemy spawns (via natural spawn conditions or statues where available)
- Native NPCs housed within the section (respecting happiness preferences)
- Key drops and crafting materials displayed in labeled chests
- Wiring demonstrations relevant to that biome (traps, teleporters, actuators)
- Signs explaining biome mechanics (spawn requirements, depth layers, size thresholds)

This is distinct from the Astral Forge Vault (project #1), which is a storage/archive hub. The Biome Encyclopedia is a reference tool — you visit it to understand how biomes work, not to store items.

---

## 2. Biome Registry

### 2.1 Surface Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 1 | Forest (Purity) | Standard grass, trees | Default (no other biome overrides) | Surface/Space layer |
| 2 | Desert | Sand, Hardened Sand, Sandstone | 1500 tiles | Surface layer |
| 3 | Snow/Ice | Snow Block, Ice Block | 1500 tiles | Surface layer |
| 4 | Jungle | Jungle Grass, Lihzahrd Brick (counts) | 140 tiles (surface jungle) | Surface layer |
| 5 | Ocean | Water volume at world edge | Within 250 tiles of world edge + below surface, 1000+ water tiles | Surface layer |
| 6 | Glowing Mushroom (Surface) | Mushroom Grass | 100 tiles | Surface layer |

### 2.2 Underground Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 7 | Cavern | Stone, default | Default underground | Below Underground layer (cavern depth) |
| 8 | Underground Desert | Hardened Sand, Sandstone | 1500 tiles | Below surface layer |
| 9 | Underground Snow/Ice | Ice Block, Snow Block | 1500 tiles | Below surface layer |
| 10 | Underground Jungle | Jungle Grass, Mud | 140 tiles | Below surface layer |
| 11 | Underground Mushroom | Mushroom Grass | 100 tiles | Below surface layer |

### 2.3 Evil Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 12 | Corruption (Surface) | Corrupt Grass, Ebonstone, Purple Ice, Ebonsand | 200 tiles (surface evil) | Surface layer |
| 13 | Corruption (Underground) | Ebonstone, Corrupt Grass | 200 tiles | Below surface layer |
| 14 | Crimson (Surface) | Crimson Grass, Crimstone, Red Ice, Crimsand | 200 tiles (surface evil) | Surface layer |
| 15 | Crimson (Underground) | Crimstone, Crimson Grass | 200 tiles | Below surface layer |

### 2.4 Hardmode Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 16 | Hallow (Surface) | Hallowed Grass, Pearlstone, Pearlsand, Pink Ice | 125 tiles | Surface layer |
| 17 | Hallow (Underground) | Pearlstone, Hallowed Grass, Pink Ice | 125 tiles | Below surface layer |

### 2.5 Special/Mini Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 18 | Dungeon | Dungeon Brick (any color) | 250 tiles | Below surface layer |
| 19 | Lihzahrd Temple | Lihzahrd Brick | 250 tiles | Below surface layer |
| 20 | Meteorite | Meteorite ore | 75 tiles | Any |
| 21 | Spider Nest | Spider Wall (background) | 200 spider wall tiles | Below surface layer |
| 22 | Granite Cave | Granite Block, Granite Wall | 150 tiles | Below surface layer |
| 23 | Marble Cave | Marble Block, Marble Wall | 150 tiles | Below surface layer |
| 24 | Bee Hive | Hive Block, Honey Block | 200 tiles | Below surface layer |

### 2.6 Sky Biomes

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 25 | Space | N/A (height-based) | Above Space layer (~above y=360 in large world) | Space layer |
| 26 | Floating Island | Rain Cloud, Disc Wall, Sunplate | N/A (structural) | Space layer |

### 2.7 Underworld

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 27 | Underworld/Hell | Ash Block, Hellstone | Below Underworld layer (last ~200 tiles) | Underworld layer |

### 2.8 Event/Conditional Zones

| # | Biome | Defining Blocks | Detection Threshold | Depth Requirement |
|---|-------|----------------|---------------------|-------------------|
| 28 | Graveyard | Tombstones | 5+ tombstones within 36-tile radius of NPC | Any |
| 29 | Shimmer | Shimmer liquid | Aether biome (present in world gen near Jungle in 1.4.4+) | Below surface layer |
| 30 | Purity (Reference) | Standard blocks, no biome override | Absence of other biome thresholds | Surface layer |

---

## 3. Layout Plan

### 3.1 World Structure

```
← WEST                                                                    EAST →
[Ocean][Snow][Forest][SPAWN/HUB][Desert][Jungle][Ocean]   ← Natural gen (overwritten)

ACTUAL LAYOUT (post-terraforming):
|-----|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|-----|-----|
|Ocean|Snow |Mush |Forst| HUB |Desrt |Jungl|Corr |Crmsn|Hallow|Dung |Templ|Ocean|
|  S  | S/U | S/U | S  |SPAWN| S/U  | S/U | S/U | S/U | S/U  | U   | U   |  S  |
|-----|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|-----|-----|

UNDERGROUND STRIP (below main sections):
|Spider|Granite|Marble|BeeHive|Meteor|Cavern|UgMush|Shimmer|Graveyard|
```

### 3.2 Section Dimensions

- **Standard surface section**: 200 tiles wide × surface-to-cavern depth (~400 tiles)
- **Standard underground section**: 200 tiles wide × cavern-to-hell depth (~600 tiles)
- **Mini-biome sections**: 100 tiles wide × 150 tiles tall (Spider, Granite, Marble, Bee Hive)
- **Central Hub**: 300 tiles wide × 200 tiles tall
- **Underworld**: Full world width (repurposed natural hell layer, segmented with labels)
- **Space**: Full world width at top (natural, with constructed floating islands)

### 3.3 Horizontal Arrangement (Left to Right)

Position is measured from world left edge (tile 0):

| Position (tiles) | Section | Width |
|-------------------|---------|-------|
| 0–250 | West Ocean | 250 |
| 250–450 | Snow/Ice (Surface + Underground) | 200 |
| 450–650 | Glowing Mushroom (Surface + Underground) | 200 |
| 650–850 | Forest/Purity (Reference) | 200 |
| 850–1050 | **Corruption (Surface + Underground)** | 200 |
| 1050–1250 | **Crimson (Surface + Underground)** | 200 |
| 1250–1550 | **CENTRAL HUB (Spawn)** | 300 |
| 1550–1750 | Desert (Surface + Underground) | 200 |
| 1750–1950 | Jungle (Surface + Underground) | 200 |
| 1950–2150 | **Hallow (Surface + Underground)** | 200 |
| 2150–2350 | Dungeon | 200 |
| 2350–2550 | Lihzahrd Temple | 200 |
| 2550–2750 | Special Mini-Biomes Strip | 200 |
| 2750–3000 | East Ocean | 250 |

**Note**: Large world is 8400 tiles wide. The above uses ~3000 tiles. Remaining space (3000–8400) is reserved for:
- Expanded sections if 200 tiles proves insufficient
- Isolation buffers (empty space preventing biome bleed)
- Future additions

### 3.4 Vertical Layers (Large World)

| Layer | Y-Range (approx.) | Contents |
|-------|-------------------|----------|
| Space | 0–360 | Floating Islands, Space section |
| Surface | 360–800 | Surface biome sections |
| Underground | 800–1200 | Transition zone |
| Cavern | 1200–2000 | Underground biome sections |
| Underworld | 2000–2400 | Hell section |

### 3.5 Isolation Strategy

Biomes bleed into each other if sections are adjacent without buffers. Mitigation:

- **3-tile-wide vertical shafts** of non-counting blocks (wood, platforms) between every section
- Evil biomes contained with **Sunflower rows** at surface boundaries
- Underground evil/hallow contained with **non-corruptible blocks** (wood, ash) as barriers
- Each section slightly over-built on block counts to tolerate minor corruption spread

---

## 4. Central Hub Design

### 4.1 Structure

- Located at world spawn (center)
- 300 tiles wide, 200 tiles tall
- Built from non-biome blocks (Gray Brick, Wood, Glass)
- Multi-floor building with:
  - **Ground floor**: Spawn point, main teleporter array
  - **Floor 2**: Master chest index (signs listing what's in each section)
  - **Floor 3**: NPC overflow housing (NPCs that don't fit biome sections)
  - **Roof**: Secondary teleporter array for sky/hell destinations

### 4.2 Teleporter Network

- **30 teleporter pads** in the hub (one per biome section)
- Each pad labeled with a sign (biome name + section number)
- Color-coded wiring:
  - Red wire: Surface biomes
  - Blue wire: Underground biomes
  - Green wire: Special biomes
  - Yellow wire: Event zones
- Each destination has a **return pad** wired back to hub
- Lever-activated (not pressure plate) to prevent accidental teleportation
- Wire length managed with **Teleporter + Wire** (max wire length is unlimited but performance matters — keep runs clean)

### 4.3 Hub Amenities

- All crafting stations (duplicate set from Astral Forge Vault)
- Nurse + Dryad housed in hub for healing/status check
- Pylon collection (one of each type for fast-travel backup)
- Bed (spawn point set)
- Storage: 10 chests with building materials, wiring supplies, spare teleporters

---

## 5. Section Template

Every biome section follows this standardized layout:

```
┌─────────────────────────────────────────────┐
│  ENTRANCE SIGN (Biome Name + Key Facts)     │
│  ┌─────────┐                                │
│  │Teleporter│ ← Return pad to hub           │
│  │   Pad    │                                │
│  └─────────┘                                │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  NPC HOUSING (2-4 rooms)             │   │
│  │  - Biome-preferred NPCs              │   │
│  │  - Valid housing (table+chair+light)  │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  DISPLAY AREA                         │   │
│  │  - Item Frames with key items         │   │
│  │  - Weapon Racks with biome weapons    │   │
│  │  - Mannequins with biome armor sets   │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  CHEST ARRAY (4-8 chests)            │   │
│  │  - Chest 1: Biome drops (common)     │   │
│  │  - Chest 2: Biome drops (rare)       │   │
│  │  - Chest 3: Crafting materials       │   │
│  │  - Chest 4: Furniture/blocks         │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  NATURAL ZONE (open area)            │   │
│  │  - Biome blocks at threshold count   │   │
│  │  - Natural terrain shape             │   │
│  │  - Mob spawning area (if applicable) │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  MECHANICS SIGNS (2-4 signs)         │   │
│  │  - Block count threshold             │   │
│  │  - Depth requirement                 │   │
│  │  - Special spawn conditions          │   │
│  │  - Music track that plays            │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │  WIRING DEMO (if applicable)         │   │
│  │  - Traps native to biome            │   │
│  │  - Statue spawners for biome mobs   │   │
│  │  - Actuated blocks for access       │   │
│  └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## 6. Technical Specifications

### 6.1 Biome Detection Mechanics

Terraria checks biome status based on tile counts within a **rectangular scan area** centered on the player:

- **Scan rectangle**: 170 tiles wide × 124 tiles tall (centered on player)
- The game counts specific tile types within this rectangle
- Whichever biome threshold is met (and has highest priority) determines the active biome
- **Priority order** (highest first): Meteorite > Dungeon > Corruption/Crimson > Hallow > Jungle > Mushroom > Snow > Desert > Ocean > Forest

### 6.2 Critical Block Counts (within scan area)

These are the **minimum tiles required** within the player's scan rectangle:

| Biome | Required Tile Count | Tile Types |
|-------|-------------------|------------|
| Corruption | 200 | Ebonstone, Corrupt Grass, Purple Ice, Ebonsand, Corrupt Hardened Sand, Corrupt Sandstone |
| Crimson | 200 | Crimstone, Crimson Grass, Red Ice, Crimsand, Crimson Hardened Sand, Crimson Sandstone |
| Hallow | 125 | Pearlstone, Hallowed Grass, Pink Ice, Pearlsand, Hallowed Hardened Sand, Hallowed Sandstone |
| Jungle | 140 | Jungle Grass, Lihzahrd Brick |
| Glowing Mushroom | 100 | Mushroom Grass |
| Snow | 1500 | Snow Block, Ice Block, Purple Ice, Red Ice, Pink Ice |
| Desert | 1500 | Sand, Ebonsand, Crimsand, Pearlsand, Hardened Sand, Sandstone (and corrupt/crimson/hallow variants) |
| Dungeon | 250 | Dungeon Brick (any color: Blue, Green, Pink) |
| Meteorite | 75 | Meteorite Ore |
| Graveyard | 5 | Tombstones (any type) within NPC scan radius |
| Ocean | N/A | Position-based: within 250 tiles of world edge + sufficient water |
| Space | N/A | Height-based: above Space layer |
| Underworld | N/A | Height-based: below Underworld layer |

### 6.3 Construction Targets

To ensure reliable biome detection with margin for error, each section will be built to **150% of minimum threshold**:

| Biome | Target Block Count |
|-------|-------------------|
| Corruption | 300 |
| Crimson | 300 |
| Hallow | 190 |
| Jungle | 210 |
| Glowing Mushroom | 150 |
| Snow | 2250 |
| Desert | 2250 |
| Dungeon | 375 |
| Meteorite | 115 |

### 6.4 Depth Layer Boundaries (Large World)

| Layer | Y Coordinate Range | Notes |
|-------|-------------------|-------|
| Space | 0 to Surface - 60 | ~y=0 to y=300 |
| Surface | varies by world gen | ~y=300 to y=440 |
| Underground | Surface to Cavern | ~y=440 to y=880 |
| Cavern | Underground to Hell | ~y=880 to y=2100 |
| Underworld | Last ~200 tiles | ~y=2100 to y=2400 |

**Important**: Underground biomes (Underground Jungle, Underground Snow, etc.) require the player to be below the Surface layer. Building these sections at the wrong depth will not trigger the biome.

### 6.5 NPC Housing Requirements

Each NPC room must have:
- At least 60 tiles of open space (interior)
- Minimum 10 tiles wide × 6 tiles tall (interior)
- A valid light source
- A valid flat-surface item (table, workbench, dresser)
- A valid comfort item (chair, throne, bench)
- Background walls (player-placed)
- No corruption/crimson within 45 tiles (for most NPCs)

### 6.6 NPC Biome Assignments (Happiness Optimization)

| Biome Section | NPCs Housed | Reason |
|---------------|-------------|--------|
| Forest | Guide, Zoologist, Golfer | Forest-loving NPCs |
| Snow | Mechanic, Cyborg, Santa Claus | Snow-preferred |
| Desert | Nurse, Arms Dealer, Steampunker | Desert-preferred |
| Jungle | Dryad, Painter, Witch Doctor | Jungle-preferred |
| Ocean | Angler, Pirate, Stylist | Ocean-preferred |
| Mushroom | Truffle | Requires Mushroom biome |
| Hallow | Wizard, Party Girl, Tax Collector | Hallow-preferred |
| Underground | Demolitionist, Goblin Tinkerer, Clothier | Underground-preferred |
| Dungeon | Clothier, Old Man (pre-Skeletron) | Thematic |
| Hub | Nurse, Merchant, Dryad (duplicates for utility) | Convenience |

### 6.7 Wiring Specifications

**Teleporter Network**:
- 30 teleporter pads in hub + 30 destination pads = 60 total
- Each pair connected by dedicated wire color where possible
- With only 4 wire colors available, use **junction boxes** and **logic gates** to multiplex
- Alternative: Use **lever + teleporter** pairs (each lever activates one specific route via logic lamp circuits)

**Statue Spawners** (per section where applicable):
- Timer (1-second) → Statue → open area
- Lava pit (thin layer) below spawn point for automatic drops
- Statues available for: Slime, Skeleton, Bat, Fish, Crab, Jellyfish, Piranha, Shark, Unicorn, Mimic, Bomb, Heart, Star

**Trap Demonstrations**:
- Dungeon section: Dart Traps, Super Dart Traps, Spear Traps, Flame Traps, Spike Ball Traps
- Temple section: Lihzahrd Traps (Super Dart, Flame, Spiky Ball, Spear)
- General: Geysers, Detonators, Explosives (deactivated with actuators)

---

## 7. Paired Characters

### 7.1 Biome Scholar

- **Mode**: Journey
- **Purpose**: Exploration, research duplication, god mode for safe observation
- **Research Status**: All items researched (or maximum practical set)
- **Loadout**:
  - Rod of Discord (instant teleportation)
  - Cell Phone (full info display)
  - Sonar Potion, Hunter Potion, Spelunker Potion (permanent via Journey duplication)
  - Void Bag + Void Vault
  - Full mobility accessories (Terraspark Boots, wings, Shield of Cthulhu)
  - No weapons needed (god mode)
- **Appearance**: Scholarly outfit (Wizard Hat, Gi, or similar)
- **Use Case**: Visiting sections to observe, checking biome detection, reading signs, verifying NPC happiness

### 7.2 Biome Warden

- **Mode**: Master
- **Purpose**: Testing spawn conditions, verifying enemy drops, combat validation
- **Loadout**:
  - Zenith (melee)
  - S.D.M.G. (ranged)
  - Last Prism (magic)
  - Terraprisma (summon)
  - Full Solar Flare armor (tank)
  - Ankh Shield, Master Ninja Gear, Celestial Shell
  - Cell Phone, Rod of Discord
  - Void Bag with spare armor sets (Vortex, Nebula, Stardust)
- **Appearance**: Warden-themed (Red's set or similar endgame vanity)
- **Use Case**: Standing in biome sections to verify correct enemy spawns, testing drop rates, confirming biome-specific events trigger

---

## 8. Construction Methodology

### 8.1 Phase 1: World Generation & Clearing

1. Generate fresh Large Master world
2. Use TEdit (external map editor) for bulk terraforming:
   - Flatten terrain in section zones
   - Remove existing biome blocks that would interfere
   - Place isolation barriers between sections
3. Alternatively: In-game with Journey mode god mode + research-duplicated blocks

### 8.2 Phase 2: Section Construction (per biome)

For each of the 30 sections:
1. Place biome-defining blocks to 150% threshold
2. Build NPC housing (standardized room template)
3. Place entrance sign with biome name
4. Place teleporter pad + wire to hub
5. Place chests and fill with biome-specific items
6. Place item frames, weapon racks, mannequins
7. Place mechanics signs (2-4 per section)
8. Build wiring demo if applicable
9. Verify biome detection (check background/music change)
10. Verify NPC can move in

### 8.3 Phase 3: Hub & Network

1. Build central hub structure
2. Wire all 30 teleporter routes
3. Test every teleporter pair (round-trip)
4. Place hub amenities (crafting stations, storage)
5. Place master index signs

### 8.4 Phase 4: Validation

1. Walk through every section with Biome Scholar
2. Confirm biome background/music triggers in each
3. Stand in each section with Biome Warden, verify spawns
4. Check all NPC housing validity
5. Test all teleporters
6. Review all signs for accuracy

---

## 9. Known Constraints & Risks

| Risk | Mitigation |
|------|-----------|
| Biome bleed (corruption/hallow spreading) | Hardmode not activated in this world; if needed, use non-corruptible barriers |
| Section too narrow for biome detection | 200-tile width exceeds 170-tile scan width; safe margin |
| NPC won't move in (corruption nearby) | Evil biome sections isolated with 50+ tile gaps of pure blocks |
| Teleporter wiring conflicts | Use junction boxes; test each route individually |
| World file size | Large world with heavy construction may approach 30-40 MB; acceptable |
| Dungeon biome requires specific wall types | Use naturally-generated dungeon walls (cannot be player-placed for biome detection in some versions) — may need to preserve original dungeon location |
| Ocean biome is position-locked | Build ocean sections at actual world edges (cannot be relocated) |

### 9.1 Dungeon Wall Caveat

In Terraria 1.4.x, the Dungeon biome requires **naturally-placed Dungeon Walls** (not player-placed) for Dungeon Guardian spawning and some enemy spawns. The section must either:
- Be built at the world's natural dungeon location, OR
- Use only the block-count method (250 Dungeon Bricks) for biome music/background, accepting that some spawn mechanics won't work

**Decision**: Preserve the natural dungeon location and build the Dungeon section around it.

### 9.2 Ocean Position Lock

Ocean biome is determined by player position (within 250 tiles of world edge) plus water volume. Cannot be relocated. The Ocean sections must remain at world edges.

**Decision**: Use natural world edges for Ocean sections. This is already reflected in the layout plan.

---

## 10. File Manifest

| File | Location | Purpose |
|------|----------|---------|
| World file (.wld) | `saves/biome-encyclopedia/` | The constructed world |
| Biome Scholar (.plr) | `saves/biome-encyclopedia/` | Journey mode exploration character |
| Biome Warden (.plr) | `saves/biome-encyclopedia/` | Master mode combat character |
| design.md | `originals/biome-encyclopedia/` | This document |
| acceptance-checklist.md | `originals/biome-encyclopedia/` | Completion criteria |
| README.md | `originals/biome-encyclopedia/` | Project overview |

---

## 11. Relationship to Other Projects

- **Astral Forge Vault** (Project #1): The Vault stores items; the Encyclopedia displays and explains them in context. Items may be sourced from the Vault during construction.
- **Future projects**: The Encyclopedia can serve as a testing ground for verifying biome-specific mechanics before implementing them elsewhere.

---

## 12. Open Questions

- [ ] Should Hardmode be activated in this world? (Enables Hallow/Underground evil spawns but risks spread)
- [ ] TEdit vs. in-game construction? (TEdit is faster but less "legitimate")
- [ ] Include pre-Hardmode and Hardmode variants of evil biomes as separate sections, or toggle via Hardmode activation?
- [ ] Should the Graveyard section use real tombstones (which despawn) or painted blocks shaped like tombstones? (Real tombstones required for biome detection)
- [ ] Include a "Biome Interactions" section showing what happens when biomes overlap (e.g., Corrupt Desert, Hallowed Ice)?
