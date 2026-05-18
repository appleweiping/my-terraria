# Boss Rush Colosseum — Design Document

## Concept and Purpose

The Boss Rush Colosseum is a purpose-built combat world designed for fighting every Terraria boss in optimal conditions. Each arena is specifically engineered for its target boss with correct dimensions, platform layouts, buff stations, and escape routes. The world enables players to practice boss fights, test loadouts, and complete full boss rush challenges.

**Target Audience:**
- Players practicing specific boss fights
- Speedrunners optimizing boss kill times
- Players testing class-specific builds against all bosses
- Groups doing multiplayer boss rush challenges
- Content creators recording boss fight footage

**Problem Solved:** Building proper arenas for every boss is time-consuming. Most players fight bosses in suboptimal arenas. This world provides perfectly optimized arenas for every encounter, with all summon items and class loadouts pre-stocked.

---

## World Specifications

| Property | Value |
|----------|-------|
| Size | Large (8400 x 2400) |
| Difficulty | Master Mode (maximum challenge) |
| Evil | Corruption (for Eater of Worlds arena) |
| Seed | Any (world is fully custom-built) |
| Name | "Boss Rush Colosseum" |
| Hardmode | Yes (world is in post-Moon Lord state) |

**Note:** World must be in post-Moon Lord state so all arenas and events are accessible. Pillars have been defeated. All biomes exist for biome-specific bosses.

---

## Overall Layout

```
x:0       x:1000      x:2800      x:4800      x:6200      x:8400
|         |           |           |           |           |
| Central | Pre-HM    | Hardmode  | Endgame   | Events    |
| Hub     | Arenas    | Arenas    | Arenas    | Arenas    |
|         |           |           |           |           |
```

**Vertical Layout:**
- Surface (y:300): Hub, preparation rooms, NPC housing
- Arena level (y:400-800): Main combat arenas (tall for flight)
- Underground (y:800-1200): Wall of Flesh prep, underground arenas
- Hell (y:2000-2400): Wall of Flesh arena (horizontal corridor)

---

## Central Hub (x:0 to x:1000, y:250 to y:450)

### Structure
- Grand colosseum entrance built from Luminite Bricks and Martian Conduit Plating
- Trophy hall displaying all boss trophies and relics
- Class loadout rooms (4 rooms, one per class)
- General preparation room with all buff stations
- Teleporter network to all arenas
- NPC housing wing

### Trophy Hall (x:100-400, y:280-350)
- Wall-mounted item frames with every boss trophy
- Relic pedestals for every boss relic (Master Mode)
- Boss banners displayed
- Music boxes for each boss theme

### Preparation Room (x:400-600, y:280-380)
**Buff Stations:**
| Station | Buff Provided |
|---------|--------------|
| Campfire | Life regeneration |
| Heart Lantern | Life regeneration (stacks) |
| Star in a Bottle | Mana regeneration |
| Honey pool (shallow) | Honey buff |
| Sunflower | Movement speed + reduced enemy spawns |
| Bast Statue | +5 defense |
| Ammo Box | 20% ammo conservation |
| Bewitching Table | +1 minion slot |
| Crystal Ball | +20 mana, magic buffs |
| Sharpening Station | Armor penetration |
| War Table | — |
| Slice of Cake | Sugar Rush |

**Potion Chest:**
| Potion | Quantity |
|--------|----------|
| Ironskin Potion | 99 |
| Regeneration Potion | 99 |
| Swiftness Potion | 99 |
| Wrath Potion | 99 |
| Rage Potion | 99 |
| Endurance Potion | 99 |
| Lifeforce Potion | 99 |
| Heartreach Potion | 99 |
| Summoning Potion | 99 |
| Archery Potion | 99 |
| Magic Power Potion | 99 |
| Ammo Reservation Potion | 30 |
| Greater Healing Potion | 99 |
| Super Healing Potion | 99 |
| Greater Mana Potion | 99 |
| Flask of Ichor | 99 |
| Flask of Cursed Flames | 99 |

### Class Loadout Rooms (x:600-1000, y:280-380)

Four rooms, each containing full progression loadouts for one class:

#### Melee Room
Chests organized by tier:
- Pre-Hardmode: Blade of Grass, Night's Edge, Molten Fury set, Molten armor
- Early Hardmode: Excalibur, Fetid Baghnakhs, Titanium armor
- Mid Hardmode: True Night's Edge, Chlorophyte armor, Turtle armor
- Late Hardmode: Terra Blade, Beetle armor, Influx Waver
- Endgame: Zenith, Solar Flare armor, Daybreak, Solar Eruption

#### Ranger Room
- Pre-Hardmode: Molten Fury, Bee's Knees, Necro armor, various arrows
- Early Hardmode: Daedalus Stormbow, Adamantite/Titanium armor
- Mid Hardmode: Megashark, Chlorophyte armor, Crystal/Ichor bullets
- Late Hardmode: Tsunami, Shroomite armor, Vortex Beater
- Endgame: S.D.M.G., Vortex armor, Phantasm, Luminite arrows/bullets

#### Mage Room
- Pre-Hardmode: Space Gun, Meteor armor, Water Bolt, Demon Scythe
- Early Hardmode: Crystal Serpent, Forbidden armor, Sky Fracture
- Mid Hardmode: Magical Harp, Spectre armor, Rainbow Rod
- Late Hardmode: Razorblade Typhoon, Spectre armor (hood/mask)
- Endgame: Last Prism, Nebula armor, Lunar Flare, Nebula Blaze

#### Summoner Room
- Pre-Hardmode: Imp Staff, Bee armor, Snapthorn
- Early Hardmode: Spider Staff, Spider armor, Cool Whip
- Mid Hardmode: Blade Staff, Hallowed armor, Durendal
- Late Hardmode: Xeno Staff, Tiki armor, Morning Star
- Endgame: Terraprisma, Stardust armor, Stardust Dragon, Kaleidoscope

---

## Pre-Hardmode Arenas (x:1000 to x:2800, y:300 to y:800)

### Arena 1: King Slime (x:1000-1400, y:400-700)
**Dimensions:** 400w x 300h tiles
**Design:**
- Flat platform arena with 5 rows of wooden platforms (every 50 tiles vertical)
- Rope columns on sides for vertical escape
- Lava pit at bottom (thin layer) for slime minion cleanup
- Campfire + Heart Lantern at center

**Summon Chest:**
| Item | Qty |
|------|-----|
| Slime Crown | 30 |
| Gold Crown | 5 |
| Gel | 999 |

### Arena 2: Eye of Cthulhu (x:1400-1900, y:350-750)
**Dimensions:** 500w x 400h tiles
**Design:**
- Large open arena (Eye needs flight space)
- 6 rows of long platforms (100+ tiles wide)
- Campfires and Heart Lanterns on every other platform
- No walls (Eye needs horizontal space for charges)
- Sunflower row at bottom

**Summon Chest:**
| Item | Qty |
|------|-----|
| Suspicious Looking Eye | 30 |

### Arena 3: Eater of Worlds (x:1000-1500, y:800-1200)
**Dimensions:** 500w x 400h (underground, in Corruption)
**Design:**
- Underground arena within Corruption biome
- Vertical shaft with platforms (worm needs vertical space)
- Ebonstone walls for biome requirement
- Piercing weapon effectiveness — open layout
- Heart Lanterns throughout

**Summon Chest:**
| Item | Qty |
|------|-----|
| Worm Food | 30 |
| Vile Powder | 99 |
| Rotten Chunk | 99 |

### Arena 4: Brain of Cthulhu (x:1500-2000, y:800-1200)
**Dimensions:** 500w x 400h (underground, in Crimson pocket)
**Design:**
- Artificial Crimson biome pocket (Crimstone walls/blocks)
- Open arena with scattered platforms
- Good visibility (Brain teleports — need to see it)
- Heart statues on timers for Creeper phase healing

**Summon Chest:**
| Item | Qty |
|------|-----|
| Bloody Spine | 30 |
| Vertebra | 99 |
| Vicious Powder | 99 |

### Arena 5: Queen Bee (x:2000-2400, y:800-1100)
**Dimensions:** 400w x 300h (underground Jungle)
**Design:**
- Artificial Jungle biome with Mud/Jungle Grass
- Enclosed arena (Queen Bee enrages outside Jungle underground)
- Platforms in grid pattern for dodging charges
- Honey pools at edges for regeneration
- Hive blocks for aesthetic

**Summon Chest:**
| Item | Qty |
|------|-----|
| Abeemination | 30 |
| Hive Block | 99 |

### Arena 6: Skeletron (x:2000-2500, y:400-750)
**Dimensions:** 500w x 350h (surface, at night)
**Design:**
- Surface arena near Dungeon entrance
- Wide platform layout for circling
- Must be fought at night (sign warning)
- Campfires on all platforms
- Nurse NPC housing adjacent for emergency healing

**Summon Chest:**
| Item | Qty |
|------|-----|
| Clothier Voodoo Doll | 10 |
| Note: "Talk to Old Man at Dungeon at night" | — |

### Arena 7: Deerclops (x:2400-2800, y:400-700)
**Dimensions:** 400w x 300h (surface, Snow biome)
**Design:**
- Artificial Snow biome (Snow Blocks)
- Flat arena with minimal platforms (Deerclops is ground-based)
- Wide horizontal space for dodging ice waves
- Campfires for warmth and regen

**Summon Chest:**
| Item | Qty |
|------|-----|
| Deer Thing | 30 |

### Arena 8: Wall of Flesh (x:200-8200, y:2100-2300)
**Dimensions:** Full world width x 200h (Hell layer)
**Design:**
- Long horizontal bridge across entire Hell biome
- Asphalt blocks for maximum run speed
- Campfires every 100 tiles
- Heart Lanterns every 150 tiles
- Lava below bridge (natural)
- Platform layers above bridge for vertical dodging
- Houses destroyed/removed to prevent Hungry spawns blocking path

**Summon Chest (at bridge start, both ends):**
| Item | Qty |
|------|-----|
| Guide Voodoo Doll | 30 |
| Note: "Throw into lava while Guide is alive" | — |

---

## Hardmode Arenas (x:2800 to x:4800, y:300 to y:800)

### Arena 9: Queen Slime (x:2800-3200, y:350-750)
**Dimensions:** 400w x 400h
**Design:**
- Hallow biome arena (Queen Slime is Hallow-themed)
- Multi-tier platform layout (she bounces and flies)
- Crystal blocks and Pearlstone aesthetic
- Open top for second phase flight

**Summon Chest:**
| Item | Qty |
|------|-----|
| Gelatin Crystal | 30 |

### Arena 10: The Twins (x:3200-3800, y:300-800)
**Dimensions:** 600w x 500h
**Design:**
- Very large open arena (two bosses need space)
- Long platforms for horizontal kiting
- Asphalt layer at bottom for ground-level speed
- Nurse housing at edge (emergency healing between phases)
- Must be night (sign warning)

**Summon Chest:**
| Item | Qty |
|------|-----|
| Mechanical Eye | 30 |

### Arena 11: The Destroyer (x:3200-3800, y:300-800)
**Shares arena with Twins** (same space works)
**Additional features:**
- Platform spacing optimized for piercing weapons
- Nurse accessible
- Must be night (sign warning)

**Summon Chest:**
| Item | Qty |
|------|-----|
| Mechanical Worm | 30 |

### Arena 12: Skeletron Prime (x:3200-3800, y:300-800)
**Shares arena with Twins/Destroyer** (Mech boss arena)
**Additional features:**
- Same large arena works for all 3 mechs
- Must be night (sign warning)

**Summon Chest:**
| Item | Qty |
|------|-----|
| Mechanical Skull | 30 |

### Arena 13: Plantera (x:3800-4200, y:800-1200)
**Dimensions:** 400w x 400h (underground Jungle)
**Design:**
- Large underground Jungle arena
- Mud blocks with Jungle Grass for biome
- Open center with ring of platforms around edges
- Multiple escape tunnels (Plantera is fast in phase 2)
- Plantera enrages above ground — fully enclosed underground
- Heart statues on timers

**Summon Chest:**
| Item | Qty |
|------|-----|
| Plantera's Bulb note: "Break bulb in Jungle Underground" | — |
| Pickaxe (for bulb) | 1 |

**Plantera Bulb Farm:** Small Jungle Grass area adjacent for bulb spawning.

### Arena 14: Golem (x:4200-4500, y:800-1100)
**Dimensions:** 300w x 300h (Lihzahrd Temple)
**Design:**
- Artificial Lihzahrd Temple room (Lihzahrd Bricks)
- Lihzahrd Altar placed in center
- Flat floor with 3 platform rows above
- Walls prevent Golem from leaving
- Compact but sufficient for dodging fists

**Summon Chest:**
| Item | Qty |
|------|-----|
| Lihzahrd Power Cell | 30 |
| Temple Key | 1 |

### Arena 15: Duke Fishron (x:4500-4800, y:300-700)
**Dimensions:** 300w x 400h (Ocean biome)
**Design:**
- Ocean biome arena (water at bottom)
- Platforms above water for aerial combat
- Very open — Duke Fishron is extremely fast
- Asphalt runway for phase transitions
- No walls — Duke needs maximum space
- Sign: "Summon by fishing in Ocean with Truffle Worm"

**Summon Chest:**
| Item | Qty |
|------|-----|
| Truffle Worm | 30 |
| Fishing Rod (Golden) | 1 |

### Arena 16: Empress of Light (x:4500-4800, y:300-700)
**Shares arena with Duke Fishron** (similar requirements)
**Design notes:**
- Same open arena works
- Sign: "For Terraprisma, fight during daytime (all attacks one-shot)"
- Lacewing spawning area adjacent (Hallow surface at night)

**Summon Chest:**
| Item | Qty |
|------|-----|
| Prismatic Lacewing | 30 |
| Note: "Kill Lacewing to summon. Daytime = instant kill attacks" | — |

---

## Endgame Arenas (x:4800 to x:6200, y:300 to y:800)

### Arena 17: Lunatic Cultist (x:4800-5100, y:300-600)
**Dimensions:** 300w x 300h (surface, at Dungeon)
**Design:**
- Dungeon entrance replica
- Open sky above for flight phase
- Platforms for dodging projectiles
- Cultist spawns at Dungeon — arena built around entrance
- Sign: "Kill Cultists at Dungeon entrance to summon"

**Summon Chest:**
| Item | Qty |
|------|-----|
| Note: "Defeat 4 Cultists at Dungeon entrance" | — |

### Arena 18: Celestial Pillars (x:5100-5800, y:300-700)
**Dimensions:** 700w x 400h (4 sub-arenas, 175w each)
**Design:**
- Four adjacent arenas, one per pillar color:
  - Solar (orange/red blocks)
  - Vortex (teal/green blocks)
  - Nebula (purple/pink blocks)
  - Stardust (blue/white blocks)
- Each sub-arena has appropriate platform layout:
  - Solar: ground-focused, platforms for dodging Crawltipedes
  - Vortex: vertical platforms for fighting flyers
  - Nebula: open space for teleporting enemies
  - Stardust: mixed layout for Star Cell splitting
- Sign: "Pillars spawn after Lunatic Cultist is defeated"

### Arena 19: Moon Lord (x:5800-6200, y:300-800)
**Dimensions:** 400w x 500h
**Design:**
- Maximum size arena (Moon Lord is enormous)
- Long platform rows for horizontal movement
- Nurse NPC housing at center (controversial but effective)
- Honey pool at center platform
- Heart statues on 1-second timers
- Star statues on 1-second timers
- Campfires and Heart Lanterns on every platform
- Asphalt bottom layer for ground kiting
- Sign: "Moon Lord spawns after all 4 Pillars are defeated"
- Sign: "Celestial Sigil also summons Moon Lord directly"

**Summon Chest:**
| Item | Qty |
|------|-----|
| Celestial Sigil | 30 |

---

## Event Arenas (x:6200 to x:8400, y:300 to y:700)

### Arena 20: Pirate Invasion (x:6200-6600, y:300-550)
**Dimensions:** 400w x 250h
**Design:**
- Flat ground arena with lava traps below
- Dart trap walls on both sides (timer-activated)
- Platforms above for player safety
- NPC housing nearby (invasion targets NPCs)
- Kill corridor funnels enemies through traps

**Summon Chest:**
| Item | Qty |
|------|-----|
| Pirate Map | 30 |

### Arena 21: Frost Moon (x:6600-7000, y:300-600)
**Dimensions:** 400w x 300h
**Design:**
- Must be night (sign warning)
- Multi-layer trap system (dart traps, spear traps, flame traps)
- Lava pit with thin lava layer for ground enemies
- Elevated player platform with campfires
- Heart statue timers for sustain
- Open top for Ice Queen flight phase

**Summon Chest:**
| Item | Qty |
|------|-----|
| Naughty Present | 30 |

### Arena 22: Pumpkin Moon (x:7000-7400, y:300-600)
**Dimensions:** 400w x 300h
**Design:**
- Similar to Frost Moon arena (shares design principles)
- Trap corridors for Mourning Wood
- Open sky for Pumpking flight
- Must be night (sign warning)
- Lava traps for ground enemies

**Summon Chest:**
| Item | Qty |
|------|-----|
| Pumpkin Moon Medallion | 30 |

### Arena 23: Old One's Army (x:7400-7800, y:350-550)
**Dimensions:** 400w x 200h
**Design:**
- Flat ground with Eternia Crystal Stand at center
- Sentry placement positions marked with blocks
- No traps (OOA has specific rules)
- Platforms above for player mobility
- Wide enough for all enemy paths
- Tavernkeep NPC housing adjacent

**Summon Chest:**
| Item | Qty |
|------|-----|
| Eternia Crystal | 30 |
| Defender Medals | 999 |
| All sentry items from Tavernkeep | — |

### Arena 24: Martian Madness (x:7800-8200, y:300-600)
**Dimensions:** 400w x 300h
**Design:**
- Open arena for Martian Saucer flight
- Platforms at multiple heights
- Ground traps for foot soldiers
- Elevated safe zone for saucer dodging
- Sign: "Trigger by being detected by Martian Probe in Space layer"

**Summon Chest:**
| Item | Qty |
|------|-----|
| Note: "Find Martian Probe in Space layer, let it escape" | — |
| Gravity Globe / Wings for reaching Space | 1 |

---

## NPC Housing Plan

NPCs housed in Hub area (x:600-1000, y:250-300) and near key arenas:

### Hub NPCs
| NPC | Purpose | Location |
|-----|---------|----------|
| Nurse | Healing between fights | Hub + Moon Lord arena |
| Dryad | Buff (Dryad's Blessing) | Hub |
| Arms Dealer | Ammo sales | Hub |
| Witch Doctor | Summoner items | Hub |
| Steampunker | Ammo, teleporters | Hub |
| Goblin Tinkerer | Reforging | Hub |
| Tavernkeep | OOA sentries | Hub + OOA arena |

### Arena-Adjacent NPCs
| NPC | Purpose | Location |
|-----|---------|----------|
| Nurse (clone housing) | Emergency healing | Moon Lord arena, Mech arena |
| Dryad (clone housing) | Blessing buff | Endgame section |

All rooms: 10x6 minimum, valid housing (light, table, chair, walls, door).

---

## Paired Character Specifications

### Character 1: "Melee Champion"

| Property | Value |
|----------|-------|
| Name | Melee Champion |
| Difficulty | Master |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | Zenith | Legendary |
| Weapon 2 | Solar Eruption | Godly |
| Weapon 3 | Daybreak | Godly |
| Weapon 4 | Terrarian | Legendary |
| Weapon 5 | Flying Dragon | Legendary |
| Accessory 1 | Warrior Emblem | Menacing |
| Accessory 2 | Mechanical Glove | Menacing |
| Accessory 3 | Fire Gauntlet | Menacing |
| Accessory 4 | Celestial Shell | Menacing |
| Accessory 5 | Ankh Shield | Warding |
| Accessory 6 | Terraspark Boots | Menacing |
| Accessory 7 | Celestial Starboard | Menacing |
| Armor | Solar Flare (full set) | — |

### Character 2: "Ranger Ace"

| Property | Value |
|----------|-------|
| Name | Ranger Ace |
| Difficulty | Master |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | S.D.M.G. | Unreal |
| Weapon 2 | Phantasm | Unreal |
| Weapon 3 | Vortex Beater | Unreal |
| Weapon 4 | Tsunami | Unreal |
| Weapon 5 | Celebration Mk2 | Unreal |
| Ammo 1 | Luminite Bullet | 9999 |
| Ammo 2 | Luminite Arrow | 9999 |
| Ammo 3 | Chlorophyte Bullet | 9999 |
| Ammo 4 | Holy Arrow | 9999 |
| Accessory 1 | Ranger Emblem | Menacing |
| Accessory 2 | Sniper Scope | Menacing |
| Accessory 3 | Magic Quiver (Molten) | Menacing |
| Accessory 4 | Celestial Shell | Menacing |
| Accessory 5 | Ankh Shield | Warding |
| Accessory 6 | Terraspark Boots | Menacing |
| Accessory 7 | Celestial Starboard | Menacing |
| Armor | Vortex (full set) | — |

### Character 3: "Mage Supreme"

| Property | Value |
|----------|-------|
| Name | Mage Supreme |
| Difficulty | Master |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | Last Prism | Mythical |
| Weapon 2 | Lunar Flare | Mythical |
| Weapon 3 | Nebula Blaze | Mythical |
| Weapon 4 | Razorblade Typhoon | Mythical |
| Weapon 5 | Nebula Arcanum | Mythical |
| Accessory 1 | Sorcerer Emblem | Menacing |
| Accessory 2 | Celestial Cuffs | Menacing |
| Accessory 3 | Mana Cloak | Menacing |
| Accessory 4 | Celestial Shell | Menacing |
| Accessory 5 | Ankh Shield | Warding |
| Accessory 6 | Terraspark Boots | Menacing |
| Accessory 7 | Celestial Starboard | Menacing |
| Armor | Nebula (full set) | — |

### Character 4: "Summoner Lord"

| Property | Value |
|----------|-------|
| Name | Summoner Lord |
| Difficulty | Master |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | Terraprisma | Ruthless |
| Weapon 2 | Stardust Dragon Staff | Ruthless |
| Weapon 3 | Stardust Cell Staff | Ruthless |
| Weapon 4 | Kaleidoscope | Legendary |
| Weapon 5 | Morning Star | Legendary |
| Accessory 1 | Summoner Emblem | Menacing |
| Accessory 2 | Papyrus Scarab | Menacing |
| Accessory 3 | Pygmy Necklace | Menacing |
| Accessory 4 | Celestial Shell | Menacing |
| Accessory 5 | Ankh Shield | Warding |
| Accessory 6 | Terraspark Boots | Menacing |
| Accessory 7 | Celestial Starboard | Menacing |
| Armor | Stardust (full set) | — |

### Character 5: "Arena Master"

| Property | Value |
|----------|-------|
| Name | Arena Master |
| Difficulty | Master |
| Health | 500 |
| Mana | 200 |

**Purpose:** Utility character for arena maintenance, teleportation, and setup.

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Tool 1 | Drill Containment Unit | — |
| Tool 2 | Cell Phone | — |
| Tool 3 | The Grand Design | — |
| Tool 4 | Rod of Discord | — |
| Weapon 1 | Zenith | Legendary |
| Accessory 1 | Master Ninja Gear | Warding |
| Accessory 2 | Terraspark Boots | Warding |
| Accessory 3 | Celestial Shell | Warding |
| Accessory 4 | Ankh Shield | Warding |
| Accessory 5 | Celestial Starboard | Warding |
| Accessory 6 | Mechanical Lens | — |
| Accessory 7 | Architect Gizmo Pack | — |
| Armor | Solar Flare (full set) | — |

**Inventory:**
- All boss summon items (30 each)
- All event summon items (30 each)
- Teleporters (50)
- Wire (9999)
- All buff potions (99 each)
- Magic Mirror
- Piggy Bank, Safe, Void Vault, Defender's Forge

---

## Technical Notes

### Construction Requirements
1. **World must be in post-Moon Lord Hardmode** — all content accessible.
2. **Corruption AND Crimson must both exist** — artificial Crimson biome for Brain of Cthulhu.
3. **Underground Jungle must be preserved** — Plantera bulbs need Jungle Grass.
4. **Hell bridge must span full world** — Wall of Flesh arena.
5. **Ocean biome must exist** — Duke Fishron requires Ocean.
6. **Hallow biome on surface** — Queen Slime, Empress of Light lacewing spawns.
7. **Snow biome** — Deerclops arena.
8. **Dungeon intact** — Lunatic Cultist spawns at Dungeon.
9. **Lihzahrd Temple accessible** — Golem requires Lihzahrd Altar.

### Arena Design Principles
- Minimum 168 tiles horizontal for bosses that charge (Eye, Twins, Duke)
- Minimum 100 tiles vertical for flying bosses
- Platform spacing: 20-25 tiles vertical (allows jump + hook)
- Campfire every 50 horizontal tiles
- Heart Lantern every 75 horizontal tiles
- Background walls in NPC areas only (arenas need mob spawning disabled via other means)
- Thin lava layers (1/255 bucket) for item farms without destroying drops

### Build Order Recommendation
1. Create Large Master Mode world
2. Progress to post-Moon Lord (or use builder tool to set world flags)
3. Flatten arena areas
4. Build Hell bridge (Wall of Flesh)
5. Create artificial biomes (Crimson pocket, Jungle underground, Hallow, Snow, Ocean)
6. Build Hub structure and NPC housing
7. Build Pre-Hardmode arenas (1-8)
8. Build Hardmode arenas (9-16)
9. Build Endgame arenas (17-19)
10. Build Event arenas (20-24)
11. Install teleporter network
12. Stock all summon chests
13. Place all signs and labels
14. Create all 5 paired characters
15. Full testing pass
