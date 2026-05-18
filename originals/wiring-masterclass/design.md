# Wiring Masterclass — Design Document

## Concept and Purpose

The Wiring Masterclass is a comprehensive educational world that teaches Terraria's wiring and logic system from first principles through advanced exploits. It serves as both a reference library and interactive tutorial for players who want to understand mechanical engineering in Terraria.

**Target Audience:**
- Intermediate players who have beaten the game but never explored wiring
- Builders who want to add mechanical features to their worlds
- Redstone-experienced Minecraft players transitioning to Terraria
- Players looking for mob farm designs and automation

**Problem Solved:** Terraria's wiring system is powerful but poorly documented in-game. Most players never learn beyond basic switches. This world provides hands-on demonstrations of every wiring concept with clear explanations.

---

## World Specifications

| Property | Value |
|----------|-------|
| Size | Large (8400 x 2400) |
| Difficulty | Journey Mode (for duplication/god mode during learning) |
| Evil | Corruption (irrelevant — surface is fully terraformed) |
| Seed | Any (world is fully custom-built) |
| Name | "Wiring Masterclass" |
| Wall Style | Clean stone slab / gemspark backgrounds per section |

---

## Overall Layout

The world uses a horizontal progression model. The surface is flattened from x:200 to x:8200. Each section occupies approximately 1200 tiles of horizontal space.

```
x:0    x:200       x:1500      x:2800      x:4100      x:5400      x:6700    x:8000  x:8400
|      |           |           |           |           |           |          |       |
| Buff | Section 1 | Section 2 | Section 3 | Section 4 | Section 5 | Section 6|       |
|      | BASICS    | LOGIC     | MACHINES  | ADVANCED  | HOIKS     | AUTO     |       |
|      |           |           |           |           |           |          |       |
```

**Vertical Layout:**
- Surface level (y:300): Hub and section headers
- Main demonstration area (y:320 to y:600): All circuits and machines
- Underground storage (y:600 to y:700): Backup item storage
- Deep area (y:700+): Untouched (available for player experimentation)

---

## Central Hub (x:200 to x:500, y:280 to y:380)

### Structure
- Grand hall built from Martian Conduit Plating and Blue Gemspark walls
- 6 teleporter pads arranged in a semicircle, each color-coded to its section
- Central information kiosk with signs explaining the world's purpose
- Item frame displays showing key items for each section

### Teleporter Color Coding
| Section | Wire Color | Pad Marker |
|---------|-----------|------------|
| 1 - Basics | Red wire | Red Gemspark block |
| 2 - Logic | Blue wire | Blue Gemspark block |
| 3 - Machines | Green wire | Green Gemspark block |
| 4 - Advanced | Yellow wire | Yellow Gemspark block |
| 5 - Hoiks | Purple Gemspark | Purple Gemspark block |
| 6 - Automation | Orange Gemspark | Orange Gemspark block |

### Hub Signs
- Welcome sign explaining the world
- "How to read demonstrations" guide sign
- Credits/version sign
- "Return here" instructions (Magic Mirror or teleporter)

---

## Section 1: Basic Wiring (x:500 to x:1500, y:300 to y:600)

### Theme
Stone Slab walls, wooden platform floors. "Workshop" aesthetic.

### Demonstrations (left to right)

#### 1.1 Wire Fundamentals (x:500-650)
- Sign: "Wires connect a trigger to a target. They are invisible without the Mechanical Lens."
- Demo: Single switch connected to a single torch (on/off)
- Demo: Same switch connected to 3 torches (one-to-many)
- Demo: Wire shown with and without Mechanical Lens (actuated blocks reveal/hide)

#### 1.2 Switches and Levers (x:650-850)
- Sign: "Switches toggle state. Levers stay in position."
- Demo: Every switch type side by side (Switch, Lever, all colored)
- Demo: Each connected to a door showing open/close behavior

#### 1.3 Pressure Plates (x:850-1050)
- Sign: "Pressure plates trigger when stepped on. Colors determine what activates them."
- Demo: Gray plate (players only) → opens door
- Demo: Brown plate (NPCs only) → lights torch
- Demo: Red/Green/Yellow/Blue plates (players + enemies) → activates traps
- Demo: Lihzahrd plate (everything) → triggers boulder
- Demo: Weighted plates (teal/pink/purple/orange) → player only, different weights
- Demo: Comparison showing all plates in a row with labels

#### 1.4 Timers (x:1050-1200)
- Sign: "Timers send a signal at regular intervals. 1s, 3s, and 5s variants."
- Demo: 1-second timer → blinking torch
- Demo: 3-second timer → cycling colored torches
- Demo: 5-second timer → slow door open/close
- Demo: All three side by side for speed comparison

#### 1.5 Actuators (x:1200-1400)
- Sign: "Actuators make solid blocks pass-through. Essential for hidden doors."
- Demo: Row of blocks with actuators — switch toggles solidity
- Demo: Hidden door in a wall (actuated stone bricks)
- Demo: Retractable bridge over a pit
- Demo: Actuated blocks with different materials showing visual difference

#### 1.6 Wire Colors (x:1400-1500)
- Sign: "4 wire colors (Red, Blue, Green, Yellow) allow independent circuits to cross."
- Demo: 4 switches, 4 torches, wires crossing but independent
- Demo: Single tile with all 4 wire colors passing through it

---

## Section 2: Logic Gates (x:1500 to x:2800, y:300 to y:600)

### Theme
Martian Conduit Plating walls, clean futuristic look.

### Demonstrations

#### 2.1 Junction Boxes Explained (x:1500-1700)
- Sign: "Junction boxes control how wires interact at crossings."
- Demo: Wire crossing WITHOUT junction box (signals pass through)
- Demo: Wire crossing WITH junction box (signals are blocked/redirected)
- Demo: All junction box types with labeled behavior

#### 2.2 Logic Gates — Lamps and Sensors (x:1700-1900)
- Sign: "Logic Gate Lamps are inputs. Logic Sensors read their state."
- Demo: Single lamp toggled by switch, sensor reads state
- Demo: Faulty vs Active lamp states shown side by side

#### 2.3 AND Gate (x:1900-2050)
- Sign: "AND: Output is ON only when ALL inputs are ON."
- Demo: 2-input AND gate with switches
- Demo: Truth table displayed on signs:
  - 0,0 → 0
  - 0,1 → 0
  - 1,0 → 0
  - 1,1 → 1
- Demo: 3-input AND gate

#### 2.4 OR Gate (x:2050-2200)
- Sign: "OR: Output is ON when ANY input is ON."
- Demo: 2-input OR gate with switches
- Demo: Truth table on signs
- Demo: Practical use — two entrances, one light

#### 2.5 NOT Gate (Inverter) (x:2200-2350)
- Sign: "NOT: Output is the OPPOSITE of input."
- Demo: Switch → NOT gate → torch (torch OFF when switch ON)
- Demo: Used to create "normally open" doors

#### 2.6 XOR Gate (x:2350-2500)
- Sign: "XOR: Output is ON when inputs DIFFER."
- Demo: 2-input XOR with switches
- Demo: Practical use — two-way light switch (hallway lighting)

#### 2.7 NAND, NOR, XNOR (x:2500-2700)
- Sign: "Compound gates built from basic gates."
- Demo: NAND (NOT + AND)
- Demo: NOR (NOT + OR)
- Demo: XNOR (NOT + XOR)
- Each with truth table signs

#### 2.8 Combinational Logic Example (x:2700-2800)
- Sign: "Combining gates creates complex behavior."
- Demo: 2-bit binary counter display
- Demo: Simple combination lock (3 levers in correct pattern opens door)

---

## Section 3: Practical Machines (x:2800 to x:4100, y:300 to y:600)

### Theme
Dungeon Brick walls, industrial/dangerous aesthetic.

### Demonstrations

#### 3.1 Dart Traps (x:2800-3000)
- Sign: "Dart traps fire projectiles when triggered. Timer + Dart Trap = automatic defense."
- Demo: Single dart trap with switch
- Demo: Timer-activated dart trap corridor
- Demo: Super Dart Trap comparison
- Demo: Flame Trap demonstration
- Demo: Spear Trap demonstration
- Demo: Spiky Ball Trap demonstration

#### 3.2 Boulder Traps (x:3000-3150)
- Sign: "Boulders deal massive damage and roll. One-use unless reset."
- Demo: Classic boulder drop trap
- Demo: Boulder corridor (multiple boulders in sequence)
- Demo: Resettable boulder trap using actuators

#### 3.3 Explosives (x:3150-3300)
- Sign: "Explosives and Detonators destroy blocks in a radius."
- Demo: Single explosive block with detonator (in contained chamber)
- Demo: Controlled demolition sequence
- Note sign: "Explosives destroy blocks permanently — use carefully!"

#### 3.4 Teleporters (x:3300-3550)
- Sign: "Teleporters move players/NPCs/enemies between two pads instantly."
- Demo: Simple A↔B teleporter pair
- Demo: One-way teleporter (using pressure plate on one end only)
- Demo: Multi-destination teleporter (switch selects destination)
- Demo: Enemy teleporter trap (pressure plate teleports enemies into lava)

#### 3.5 Pumps (x:3550-3800)
- Sign: "Inlet Pumps pull liquid. Outlet Pumps push liquid. Wire them together."
- Demo: Water pump system (moves water between tanks)
- Demo: Lava pump system
- Demo: Honey pump system
- Demo: Infinite liquid generator (pump loop)
- Demo: Obsidian generator (water + lava pumps meeting)

#### 3.6 Cannons and Fireworks (x:3800-4000)
- Sign: "Cannons launch projectiles. Bunny Cannon for fun, others for defense."
- Demo: Bunny Cannon with timer
- Demo: Snowball Cannon defense line
- Demo: Firework rocket launcher (celebration display)
- Demo: Confetti cannon array

#### 3.7 Music Boxes (x:4000-4100)
- Sign: "Music Boxes play recorded tracks when wired."
- Demo: Jukebox system — switch between 5 music boxes
- Demo: Timer-based playlist (auto-advances tracks)

---

## Section 4: Advanced Contraptions (x:4100 to x:5400, y:300 to y:700)

### Theme
Luminite Brick walls, endgame/cosmic aesthetic.

### Demonstrations

#### 4.1 Pixel Displays (x:4100-4500)
- Sign: "Gemspark blocks + wiring = controllable pixel displays."
- Demo: 8x8 pixel display with manual toggle switches
- Demo: Pre-programmed image display (creeper face, heart, sword)
- Demo: Scrolling text display "TERRARIA" (timer-driven)
- Demo: Binary clock display

#### 4.2 Mob Farms with Wire Triggers (x:4500-4900)
- Sign: "Combine traps, teleporters, and timers for automated mob farming."
- Demo: Basic mob grinder (dart traps + timer in enclosed space)
- Demo: Lava trap farm (thin lava layer, conveyor via slopes)
- Demo: Teleporter collection farm (enemies teleported to kill chamber)
- Demo: AFK farm with player sensor activation
- Each farm has item collection area below with chests

#### 4.3 Statue Engines (x:4900-5200)
- Sign: "Wired statues spawn enemies/critters/items on a timer."
- Demo: Slime statue + lava = gel farm
- Demo: Goldfish statue + lava = gold coin farm
- Demo: Jellyfish statue + lava = glowstick farm
- Demo: Heart/Star statue for regeneration stations
- Demo: King Statue / Queen Statue NPC teleportation
- Demo: All functional statues labeled with their outputs

#### 4.4 Announcement Boxes (x:5200-5400)
- Sign: "Announcement Boxes display custom text in chat when triggered."
- Demo: Pressure plate → announcement box greeting
- Demo: Multi-message system (sequential announcements)
- Demo: Warning system for trap areas

---

## Section 5: Hoik Engines and Exploits (x:5400 to x:6700, y:300 to y:700)

### Theme
Hive walls and Honey blocks, organic/experimental aesthetic.

### Demonstrations

#### 5.1 Hoik Fundamentals (x:5400-5700)
- Sign: "Hoiks exploit slope collision to move entities at extreme speed. Not a bug — a feature!"
- Demo: Basic upward hoik (single tile, player launched up)
- Demo: Basic downward hoik
- Demo: Basic horizontal hoik (left and right)
- Demo: Speed comparison — hoik vs teleporter vs walking
- Sign: "Hoiks work by placing slopes so the game pushes you through blocks."

#### 5.2 Hoik Elevators (x:5700-6000)
- Sign: "Vertical hoik shafts move players up/down instantly."
- Demo: Simple hoik elevator (up only)
- Demo: Bidirectional hoik elevator (switch selects direction)
- Demo: Multi-floor hoik elevator with floor selection
- Demo: Express elevator (surface to underground in <1 second)

#### 5.3 Hoik Tracks (x:6000-6300)
- Sign: "Horizontal hoik tracks are faster than Minecart Rails."
- Demo: Long horizontal hoik track
- Demo: Hoik track with curves (direction changes)
- Demo: Hoik loop (circular track)
- Demo: Comparison: Hoik vs Minecart vs Teleporter for horizontal travel

#### 5.4 NPC Hoiks (x:6300-6500)
- Sign: "NPCs can be hoiked to reposition them without housing reassignment."
- Demo: NPC collection hoik (gathers all NPCs to one spot)
- Demo: NPC delivery system (hoik NPCs to specific locations)
- Demo: Pylon-compatible NPC positioning via hoik

#### 5.5 Advanced Hoik Applications (x:6500-6700)
- Sign: "Hoiks combined with wiring enable complex transport systems."
- Demo: Hoik + actuator toggled track (on/off transport)
- Demo: Item hoik (moving dropped items)
- Demo: Enemy hoik trap (forces enemies into kill chamber)
- Demo: Hoik-based mob farm

---

## Section 6: Automated Systems (x:6700 to x:8000, y:300 to y:700)

### Theme
Steampunk walls and Cog blocks, automation aesthetic.

### Demonstrations

#### 6.1 Day/Night Sensors (x:6700-6900)
- Sign: "Logic Sensors detect time of day, player proximity, and liquid."
- Demo: Day sensor → opens outer doors at dawn
- Demo: Night sensor → activates torch lighting at dusk
- Demo: Combined day/night → automatic lamp posts
- Demo: Player Above sensor → automatic lighting when player enters room

#### 6.2 Liquid Sensors and Generators (x:6900-7200)
- Sign: "Liquid sensors detect water/lava/honey. Pumps can generate infinite liquid."
- Demo: Water sensor → triggers pump when level drops
- Demo: Self-refilling water tank
- Demo: Infinite water generator (pump timer loop)
- Demo: Infinite lava generator
- Demo: Infinite honey generator
- Demo: Obsidian/Honey Block factory (automated liquid mixing)

#### 6.3 Automatic Doors (x:7200-7450)
- Sign: "Pressure plates + doors/actuators = hands-free entry."
- Demo: Simple pressure plate door
- Demo: Actuator hidden door (walk-through wall)
- Demo: Timed auto-close door (opens, waits 3s, closes)
- Demo: One-way door (only opens from one side)
- Demo: NPC-proof door (gray pressure plate only)

#### 6.4 Trap Defense Systems (x:7450-7700)
- Sign: "Automated defenses protect your base without player input."
- Demo: Perimeter dart trap system (enemy pressure plates)
- Demo: Lava moat with pump refill
- Demo: Falling boulder reset trap
- Demo: Multi-layer defense (darts + spears + spiky balls)
- Demo: Blood Moon auto-defense activation (using night sensor)

#### 6.5 Automated Farms (x:7700-7900)
- Sign: "Wire-based farms for resources."
- Demo: Automated mushroom farm (actuated mud blocks, timer harvest)
- Demo: Herb garden with planter boxes and timer-based harvest check
- Demo: Tree farm with actuated base blocks
- Demo: Crystal shard farm (pearlstone + timer-based collection)

#### 6.6 Complex Integrated Systems (x:7900-8000)
- Sign: "Combining everything: a fully automated base."
- Demo: Complete automated house:
  - Auto-lights (day/night sensor)
  - Auto-doors (pressure plates)
  - Auto-defense (enemy sensors + traps)
  - Auto-healing (heart statue + timer)
  - Status display (announcement boxes)

---

## Item Lists for Key Chests

### Hub Chest — Wiring Tools
| Item | Quantity |
|------|----------|
| The Grand Design | 1 |
| Wire | 9999 |
| Wrench (Red) | 1 |
| Blue Wrench | 1 |
| Green Wrench | 1 |
| Yellow Wrench | 1 |
| Wire Cutter | 1 |
| Multicolor Wrench | 1 |
| Mechanical Lens | 1 |
| Actuator | 999 |
| Presserator | 1 |

### Section 1 Chest — Basic Components
| Item | Quantity |
|------|----------|
| Switch | 50 |
| Lever | 50 |
| Pressure Plate (all colors) | 20 each |
| Timer (1s) | 10 |
| Timer (3s) | 10 |
| Timer (5s) | 10 |
| Torch | 200 |
| Door | 20 |

### Section 3 Chest — Traps and Machines
| Item | Quantity |
|------|----------|
| Dart Trap | 50 |
| Super Dart Trap | 50 |
| Flame Trap | 30 |
| Spear Trap | 30 |
| Spiky Ball Trap | 30 |
| Boulder | 20 |
| Explosive | 10 |
| Detonator | 5 |
| Teleporter | 20 |
| Inlet Pump | 10 |
| Outlet Pump | 10 |

### Section 4 Chest — Advanced Materials
| Item | Quantity |
|------|----------|
| Gemspark Block (all colors) | 200 each |
| Logic Gate (AND) | 30 |
| Logic Gate (OR) | 30 |
| Logic Gate (NAND) | 30 |
| Logic Gate (NOR) | 30 |
| Logic Gate (XOR) | 30 |
| Logic Gate (XNOR) | 30 |
| Logic Gate Lamp (On) | 50 |
| Logic Gate Lamp (Off) | 50 |
| Logic Sensor (Day) | 10 |
| Logic Sensor (Night) | 10 |
| Logic Sensor (Player Above) | 10 |
| Announcement Box | 20 |

### Section 5 Chest — Hoik Materials
| Item | Quantity |
|------|----------|
| Stone Block | 9999 |
| Hammer (any high-tier) | 1 |
| Actuator | 999 |
| Rope | 999 |
| Platform | 500 |

### Section 6 Chest — Automation
| Item | Quantity |
|------|----------|
| Logic Sensor (Day) | 20 |
| Logic Sensor (Night) | 20 |
| Logic Sensor (Player Above) | 20 |
| Logic Sensor (Water) | 10 |
| Logic Sensor (Lava) | 10 |
| Logic Sensor (Honey) | 10 |
| Inlet Pump | 20 |
| Outlet Pump | 20 |
| Timer (1s) | 20 |
| Heart Statue | 5 |
| Star Statue | 5 |
| King Statue | 3 |
| Queen Statue | 3 |

---

## NPC Housing Plan

NPCs are housed in the Hub area (x:200-500, y:280-380) for convenience:

| NPC | Purpose | Location |
|-----|---------|----------|
| Mechanic | Sells wiring components | Hub, Room 1 |
| Steampunker | Sells Steampunk items, teleporters | Hub, Room 2 |
| Cyborg | Sells rockets, nanites | Hub, Room 3 |
| Goblin Tinkerer | Reforging tools | Hub, Room 4 |
| Wizard | Sells magic items | Hub, Room 5 |
| Nurse | Healing | Hub, Room 6 |

All rooms are 10x6 tiles minimum with:
- Background wall (Martian Conduit Plating)
- Light source (Martian Lantern)
- Flat surface (Martian Table)
- Comfort item (Martian Chair)
- Door or platform entry

---

## Paired Character Specifications

### Character 1: "Wire Wizard"

| Property | Value |
|----------|-------|
| Name | Wire Wizard |
| Difficulty | Journey |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | The Grand Design | — |
| Weapon 2 | Clentaminator | — |
| Tool 1 | Drill Containment Unit | — |
| Tool 2 | Cell Phone | — |
| Accessory 1 | Master Ninja Gear | Warding |
| Accessory 2 | Terraspark Boots | Warding |
| Accessory 3 | Celestial Shell | Warding |
| Accessory 4 | Ankh Shield | Warding |
| Accessory 5 | Wings (Celestial Starboard) | Warding |
| Accessory 6 | Mechanical Lens (vanity) | — |
| Armor (Head) | Solar Flare Helmet | — |
| Armor (Body) | Solar Flare Breastplate | — |
| Armor (Legs) | Solar Flare Leggings | — |

**Inventory:**
- Full stack of each wire color (999)
- All wrench types
- Wire Cutter
- Actuators (999)
- Presserator
- All pressure plate types (50 each)
- All timer types (20 each)
- Switches and Levers (99 each)
- Magic Mirror
- Piggy Bank, Safe, Void Vault

### Character 2: "Trap Master"

| Property | Value |
|----------|-------|
| Name | Trap Master |
| Difficulty | Journey |
| Health | 500 |
| Mana | 200 |

**Loadout:**
| Slot | Item | Modifier |
|------|------|----------|
| Weapon 1 | Zenith | Legendary |
| Weapon 2 | S.D.M.G. | Unreal |
| Tool 1 | Drill Containment Unit | — |
| Tool 2 | Cell Phone | — |
| Accessory 1 | Master Ninja Gear | Warding |
| Accessory 2 | Terraspark Boots | Warding |
| Accessory 3 | Celestial Shell | Warding |
| Accessory 4 | Ankh Shield | Warding |
| Accessory 5 | Wings (Celestial Starboard) | Warding |
| Accessory 6 | Mechanical Lens (vanity) | — |
| Armor (Head) | Solar Flare Helmet | — |
| Armor (Body) | Solar Flare Breastplate | — |
| Armor (Legs) | Solar Flare Leggings | — |

**Inventory:**
- Dart Trap (99), Super Dart Trap (99)
- Flame Trap (99), Spear Trap (99), Spiky Ball Trap (99)
- Boulder (50)
- Teleporter (50)
- Inlet Pump (50), Outlet Pump (50)
- All statue types (functional ones, 5 each)
- Explosive (20), Detonator (10)
- Cannon, Bunny Cannon, Snowball Cannon
- Gemspark Blocks (all colors, 200 each)
- Logic Gates (all types, 30 each)
- Logic Gate Lamps (50 each)
- Logic Sensors (all types, 20 each)
- Announcement Box (20)
- Magic Mirror
- Piggy Bank, Safe, Void Vault

---

## Technical Notes

### Construction Requirements
1. **World must be Journey Mode** — allows research/duplication of wiring components and god mode for safe demonstration viewing.
2. **All demonstrations must be self-contained** — each demo should work independently without affecting others.
3. **Wire routing must avoid cross-contamination** — use all 4 wire colors strategically; junction boxes where colors must cross.
4. **Signs must use clear, concise language** — max 3-4 lines per sign. Use multiple signs for complex explanations.
5. **Each demo needs a "reset" mechanism** — levers/switches should return demos to default state.
6. **Hoik sections require precise slope placement** — use half-blocks and slopes exactly as documented. Test each hoik before finalizing.
7. **Mob farm sections need enclosed spawn areas** — 84+ tiles from player position, proper spawn surfaces.
8. **Liquid generators must be sealed** — prevent accidental flooding with containment walls.
9. **Background walls must be placed everywhere** — prevents mob spawning in demonstration areas.
10. **Lighting must be adequate throughout** — players should never be in darkness while learning.

### Build Order Recommendation
1. Flatten terrain and place background walls
2. Build Hub structure and NPC housing
3. Build section dividers and headers
4. Wire teleporter network (Hub ↔ all sections)
5. Build Section 1 (simplest, establishes patterns)
6. Build Section 2 (logic gates)
7. Build Section 3 (machines)
8. Build Section 6 (automation — uses concepts from 1-3)
9. Build Section 4 (advanced — uses concepts from 1-3)
10. Build Section 5 (hoiks — independent system)
11. Final testing pass — verify every demonstration works
12. Place all signs and labels
13. Stock all chests
14. Create paired characters

### Sign Convention
- **White signs**: Section headers and navigation
- **Yellow signs**: Demonstration titles
- **Green signs**: Explanatory text (how it works)
- **Red signs**: Warnings (explosives, lava, one-way mechanisms)
