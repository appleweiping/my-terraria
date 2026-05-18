# AGENTS.md

This repository is a long-term Terraria save archive. Agents working here should behave like disciplined archivists and ambitious Terraria save curators, not generic file movers.

## Mission

Maintain a high-quality, source-traceable Terraria save library containing:

- backed-up local saves
- imported external worlds/characters, with public/private handling based on provenance and redistribution risk
- original save projects designed to be complete, distinctive, and actually useful

The user explicitly rejects toy/demo saves. Do not create placeholder work and pretend it is complete.

## Repository Layout

- `Terraria_saves/`
  - Canonical archived save files.
  - Binary save files are tracked with Git LFS.
- `inventory/`
  - File inventories, hashes, sorting notes, and restoration guidance.
- `external-sources/`
  - Research notes, source candidates, provenance records, and import decisions.
- `private-imports/` or local-only paths outside Git
  - Use for private backup of high-quality third-party saves whose redistribution rights are unclear.
  - Do not push private-imported third-party binaries to public GitHub unless permission/license is clear.
- `originals/`
  - Original save concepts, world-generation configs, design specs, validation checklists, and generated seed worlds.

## External Save Import Policy

When the user asks to expand the archive by importing saves from other people:

1. Search broadly first.
   - Start with GitHub, but do not force GitHub-only results if the best Terraria saves live elsewhere.
   - Also inspect reputable Terraria distribution surfaces such as CurseForge, Steam Workshop pages, official forum threads, and well-known map pages.
2. Prefer high-signal candidates.
   - Evidence of quality includes downloads, update recency, community reputation, screenshots/video, changelog quality, completeness, and clear install instructions.
   - Prefer saves that are meaningfully different from this archive: adventure maps, polished all-item/storage systems, arenas, farms, challenge worlds, class-ready characters, modded total-conversion saves, or unusually strong builds.
3. Respect provenance and choose the right storage surface.
   - If a source is high-quality, novel, and popular but has unclear redistribution terms, you may create a local/private backup for the user with full provenance and hashes.
   - Do not push third-party binary saves with unclear redistribution rights to the public GitHub repo unless the user explicitly confirms this repository should be treated as private or permission/license is clear.
   - If the repo is public and permission is unclear, commit source notes and install instructions, not the third-party binary files.
   - Keep a provenance note for every imported save: source URL, author, version, license/permission status, retrieval date, expected Terraria/tModLoader version, included files, and reason for inclusion.
4. Match complete save sets.
   - Preserve associated `.wld`, `.plr`, `.map`, `.bak`, `.twld`, `.tplr`, mod lists, readmes, and install notes when they belong together.
   - Do not split a curated external save set unless the source itself separates it cleanly.
5. Validate after import.
   - Check file counts, sizes, hashes, Git LFS tracking, and whether the files are in the expected `Players` / `Worlds` restore locations.
   - Add or update inventory notes and commit in scoped batches.

## Original Save Creation Policy

When creating original saves, the bar is high:

- No toy worlds, empty shells, or "proof of concept" saves presented as final.
- Do not stop at a generated seed/base world. A generated base is only a staging point; continue toward a finished ultimate map.
- A credible original save must have a thesis, world/character role, progression path, storage/utility plan, build plan, biome/farm/arena coverage, and acceptance tests.
- Distinctiveness matters. Do not merely clone Builder's Workshop, a generic all-item map, or a random generated world.
- A generated vanilla world can be committed as a seed/base world only as an intermediate commit, not as the endpoint.
- If a fully completed `.wld` or `.plr` cannot be generated programmatically in the current environment, still push the save as far as the tools allow and record exactly what remains. Do not use tool limits as an excuse to stop at a toy stage.
- For a finished original save, aim for:
  - all major biomes accessible
  - clean spawn hub
  - storage and crafting system
  - class loadout rooms
  - boss/event arenas
  - potion/material farms
  - NPC housing plan
  - transport network
  - clear restore/install notes
  - matching characters where useful

## Commit Policy

- Keep commits scoped by concern: docs/protocols, external-source research, imported players, imported worlds, original projects, inventory updates.
- Push after each coherent batch when network/auth works.
- Do not remove existing saves unless the user explicitly approves deletion.
- Preserve binary saves with Git LFS.

## Handoff Protocol

When multiple agents work on this repository (sequentially or in parallel), follow these coordination rules:

### Research → Import → Verify Pipeline

1. **Research agent** produces:
   - A markdown file in `external-sources/` with candidate list
   - Each candidate has: name, source URL, author, license, category, quality signals, download link (if public), and import recommendation (public/private/skip)
   - File naming: `external-sources/YYYY-MM-DD-<source-name>.md`

2. **Import agent** consumes the research file and:
   - Downloads recommended candidates
   - Computes SHA-256 hashes
   - Places files in correct location (imported/ for public, private-imports/ for restricted)
   - Creates per-import `THIRD_PARTY_NOTICE.md`
   - Updates `inventory/terraria-file-inventory.csv`
   - Commits with message format: `Import <category>: <save-name> from <source>`

3. **Verify agent** runs after import and:
   - Checks all .wld/.plr files are LFS-tracked (`git lfs ls-files`)
   - Validates SHA-256 hashes against provenance records
   - Confirms file sizes are reasonable (not zero-byte or truncated)
   - Updates `inventory/expansion-log.md`
   - Reports any discrepancies

### Original Project Pipeline

1. **Design agent** produces:
   - `originals/<project-name>/design.md` — concept, thesis, feature list
   - `originals/<project-name>/acceptance-checklist.md` — measurable completion criteria

2. **Build agent** executes:
   - Generates or modifies .wld/.plr files using available tooling
   - Records build steps and intermediate hashes
   - Commits working state with message: `WIP: <project-name> — <description>`

3. **QA agent** validates:
   - Reads back the .wld file to verify title, spawn, chest count, sign count
   - Checks acceptance-checklist.md items
   - Commits final state with message: `Complete <project-name> v<version>`

### Handoff Document Format

When an agent cannot complete its work in one session, it must leave a handoff note:

```
File: .work/handoff/<YYYY-MM-DD>-<task>.md

# Handoff: <task description>

## Completed
- [x] item 1
- [x] item 2

## Remaining
- [ ] item 3
- [ ] item 4

## Blockers
- description of any blockers

## Context
- key decisions made
- files modified
- next agent should start by...
```

### Conflict Avoidance

- Agents working in parallel must claim non-overlapping directories
- Research agents: only write to external-sources/
- Import agents: only write to Terraria_saves/imported/ and inventory/
- Original project agents: only write to originals/<their-project>/
- Documentation agents: only write to docs/ and root markdown files
- Never modify another agent's in-progress work without explicit coordination
