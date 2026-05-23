# Project Context

## Current State (as of 2026-05-23)

| Metric | Value |
|--------|-------|
| Personal worlds | 44 |
| Personal players | 54 |
| Public third-party imports | 5 (+ 1 pending download: A Link to Terraria) |
| Private-only third-party saves | 15 worlds + 10 players (private-imports/) |
| Original projects | 5 (Astral Forge Vault, Biome Encyclopedia, Boss Rush Colosseum, Wiring Masterclass, Starter Academy) |
| Paired characters | 17 (across all original projects) |
| Total tracked binary files | ~330+ (wld+plr+bak+map) |
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
- All 5 original projects complete (Boss Rush Colosseum, Wiring Masterclass, Starter Academy: done)
- Improve documentation to top-tier level: naming conventions + metadata spec added

## Original Project Status

| Project | World | Characters | Construction | QA |
|---------|-------|-----------|-------------|-----|
| Astral Forge Vault | ✅ | ✅ 5 chars | ✅ Complete | ✅ |
| Biome Encyclopedia | ✅ | ✅ 2 chars | ✅ Complete | ✅ |
| Boss Rush Colosseum | ✅ | ✅ 5 chars | ✅ Complete | ✅ |
| Wiring Masterclass | ✅ | ✅ 2 chars | ✅ Complete | ✅ |
| Starter Academy | ✅ | ✅ 3 chars | ✅ Complete | ✅ |

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
- Download A Link to Terraria .wld from CurseForge (AGPLv3, 288K downloads) — provenance + meta.json ready
- Contact KhaiosLive (Khaiostomization, 203K downloads) for Pillar 3 build showcase permission
- Contact juicebox1023 (THE KINGDOM, 99K downloads) for Pillar 3 build showcase permission
- Verify Shimmering Skies BSD license variant on CurseForge

### Medium Priority
- Create original Calamity endgame world for Pillar 5 (no open-license community saves exist)
- Add pathfinding to TerrariaGameAgent
- Expand TerrariaAgentMod with building pattern templates
- Generate TEdit full-map renders for Tier S/A saves

### Infrastructure
- Add load-testing step to CI
- Run WorldMetadataExtractor to refresh catalog.json

## Domain Language

- "Save" = a .wld (world) or .plr (player) file
- "Import" = bringing an external third-party save into the archive
- "Original" = a save we design and build ourselves
- "Provenance" = source URL, author, license, hash, retrieval date
- "Restore" = copying saves into Terraria's live game folder
- "Paired characters" = .plr files designed to go with a specific world
- "Sidecar" = .meta.json file alongside a save with structured metadata