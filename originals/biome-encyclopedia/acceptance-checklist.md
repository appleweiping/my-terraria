# Biome Encyclopedia — Acceptance Checklist

**Project**: Biome Encyclopedia  
**Version**: Terraria 1.4.4.9  
**Last Updated**: 2026-05-18

---

## World Foundation

- [ ] Large world generated (8400 × 2400 tiles)
- [ ] Master difficulty set
- [ ] World loads without errors in Terraria 1.4.4.9
- [ ] Spawn point set at Central Hub
- [ ] World name set to "Biome Encyclopedia" (or similar identifiable name)

---

## Central Hub

- [ ] Hub structure built (300 tiles wide × 200 tiles tall)
- [ ] 30 teleporter pads placed and labeled with signs
- [ ] All teleporter routes functional (round-trip tested)
- [ ] All crafting stations present in hub
- [ ] Nurse + Dryad housed in hub (utility NPCs)
- [ ] Bed placed and spawn point set
- [ ] Master index signs placed (listing all sections)
- [ ] 10 storage chests with building/wiring supplies

---

## Biome Sections — Universal Criteria

For EACH of the 30 biome sections, ALL of the following must be true:

- [ ] Entrance sign placed with biome name and section number
- [ ] Teleporter pad present and wired to hub (return trip works)
- [ ] Biome background/music triggers correctly when player stands in section
- [ ] At least one chest present with key biome drops
- [ ] At least 2 mechanics signs explaining biome thresholds/requirements
- [ ] Section isolated from adjacent sections (no biome bleed detected)

---

## Biome-Specific Verification

### Surface Biomes

- [ ] **Forest/Purity**: Default background displays; no other biome overrides; Guide housed
- [ ] **Desert**: 2250+ Sand/Hardened Sand/Sandstone tiles placed; desert background triggers; Arms Dealer housed
- [ ] **Snow/Ice**: 2250+ Snow/Ice tiles placed; snow background triggers; Mechanic housed
- [ ] **Jungle**: 210+ Jungle Grass tiles placed; jungle background triggers; jungle music plays; Dryad housed
- [ ] **Ocean (West)**: Within 250 tiles of west world edge; sufficient water; ocean music plays; Angler housed
- [ ] **Ocean (East)**: Within 250 tiles of east world edge; sufficient water; ocean music plays; Pirate housed
- [ ] **Glowing Mushroom (Surface)**: 150+ Mushroom Grass tiles; mushroom background triggers; Truffle can move in (Hardmode required)

### Underground Biomes

- [ ] **Cavern**: Player below cavern layer; default underground background; Goblin Tinkerer housed
- [ ] **Underground Desert**: 2250+ desert tiles below surface layer; underground desert background triggers
- [ ] **Underground Snow/Ice**: 2250+ ice/snow tiles below surface layer; underground snow background triggers
- [ ] **Underground Jungle**: 210+ Jungle Grass tiles below surface layer; underground jungle music plays
- [ ] **Underground Mushroom**: 150+ Mushroom Grass tiles below surface layer; mushroom background triggers underground

### Evil Biomes

- [ ] **Corruption (Surface)**: 300+ Ebonstone/Corrupt Grass tiles at surface; corruption music plays; Shadow Orb items in chest
- [ ] **Corruption (Underground)**: 300+ Ebonstone tiles below surface; underground corruption background triggers
- [ ] **Crimson (Surface)**: 300+ Crimstone/Crimson Grass tiles at surface; crimson music plays; Crimson Heart items in chest
- [ ] **Crimson (Underground)**: 300+ Crimstone tiles below surface; underground crimson background triggers
- [ ] Evil biome sections have non-corruptible barriers on all sides (3+ tiles of wood/ash)

### Hardmode Biomes

- [ ] **Hallow (Surface)**: 190+ Pearlstone/Hallowed Grass tiles at surface; hallow music plays; Wizard housed
- [ ] **Hallow (Underground)**: 190+ Pearlstone/Pink Ice tiles below surface; underground hallow background triggers
- [ ] Hallow sections contained with non-corruptible barriers

### Special Biomes

- [ ] **Dungeon**: 375+ Dungeon Brick tiles below surface; dungeon music plays; naturally-generated dungeon walls present; Clothier housed
- [ ] **Lihzahrd Temple**: 375+ Lihzahrd Brick tiles below surface; temple background triggers; Lihzahrd traps demonstrated
- [ ] **Meteorite**: 115+ Meteorite Ore tiles placed; meteorite background triggers; Meteorite armor set in chest
- [ ] **Spider Nest**: 200+ Spider Wall tiles below surface; spider cave background triggers; Spider enemies can spawn
- [ ] **Granite Cave**: 150+ Granite Block/Wall tiles below surface; granite background triggers; Granite Golem can spawn
- [ ] **Marble Cave**: 150+ Marble Block/Wall tiles below surface; marble background triggers; Medusa/Hoplite can spawn
- [ ] **Bee Hive**: 200+ Hive/Honey tiles below surface; hive background triggers; Larva placed (or Queen Bee summon item in chest)

### Sky Biomes

- [ ] **Space**: Section built above Space layer; space background triggers; Harpy can spawn
- [ ] **Floating Island**: At least one constructed floating island with Skyware chest; Starfury/Lucky Horseshoe in chest

### Underworld

- [ ] **Hell/Underworld**: Section at world bottom (below Underworld layer); hell background triggers; Hellstone/Obsidian in chest; Demon/Voodoo Demon can spawn

### Event/Conditional Zones

- [ ] **Graveyard**: 5+ tombstones placed within 36-tile radius; graveyard fog effect triggers; Ecto Mist visible
- [ ] **Shimmer**: Shimmer liquid present; aether biome visual triggers; items can be transmuted in shimmer pool
- [ ] **Purity (Reference)**: Clean section with no biome override; serves as baseline comparison; standard forest music plays

---

## NPC Housing

- [ ] All NPC rooms pass housing validity check (query via "?" button in housing menu)
- [ ] NPCs assigned to biome-appropriate sections per happiness optimization table
- [ ] No NPC reports "unhappy" status due to biome or neighbor conflicts
- [ ] Truffle section has Mushroom biome active (required for Truffle to spawn)
- [ ] No housing within 45 tiles of Corruption/Crimson (except intentional evil-biome NPCs)

---

## Display & Documentation

- [ ] Each section has item frames displaying 3+ signature items for that biome
- [ ] Each section has at least one weapon rack with a biome-specific weapon
- [ ] Mannequins display biome-specific armor sets where applicable (Jungle, Snow, Desert, Dungeon, Hell)
- [ ] All signs are legible and contain accurate information (block counts, depth requirements, spawn conditions)
- [ ] No sign contains outdated or incorrect information for version 1.4.4.9

---

## Wiring & Mechanics

- [ ] All 30 teleporter pairs tested (hub → destination AND destination → hub)
- [ ] No wiring conflicts (teleporters don't activate unintended destinations)
- [ ] Statue spawners functional in applicable sections (timer activates, mob spawns)
- [ ] Trap demonstrations in Dungeon and Temple sections are functional but safe (player can observe without taking damage via actuated blocks or safe distance)
- [ ] Junction boxes used where wire colors must cross

---

## Paired Characters

### Biome Scholar (Journey Mode)

- [ ] Character created in Journey mode
- [ ] All mobility items present (Terraspark Boots, wings, Rod of Discord)
- [ ] Cell Phone crafted and in inventory
- [ ] Void Bag + Void Vault available
- [ ] God mode accessible (Journey power menu)
- [ ] Character can access all sections without obstruction

### Biome Warden (Master Mode)

- [ ] Character created in Master mode
- [ ] Zenith in inventory
- [ ] S.D.M.G. in inventory with ammo
- [ ] Last Prism in inventory
- [ ] Terraprisma in inventory
- [ ] Solar Flare armor equipped
- [ ] Ankh Shield equipped
- [ ] Cell Phone + Rod of Discord in inventory
- [ ] Spare armor sets in Void Bag (Vortex, Nebula, Stardust)
- [ ] Character can survive in all biome sections without dying

---

## Integrity & Maintenance

- [ ] World file backed up to `saves/biome-encyclopedia/` in Terraria_doc archive
- [ ] Both character files (.plr + .plr.bak) backed up alongside world
- [ ] No corruption/crimson spread detected outside designated evil sections
- [ ] World file size reasonable (under 50 MB)
- [ ] World loads in under 10 seconds on target hardware

---

## Final Validation Pass

- [ ] Complete walkthrough: teleport to every section from hub, verify biome triggers
- [ ] Complete sign audit: read every sign, confirm accuracy
- [ ] Complete chest audit: open every chest, confirm contents match biome
- [ ] Complete NPC audit: verify all NPCs are in assigned housing
- [ ] Screenshot documentation of each section (optional but recommended)
- [ ] No "homeless" NPCs (all assigned to valid housing)
- [ ] No floating/orphaned blocks or unfinished construction visible

---

## Completion Summary

| Category | Items | Verified |
|----------|-------|----------|
| World Foundation | 5 | _ / 5 |
| Central Hub | 8 | _ / 8 |
| Biome Sections (universal × 30) | 180 | _ / 180 |
| Biome-Specific | 30 | _ / 30 |
| NPC Housing | 5 | _ / 5 |
| Display & Documentation | 5 | _ / 5 |
| Wiring & Mechanics | 5 | _ / 5 |
| Biome Scholar | 6 | _ / 6 |
| Biome Warden | 10 | _ / 10 |
| Integrity | 5 | _ / 5 |
| Final Validation | 7 | _ / 7 |
| **TOTAL** | **~266** | **_ / 266** |

Project is complete when all items are checked.
