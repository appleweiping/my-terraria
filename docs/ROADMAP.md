# Content Expansion Roadmap

> A structured plan for building a top-tier Terraria save archive — not just a folder of `.wld` files, but an engineered collection with documentation, tooling, and curatorial standards.

---

## 1. Content Pillars

The archive organizes saves into six major categories. Each pillar represents a distinct purpose and audience. A complete archive has strong representation across all six.

### 1.1 Adventure & Story Maps

RPG campaigns, puzzle worlds, parkour challenges, and narrative-driven experiences built by the community. These are the saves people *play through* rather than reference.

- **Examples**: CTM (Complete the Monument), escape rooms, story-driven campaigns
- **What to look for**: Custom dialogue via signs, structured progression, intentional difficulty curves
- **Preservation value**: Many adventure maps disappear when forum threads die — archival prevents loss

### 1.2 All-Items & Utility Worlds

Storage hubs, crafting references, and research worlds designed for quick access to game content.

- **Examples**: Builder's Workshop, all-items maps, NPC housing templates
- **What to look for**: Organizational clarity, version currency, completeness of item coverage
- **Preservation value**: These are living documents — tracking versions shows how the game's item pool evolved

### 1.3 Build Showcases

Architecture, pixel art, themed megabuilds, and aesthetic demonstrations. The artistic side of Terraria.

- **Examples**: Pixel art worlds, castle builds, biome-themed cities, recreation builds
- **What to look for**: Technical skill, scale, creativity, use of paint/actuators/lighting
- **Preservation value**: Represents the ceiling of what's possible in vanilla or modded Terraria

### 1.4 Challenge & Speedrun Worlds

Boss rush arenas, class-locked challenge setups, hardcore progression worlds, and speedrun-optimized seeds.

- **Examples**: Boss rush arenas, "no-hit" practice worlds, pre-built class loadouts, seeded worlds with documented routes
- **What to look for**: Balance, replayability, clear rules/constraints documented in signs or companion files
- **Preservation value**: Captures the competitive and challenge community's infrastructure

### 1.5 Modded Archives

Saves from tModLoader ecosystems — Calamity, Thorium, Fargo's, and other major content mods.

- **Examples**: Calamity endgame worlds, Thorium progression saves, modded all-items worlds
- **What to look for**: Mod version pinning, load order documentation, compatibility notes
- **Preservation value**: Modded saves are extremely fragile across updates — versioned snapshots are critical

### 1.6 Original Projects

Custom-built worlds with design documentation, created specifically for this archive. These are the flagship entries that distinguish this project from a download folder.

- **Examples**: Astral Forge Vault, purpose-built educational worlds, technical demonstrations
- **What to look for**: Design intent documentation, build logs, paired characters, reproducible methodology
- **Preservation value**: These *are* the archive's identity — unique content that exists nowhere else

---

## 2. Quality Tiers

Not every save belongs in the archive. These tiers define curatorial standards.

### Tier S — Iconic

Saves that are widely recognized in the Terraria community or represent the definitive version of their category.

- Known by name across the community (e.g., Builder's Workshop)
- Actively maintained or historically significant
- Complete or near-complete in their scope
- Sets the standard others are measured against

### Tier A — Exceptional

High-quality saves with a unique concept, strong execution, and clear purpose.

- Well-organized and intentionally designed
- Offers something not found in other archived saves
- Documented (even minimally — signs, README, forum post)
- Stable and functional on its target version

### Tier B — Solid Reference

Useful saves that serve a clear purpose, even if they aren't groundbreaking.

- Functional and complete enough to be useful
- Fills a gap in the archive's coverage
- May lack polish but has clear utility
- Good for learning or quick reference

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Completeness | High | Does it fully deliver on its stated purpose? |
| Uniqueness | High | Does it offer something the archive doesn't already have? |
| Documentation | Medium | Are there signs, READMEs, or companion files explaining the save? |
| Maintenance | Medium | Is it updated for current versions, or is it a historical snapshot? |
| Technical Quality | Medium | Chest organization, wiring correctness, build precision |
| Provenance | Low | Is the source known and credible? |

---

## 3. Expansion Phases

### Phase 1: Foundation (Complete)

**Status**: ✅ Complete as of 2026-05-23

Establish the archive's core infrastructure and initial content.

- [x] Personal save collection organized (44 worlds, 54 players)
- [x] Initial third-party imports (4 public, 7 private-reference)
- [x] First original project (Astral Forge Vault) with paired characters
- [x] Local tooling operational (TEdit, .NET SDK, TerrariaAgentFramework)
- [x] Basic metadata documentation for all existing saves (CATALOG.md + meta.json sidecars)
- [x] Directory structure and naming conventions finalized (docs/naming-conventions.md)
- [x] README and project documentation complete

**Exit criteria met**: Every save in the archive has at minimum a one-line description, version tag, and tier classification.

### Phase 2: Breadth

**Status**: In progress as of 2026-05-23

**Goal**: Cover all six content pillars with at least 2-3 quality imports each.

- [x] All 5 original projects complete (Astral Forge Vault, Biome Encyclopedia, Boss Rush Colosseum, Wiring Masterclass, Starter Academy)
- [x] Per-save .meta.json sidecars for all 4 public imports
- [x] CI workflow operational (catalog check, LFS validation, provenance check)
- [x] Naming conventions and metadata spec documented
- [ ] Identify and import 2-3 adventure/story maps (Tier A or above) — 1 more needed
- [ ] Expand utility world coverage (Builder's Workshop or version snapshots)
- [ ] Import 2-3 notable build showcases from community sources — 2 needed
- [ ] Add challenge/speedrun world setups with documentation — 1 more needed
- [ ] Begin modded archive with Calamity and Thorium endgame saves — 2 needed
- [ ] Document sourcing and licensing for all third-party imports (already met for public imports)

**Exit criteria**: No content pillar has fewer than 2 archived saves. All imports have provenance documentation.

### Phase 3: Depth

**Goal**: Multiple original projects, modded support infrastructure, and version-controlled snapshots.

- [ ] Complete 2-3 additional original projects (see Section 5)
- [ ] Implement version-tagged snapshots (same world archived across Terraria updates)
- [ ] Build modded save infrastructure (mod version pinning, load order files)
- [ ] Automated metadata extraction pipeline operational
- [ ] Visual documentation generated for all Tier S and Tier A saves
- [ ] Save integrity verification automated (hash checks, load testing)
- [ ] Cross-version compatibility matrix documented

**Exit criteria**: Archive contains 3+ original projects with full design docs. Automated tooling covers metadata extraction and integrity checks.

### Phase 4: Community

**Goal**: Open the archive to external contributions with quality controls.

- [ ] Contribution guidelines published (what qualifies, how to submit)
- [ ] Save submission process defined (PR-based or form-based)
- [ ] Quality review checklist for incoming submissions
- [ ] Public catalog/index (searchable, filterable)
- [ ] Showcase page or gallery for Tier S content
- [ ] Licensing framework for original vs. third-party content

**Exit criteria**: At least one external contribution accepted through the defined process. Public index is live and searchable.

---

## 4. Technical Infrastructure Goals

### 4.1 Automated Integrity Checks

- Hash-based verification that saves haven't been corrupted
- Automated "can this world load?" testing against target Terraria versions
- CI pipeline that validates new additions before merge
- Detect missing companion files (characters paired with worlds)

### 4.2 Save Metadata Extraction

Automated extraction of structured data from `.wld` and `.plr` files:

- World name, size (small/medium/large), seed
- Difficulty (classic/expert/master) and special seeds (getfixedboi, etc.)
- NPC count and housing status
- Chest count and item summary statistics
- Sign count and content extraction
- Terraria version the save was last opened in
- Player inventory summary, class loadout, progression flags

**Tooling**: Extend AstralForgeBuilder or build a dedicated `TerrariaSaveAnalyzer` CLI tool using the .NET SDK and known world format specs.

### 4.3 Visual Documentation

- TEdit full-map renders (PNG) for every world
- Annotated screenshots highlighting key areas
- Before/after comparisons for worlds that evolve across versions
- Thumbnail generation for catalog display

### 4.4 Version Compatibility Matrix

**v2.1 status:** Basic catalog-level matrix is implemented in `inventory/CATALOG.md` and `inventory/catalog.json` via `tools/build_catalog.py`. It aggregates metadata-extracted worlds by Terraria version, difficulty, and total chest count. Next step is per-save load testing.

| Save | Created In | Last Tested | 1.4.4.9 | 1.4.5.x | Notes |
|------|-----------|-------------|----------|----------|-------|
| (template row) | v1.4.4.9 | 2025-01 | OK | Untested | — |

- Track which Terraria version each save was created in
- Track which versions it has been confirmed to load in
- Flag saves that are known to break on version upgrade
- Special attention to modded saves (mod version + game version)

### 4.5 Save Restoration Testing

- Automated test: copy save to Terraria save directory, launch, verify no crash
- Validate that paired characters can load into their paired worlds
- Check for missing mod dependencies in modded saves
- Report generation: which saves are healthy, which need attention

---

## 5. Original Project Ideas

These are purpose-built worlds that would be unique to this archive. Each should have a design document, build log, and paired characters where appropriate.

### 5.1 Museum World

> Every placeable block, wall, and furniture item in the game — placed, labeled, and organized.

- Organized by category (blocks, walls, furniture, lighting, crafting stations)
- Every item labeled with a sign (item name, source/craft, ID)
- Sections for paint variants, actuated states, and echo blocks
- Living document — updated with each Terraria content patch
- **Estimated scale**: Large world, 1000+ signs, months of work

### 5.2 Progression Guide World

> A teaching world designed to walk new players through Terraria's progression from spawn to Moon Lord.

- Zones for each progression stage (pre-boss, pre-hardmode, mech bosses, etc.)
- Each zone contains: recommended gear, arena setup, NPC housing, farm designs
- Sign-based explanations at every station
- Paired characters at each progression checkpoint
- **Estimated scale**: Large world, 5-8 paired characters, extensive sign documentation

### 5.3 Wiring Showcase

> Complex wire mechanisms demonstrated, documented, and deconstructable.

- Teleporter networks, trap systems, automated farms
- Logic gate demonstrations (AND, OR, XOR, timers, sensors)
- Practical applications: boss arenas with toggle-able traps, automated event farms
- Each mechanism isolated and labeled for study
- **Estimated scale**: Medium/Large world, heavy use of actuators and logic gates

### 5.4 Biome Encyclopedia

> Every biome (natural and artificial) constructed with documentation on requirements and mechanics.

- Natural biomes recreated artificially with minimum block counts documented
- Biome-specific NPC housing, enemy spawns, and loot tables noted
- Pylon network demonstrating biome placement strategies
- Edge cases documented (biome blending, priority rules, underground vs. surface)
- **Estimated scale**: Large world, systematic layout, reference-heavy

### 5.5 PvP Arena Collection

> Multiple balanced PvP maps in a single world, designed for different team sizes and rulesets.

- 1v1, 2v2, and FFA arenas with distinct layouts
- Class-balanced loadout chests at each arena
- Wired start gates, score tracking (where possible), and reset mechanisms
- Rule signs and suggested loadouts for each arena type
- **Estimated scale**: Large world, heavy wiring, multiple paired characters with preset loadouts

---

## 6. Success Metrics

How to know the archive is achieving "top-tier" status:

| Metric | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|--------|---------|---------|---------|---------|
| Total archived worlds | 75+ | 90+ | 110+ | 130+ |
| Content pillars covered | 3/6 | 6/6 | 6/6 | 6/6 |
| Original projects | 1 | 1 | 3-4 | 5+ |
| Saves with full metadata | 10% | 50% | 90% | 100% |
| Saves with visual docs | 5% | 30% | 70% | 90% |
| Automated checks passing | — | Basic | Full | Full + CI |

---

## 7. Principles

1. **Preservation over accumulation** — A smaller, well-documented archive beats a massive dump of unlabeled files.
2. **Originals are the differentiator** — Anyone can download Builder's Workshop. Original projects with design docs are what make this archive unique.
3. **Version awareness** — Terraria updates break saves. Version tagging and compatibility tracking are non-negotiable.
4. **Documentation is content** — A world without context is just bytes. Signs, READMEs, metadata, and renders turn saves into knowledge.
5. **Engineering standards apply** — Integrity checks, automated testing, structured metadata, and reproducible processes. This is a software project that happens to contain game saves.
