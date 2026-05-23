---
title: 2026-05-23 Phase 2 Planning — Content Expansion
type: planning-log
status: active
created: 2026-05-23
updated: 2026-05-23
tags:
  - phase2
  - planning
  - content-pillars
  - imports
  - originals
---

# 2026-05-23 Phase 2 Planning

Phase 1 is now complete. This document records the Phase 2 plan and tracks progress against the six content pillars.

## Phase 1 Completion Summary

All Phase 1 exit criteria are now met:

| Criterion | Status |
|-----------|--------|
| Every save has at minimum a one-line description | ✅ CATALOG.md covers all tracked saves |
| Version tag present | ✅ Version compatibility matrix in CATALOG.md |
| Tier classification | ⚠️ Partial — originals and imports classified, personal saves use 'personal' tier |
| Naming conventions documented | ✅ docs/naming-conventions.md added 2026-05-23 |
| Per-save metadata format specified | ✅ docs/metadata-spec.md added 2026-05-23 |
| CI workflow | ✅ .github/workflows/ci.yml added 2026-05-23 |

## Phase 2 Goals

Cover all six content pillars with at least 2-3 quality imports each.

### Current Pillar Coverage

| Pillar | Current | Target | Gap |
|--------|---------|--------|-----|
| 1. Adventure & Story Maps | 2 (Story of Red Cloud + Remix) | 3+ | +1 needed |
| 2. All-Items & Utility Worlds | 1 (Compact All-Items Hub) | 2+ | +1 needed |
| 3. Build Showcases | 0 | 2+ | +2 needed |
| 4. Challenge & Speedrun | 1 (All Boss Battle Arenas) | 2+ | +1 needed |
| 5. Modded Archives | 0 | 2+ | +2 needed |
| 6. Original Projects | 2 complete (Astral Forge Vault, Biome Encyclopedia) | 3+ | +1 needed |

### Priority Import Candidates

Based on research in `2026-05-18-adventure-map-research.md`:

**Pillar 1 — Adventure/Story (1 more needed)**
- Candidates with confirmed redistribution-compatible licenses are limited
- Focus: GitHub-hosted maps with explicit open licenses
- Avoid: Steam Workshop (non-redistributable), forum posts without explicit permission

**Pillar 2 — All-Items/Utility (1 more needed)**
- Builder's Workshop (official Terraria team release) — check current license status
- Version-specific snapshots of existing imports would count

**Pillar 3 — Build Showcases (2 needed)**
- No candidates identified yet — requires new research pass
- Target: pixel art worlds, megabuilds, or themed cities with open licenses

**Pillar 4 — Challenge/Speedrun (1 more needed)**
- Seeded worlds with documented routes
- Class-locked challenge setups

**Pillar 5 — Modded Archives (2 needed)**
- Calamity endgame world (requires Calamity mod version pinning)
- Thorium progression save
- Key constraint: mod version must be documented alongside game version

**Pillar 6 — Original Projects (1 more needed)**
- Boss Rush Colosseum: design complete, 90-item checklist ready, construction not started
- Wiring Masterclass: design complete, 80-item checklist ready, construction not started
- Either would satisfy the Phase 2 target

## Original Project Construction Priority

The two incomplete originals are the highest-value Phase 2 deliverables because they are unique content that exists nowhere else.

### Boss Rush Colosseum

- **Effort**: Very high (90 checklist items, 15+ arenas, full NPC housing)
- **Blocker**: Requires in-game construction time — cannot be automated without TerrariaAgentFramework integration
- **Next step**: Verify TerrariaAgentFramework can generate the base world structure; manual construction for arena details

### Wiring Masterclass

- **Effort**: High (80 checklist items, 6 sections, complex wiring)
- **Blocker**: Same as above — requires in-game construction
- **Next step**: Journey Mode world generation is simpler; framework can flatten terrain and place hub structure

## Infrastructure Priorities

1. **Per-save .meta.json sidecars** — Add to all 4 public imports first (highest visibility)
2. **CI load-testing** — Add Terraria headless load test to CI once infrastructure is available
3. **TEdit map renders** — Generate PNG renders for Astral Forge Vault and Biome Encyclopedia

## Phase 2 Exit Criteria

- No content pillar has fewer than 2 archived saves
- All imports have provenance documentation (already met)
- At least 3 original projects with full design docs (currently 2 complete + 3 in progress)
- CI passes on every commit
