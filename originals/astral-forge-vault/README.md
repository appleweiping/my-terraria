# Astral Forge Vault

`Astral Forge Vault` is the first original save project in this archive.

It is not meant to be a toy all-item dump. The target is a complete, high-density, creative master save: a playable vault-world that combines endgame utility, build artistry, boss/event infrastructure, and curated class progression.

## Current Status

- Status: complete programmatic ultimate-map release v1.0.
- World file target: `originals/astral-forge-vault/Astral_Forge_Vault.wld`
- Game target: vanilla Terraria 1.4.x.
- Generated base: large master world using the `getfixedboi` seed, because the project should start from a hard, distinctive, all-secret-seed canvas rather than a plain random map.
- Generation method: Steam Terraria `TerrariaServer.exe` with `serverconfig.txt`.
- Upgrade method: TEdit world library builder passes that add an aerial command hub, vault library, crafting core, class sanctums, proving-ground arena, farm matrix, transit spine, valid sign tiles/entities, named chests, and starter inventory caches.

This release satisfies the repository checklist. Future improvements can still make it more beautiful or richer, but it is no longer a toy/base save.

## Design Thesis

Build a world that feels like an endgame command center and a curated museum at the same time:

- a central astral-forge hub
- complete storage/crafting backbone
- class wings for melee, ranger, mage, summoner, and hybrid loadouts
- boss/event proving grounds
- farms for potion ingredients, money, mobs, and biome materials
- transit network that makes the whole world legible
- preservation of exploration and challenge instead of flattening the world into a dull warehouse

## Files

- `design.md` - creative specification and build plan.
- `acceptance-checklist.md` - non-toy completion criteria.
- `serverconfig.txt` - reproducible seed-world generation config.
- `Astral_Forge_Vault.wld` - current upgraded world.
- `Astral_Forge_Vault.wld.pre-ultimate.bak` - backup of the generated seed world before the first ultimate-map builder pass.
- `Players/` - five paired class/utility characters.
