# AGENTS.md

This repository is a long-term Terraria save archive. Agents working here should behave like disciplined archivists and ambitious Terraria save curators, not generic file movers.

## Mission

Maintain a high-quality, source-traceable Terraria save library containing:

- backed-up local saves
- imported external worlds/characters when licensing and provenance allow
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
3. Respect license and provenance.
   - Do not copy third-party binary saves into this public GitHub repository unless the source license/terms clearly permit redistribution or the user has obtained permission.
   - If a source has no license or unclear redistribution terms, record it as a candidate and provide download/install instructions rather than committing its files.
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
- A credible original save must have a thesis, world/character role, progression path, storage/utility plan, build plan, biome/farm/arena coverage, and acceptance tests.
- Distinctiveness matters. Do not merely clone Builder's Workshop, a generic all-item map, or a random generated world.
- A generated vanilla world can be committed as a seed/base world only when labeled honestly as a seed/base, not as a finished handcrafted save.
- If a fully completed `.wld` or `.plr` cannot be generated programmatically in the current environment, create the full design dossier, configs, and next-action checklist instead of fabricating completion.
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

