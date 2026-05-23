# Project Context

## Current State (as of 2026-05-23)

| Metric | Value |
|--------|-------|
| Personal worlds | 72 |
| Personal players | 91 |
| Public third-party imports | 4 |
| Private-only third-party saves | 7 |
| Original projects | 5 (Astral Forge Vault, Biome Encyclopedia, Boss Rush Colosseum, Wiring Masterclass, Starter Academy) |
| Paired characters | 17 (across all original projects) |
| Total tracked binary files | ~320+ |
| Git LFS | Active for .wld, .plr, .map, .bak |
| GitHub | https://github.com/appleweiping/my-terraria (public) |
| Framework | TerrariaAgentFramework v2.1 (world/character generation + deterministic catalog tooling) |
| Game Agent | TerrariaGameAgent (network protocol bot, compiles and runs) |
| Mod | TerrariaAgentMod (tModLoader, awaiting SDK build) |
| CI | .github/workflows/ci.yml — catalog check, LFS pointer validation, provenance check |

## Project Phase

Phase 1 — Foundation (COMPLETE as of 2026-05-23)
- Personal save backup: done
- Initial third-party imports with provenance: done
- First original project (Astral Forge Vault): done
- Repository governance (AGENTS.md): done
- Naming conventions documented: done (docs/naming-conventions.md)
- Per-save metadata format specified: done (docs/metadata-spec.md)
- CI workflow: done (.github/workflows/ci.yml)
- README and project documentation: done

Phase 2 — Breadth (IN PROGRESS)
- Expand coverage across all content pillars (6 pillars, currently 3 covered)
- Add automated integrity tooling: catalog/version-matrix generator present (tools/build_catalog.py)
- Create additional original projects (Boss Rush Colosseum, Wiring Masterclass: design complete, construction pending)
- Improve documentation to top-tier level: naming conventions + metadata spec added

## Original Project Status

| Project | World | Characters | Construction | QA |
|---------|-------|-----------|-------------|-----|
| Astral Forge Vault | ✅ | ✅ 5 chars | ✅ Complete | ✅ |
| Biome Encyclopedia | ✅ | ✅ 2 chars | ✅ Complete | ✅ |
| Boss Rush Colosseum | ✅ placeholder | ✅ 5 chars | ❌ Not started | ❌ |
| Wiring Masterclass | ✅ placeholder | ✅ 2 chars | ❌ Not started | ❌ |
| Starter Academy | ✅ | ✅ 3 chars | ✅ Present | ⚠️ QA pending |

## Key Decisions Made

- Repo is PUBLIC: no All-Rights-Reserved binaries in Git
- Git LFS for all binary saves (enforced via .gitattributes)
- Private imports stored locally at private-imports/ (gitignored)
- Original saves must pass acceptance checklist, no toy/demo work
- SHA-256 provenance required for every import
- Naming conventions: kebab-case dirs, Title Case save files, date-prefixed research logs
- Per-save metadata: .meta.json sidecar format (docs/metadata-spec.md)

## Next Actions (Agent Task Pool)

### High Priority
- Build Boss Rush Colosseum world (90-item acceptance checklist, all arenas)
- Build Wiring Masterclass world (80-item acceptance checklist, 6 sections)
- Complete Starter Academy QA readback and in-game walkthrough

### Medium Priority
- Import 2-3 adventure/story maps with compatible licenses (research done in external-sources/2026-05-18-adventure-map-research.md)
- Import 2-3 build showcases from community sources
- Add challenge/speedrun world setups
- Begin modded archive (Calamity, Thorium endgame saves)

### Infrastructure
- Add per-save .meta.json sidecars for all public imports and originals
- Implement save metadata extraction pipeline (TerrariaSaveAnalyzer CLI)
- Generate TEdit full-map renders for Tier S/A saves
- Add load-testing step to CI

## Domain Language

- "Save" = a .wld (world) or .plr (player) file
- "Import" = bringing an external third-party save into the archive
- "Original" = a save we design and build ourselves
- "Provenance" = source URL, author, license, hash, retrieval date
- "Restore" = copying saves into Terraria's live game folder
- "Paired characters" = .plr files designed to go with a specific world
- "Sidecar" = .meta.json file alongside a save with structured metadata