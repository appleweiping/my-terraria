# CLAUDE.md

You are working on a Terraria save archive project. Read AGENTS.md for full governance rules.

## Critical Rules (always apply)

1. NEVER delete existing save files (.wld, .plr, .map, .bak) without explicit user approval
2. ALL binary saves must be tracked with Git LFS
3. NEVER push third-party saves with unclear redistribution rights to this public repo
4. Every imported save needs full provenance (source URL, author, license, hash, date)
5. Original saves must meet the acceptance bar in AGENTS.md — no toy/demo work

## Quick Reference

- Project root: D:\Terraria_doc
- GitHub: https://github.com/appleweiping/my-terraria (public)
- Binary saves: use Git LFS (configured in .gitattributes)
- Private imports: private-imports/ (gitignored, local only)
- Tooling: .work/ (gitignored) — contains .NET SDK, TEdit, AstralForgeBuilder
- Current phase: Phase 2 (Breadth)

## Before Committing

- Run `git lfs status` to verify LFS tracking
- Scope commits by concern (docs, imports, originals, inventory)
- Write clear commit messages in English
- Do not force-push or rewrite history

## File Conventions

- Documentation: Markdown, English
- Provenance records: external-sources/*.md
- Inventory: inventory/*.csv and inventory/*.md
- Original project docs: originals/<project-name>/README.md, design.md, acceptance-checklist.md
