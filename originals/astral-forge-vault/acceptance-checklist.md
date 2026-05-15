# Astral Forge Vault Acceptance Checklist

Do not mark this original save as complete until these checks pass.

## Binary Save Presence

- [x] `Astral_Forge_Vault.wld` exists and is readable/writable through TEdit's world library.
- [x] Pre-upgrade backup exists as `Astral_Forge_Vault.wld.pre-ultimate.bak`.
- [ ] Optional matching `.map` cache exists for at least one curator/test character.
- [ ] Any matching `.plr` files exist and open in Terraria.

## World Standard

- [x] Spawn hub / aerial command center exists from the first builder pass.
- [x] Storage vault exists with named functional chests.
- [ ] Crafting stations cover normal, hardmode, and endgame crafting.
- [x] Class sanctum area exists for melee, ranger, mage, summoner, and hybrid loadouts.
- [x] Universal proving-ground arena exists.
- [x] Farm matrix scaffold exists.
- [x] Transit spine exists around the hub.
- [ ] Signs or in-world labels make the map self-explanatory. The first builder pass attempted sign entities, but they did not survive validation; implement with valid sign tiles/entities in a later pass.
- [ ] The world still has personality and exploration value.

## Archive Standard

- [x] Source/design notes are updated.
- [ ] Inventory includes the world and any paired players.
- [x] SHA-256 hashes are recorded in `inventory/expansion-log.md`.
- [ ] Git LFS tracks all binary save files.
- [ ] Commit message distinguishes generated base, handcrafted additions, imported additions, and finished release.
