# TerrariaAgentFramework — Complete API Reference

> Version 2.1 · Built on .NET 8 + TEdit core libraries

---

## Overview

TerrariaAgentFramework is a programmatic world and character generation engine for Terraria. It exposes a fluent C# API and a JSON-driven CLI that lets agents create fully-populated worlds and characters without touching the game.

```
Input: JSON spec file
Output: .wld world file + .plr player files
```

---

## CLI Reference

```powershell
$dotnet = "D:\Terraria_doc\.work\dotnet\dotnet.exe"
$proj   = "D:\Terraria_doc\.work\TerrariaAgentFramework\TerrariaAgentFramework.csproj"

# Generate world + characters from spec
& $dotnet run --project $proj -- --spec path/to/spec.json --output D:\output\

# Quick character creation
& $dotnet run --project $proj -- --player "Solar Warden" --class melee --god --output player.plr

# Validate a spec without generating
& $dotnet run --project $proj -- --spec path/to/spec.json --dry-run
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--spec <path>` | string | Path to JSON world specification |
| `--output <path>` | string | Output directory (worlds) or file path (players) |
| `--player <name>` | string | Quick player name (bypasses spec) |
| `--class <class>` | string | `melee` \| `ranged` \| `mage` \| `summoner` |
| `--difficulty <diff>` | string | `classic` \| `mediumcore` \| `hardcore` \| `journey` |
| `--god` | flag | Max stats + all buffs + all accessory slots |
| `--dry-run` | flag | Validate spec and print plan without writing files |
| `--help` | flag | Show usage |

---

## JSON Spec Format

### Top-Level Schema

```json
{
  "title": "string — world name",
  "size": "Small | Medium | Large",
  "difficulty": "Classic | Expert | Master | Journey",
  "seed": "string — optional world seed",
  "spawnX": "int — optional spawn tile X",
  "spawnY": "int — optional spawn tile Y",
  "sourceWorld": "string — optional path to base .wld to modify",
  "hub": { "type": "celestial | simple | none" },
  "biomes": [ BiomeSpec ],
  "structures": [ StructureSpec ],
  "architecture": [ StructureSpec ],
  "terrain": [ StructureSpec ],
  "teleporterNetwork": true,
  "players": [ PlayerSpec ]
}
```

### BiomeSpec

```json
{
  "type": "forest | desert | snow | jungle | ocean | mushroom | corruption | crimson | hallow | dungeon | hell | space | granite | marble | spider",
  "position": 1000,
  "width": 250
}
```

`position` is the tile X coordinate of the biome's left edge. `width` is in tiles.

### StructureSpec

```json
{
  "type": "string — see tables below",
  "x": 2000,
  "y": 500,
  "params": {
    "key": "value"
  }
}
```

### PlayerSpec

```json
{
  "name": "string",
  "difficulty": "Classic | Mediumcore | Hardcore | Journey",
  "health": 500,
  "mana": 200,
  "maxStats": true,
  "godMode": true,
  "allPermanentBuffs": true,
  "allAccessorySlots": true,
  "armor": ["Solar Flare Helmet", "Solar Flare Breastplate", "Solar Flare Leggings"],
  "accessories": ["Ankh Shield", "Terraspark Boots"],
  "weapons": ["Zenith", "Last Prism"],
  "tools": ["Cell Phone", "Rod of Discord"],
  "utility": ["Magic Mirror", "Piggy Bank"],
  "items": [
    { "name": "Luminite Bullet", "stack": 999 },
    { "name": "Celestial Sigil", "stack": 99 }
  ],
  "prefixes": {
    "0": "Legendary",
    "1": "Unreal"
  }
}
```

---

## Structure Types

### Structures (`structures` array)

| Type | Description | Key Params |
|------|-------------|-----------|
| `boss_arena` | Multi-tier platform arena with campfires, heart lanterns, and nurse housing | `tiers` (int, default 8) |
| `storage_vault` | Organized chest vault with labeled sections | `chests` (int, default 20) |
| `npc_housing` | Valid NPC housing rooms in a row | `count` (int, default 10) |
| `crafting_hub` | All crafting stations in one room | — |
| `farm` | Automated farm setup | `farmType`: `herb \| mushroom \| mob \| gem` |

### Architecture Types (`architecture` array)

| Type | Description |
|------|-------------|
| `castle` | Stone castle with towers, moat, and interior rooms |
| `sky_palace` | Floating palace with cloud blocks and sky-themed decor |
| `pagoda` | Multi-story Asian-style tower |
| `treehouse` | Living wood treehouse with rope bridges |
| `underwater_dome` | Glass dome submerged in water |
| `pyramid` | Sand pyramid with interior chambers |
| `mushroom_village` | Glowing mushroom biome village |
| `hell_fortress` | Hellstone fortress in the underworld |
| `observatory` | Tall tower with telescope and star charts |
| `colosseum` | Roman-style arena with spectator seating |
| `npc_town` | Full NPC town with varied housing styles |

### Terrain Types (`terrain` array)

| Type | Description |
|------|-------------|
| `mountain` | Surface mountain with cave system |
| `lake` | Surface lake with waterfall |
| `cave_system` | Underground cave network |
| `floating_island` | Sky island with loot chest |
| `waterfall` | Decorative waterfall from surface to underground |
| `lava_river` | Underground lava river in the cavern layer |
| `crystal_cavern` | Crystal shard cave with gem deposits |

---

## Hub Types

| Type | Description |
|------|-------------|
| `celestial` | Celestial-themed hub with Luminite blocks, teleporter pads, and trophy hall |
| `simple` | Basic wooden hub with minimal decoration |
| `none` | No hub generated |

---

## C# Fluent API

### WorldBuilder

```csharp
var world = new WorldBuilder("My World", WorldSize.Large, Difficulty.Master)
    .FromExisting("path/to/base.wld")   // optional: modify existing world
    .WithSeed("getfixedboi")
    .WithSpawn(4200, 400)
    .AddBiome(BiomeType.Jungle, x: 1200, width: 300)
    .AddStructure(StructureType.BossArena, x: 2000, y: 500, tiers: 8)
    .AddArchitecture(ArchitectureType.Colosseum, x: 5000, y: 500)
    .AddTerrain(TerrainType.FloatingIsland, x: 3000, y: 100)
    .WithTeleporterNetwork()
    .Build("output/My World.wld");
```

### PlayerBuilder

```csharp
var player = new PlayerBuilder("Solar Warden")
    .WithDifficulty(PlayerDifficulty.Classic)
    .WithMaxStats()
    .WithGodMode()
    .WithArmor("Solar Flare Helmet", "Solar Flare Breastplate", "Solar Flare Leggings")
    .WithAccessories("Ankh Shield", "Celestial Shell", "Terraspark Boots")
    .WithWeapons("Zenith", "Last Prism", "S.D.M.G.")
    .WithTools("Cell Phone", "Rod of Discord")
    .WithItems(("Luminite Bullet", 999), ("Celestial Sigil", 99))
    .WithPrefix(slot: 0, "Legendary")
    .Build("output/Solar Warden.plr");
```

### ItemLookup

```csharp
// Fuzzy name-to-ID resolution
int id = ItemLookup.FindItem("Zenith");           // exact match
int id = ItemLookup.FindItem("zenith");           // case-insensitive
int id = ItemLookup.FindItem("last prism");       // multi-word
int id = ItemLookup.FindTile("Dirt Block");       // tile ID
int id = ItemLookup.FindWall("Stone Wall");       // wall ID
```

---

## Prefix Reference

| Name | ID | Best For |
|------|----|---------|
| `Legendary` | 81 | Melee weapons |
| `Unreal` | 82 | Ranged weapons |
| `Mythical` | 83 | Magic weapons |
| `Ruthless` | 59 | Summon weapons |
| `Godly` | 59 | Universal weapons |
| `Warding` | 66 | Accessories (+4 defense) |
| `Menacing` | 72 | Accessories (+4% damage) |
| `Lucky` | 73 | Accessories (+4% crit) |

---

## Complete Spec Examples

See `Specs/` directory:

| File | Project | Description |
|------|---------|-------------|
| `boss-rush-colosseum.json` | Boss Rush Colosseum | 5 characters, 4 arena zones, colosseum architecture |
| `biome-encyclopedia-full.json` | Biome Encyclopedia | All 15 biomes, observatory, crystal cavern |
| `starter-academy.json` | Starter Academy | 3 progression characters, NPC town, herb farm |
| `wiring-masterclass.json` | Wiring Masterclass | 2 wiring characters, observatory, cave system |

---

## Extending the Framework

### Adding a New Structure Type

1. Add a case to `StructureFactory.cs`
2. Implement the `Build(World world, int x, int y, Dictionary<string, string>? params)` method
3. Add the type string to `WorldSpec.cs` documentation
4. Add a test in `tests/`

### Adding a New Architecture Type

Same pattern as structures, but in `ArchitectureFactory.cs`.

### Adding a New Biome Type

Add a case to `BiomeFactory.cs`. Each biome factory method receives the world, position, and width, and is responsible for placing the correct blocks, walls, and background elements to register as that biome in Terraria.

---

## Known Limitations

- World generation modifies tile data only — NPC spawning, boss flags, and event states require loading the world in-game at least once
- `sourceWorld` path must be an absolute path or relative to the project directory
- Player files generated with `godMode: true` will have all buffs active on first load
- Biome registration requires the correct minimum block counts (documented in BiomeFactory.cs comments)
