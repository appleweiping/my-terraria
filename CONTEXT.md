# Project Context

## Current State (as of 2026-05-21)

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

## Project Phase

Phase 1 — Foundation (COMPLETE)
- Personal save backup: done
- Initial third-party imports with provenance: done
- First original project (Astral Forge Vault): done
- Repository governance (AGENTS.md): done

Phase 2 — Breadth (IN PROGRESS)
- Expand coverage across all content pillars
- Add automated integrity tooling: catalog/version-matrix generator now present (`tools/build_catalog.py`)
- Create second original project
- Improve documentation to top-tier level

## Key Decisions Made

- Repo is PUBLIC: no All-Rights-Reserved binaries in Git
- Git LFS for all binary saves (enforced via .gitattributes)
- Private imports stored locally at private-imports/ (gitignored)
- Original saves must pass acceptance checklist, no toy/demo work
- SHA-256 provenance required for every import

## Next Actions (Agent Task Pool)

- Import more adventure/story maps with compatible licenses
- Import modded (tModLoader) saves if license-compatible sources found
- Design and build second original project
- Add CI workflow for LFS integrity checks
- Extract and document save metadata (version, size, difficulty, NPCs)
- Create visual documentation (TEdit map renders)
- Add CI workflow for `python tools/build_catalog.py --check`

## Domain Language

- "Save" = a .wld (world) or .plr (player) file
- "Import" = bringing an external third-party save into the archive
- "Original" = a save we design and build ourselves
- "Provenance" = source URL, author, license, hash, retrieval date
- "Restore" = copying saves into Terraria's live game folder
- "Paired characters" = .plr files designed to go with a specific world