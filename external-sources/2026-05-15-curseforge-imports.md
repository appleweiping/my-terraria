---
title: 2026-05-15 CurseForge Popular Terraria Map Import
type: external-source-batch
status: completed
created: 2026-05-15
updated: 2026-05-15
tags:
  - terraria
  - curseforge
  - external-import
  - private-backup
---

# 2026-05-15 CurseForge Popular Terraria Map Import

This batch backs up high-signal Terraria maps from CurseForge into the local archive and separates public redistribution from private-only preservation.

## Import Rule Used

- Public GitHub import requires a source-page license or permission that allows redistribution.
- High-quality maps with unclear or restrictive redistribution are backed up under ignored `private-imports/` paths only.
- For every downloaded archive or save file, keep source URL, file id, file name, local path, size, SHA-256, and import decision.
- Do not relicense third-party worlds under this repository's MIT license; keep `THIRD_PARTY_NOTICE.md` beside each public imported save.

## Public Imports

These files were downloaded into `Terraria_saves/imported/` and are suitable for Git LFS tracking because the source pages showed redistribution-compatible licenses.

| Title | Category | Source | Author | File id | Source license observed | Local path | Size | SHA-256 |
|---|---|---|---|---:|---|---|---:|---|
| The Story of Red Cloud | Adventure / RPG world | https://www.curseforge.com/terraria/maps/story-red-cloud | vibrent | 4642678 | Public Domain | `Terraria_saves/imported/story-of-red-cloud/the-story-of-red-cloud.wld` | 7,317,322 | `6201526758b8c1f654972b745cc2b02698bcf5d5d6922eabbca31becc1994706` |
| All Boss Battle Arenas Expert | Boss arena / combat utility | https://www.curseforge.com/terraria/maps/all-boss-battle-arenas | EmberNov | 2831908 | Creative Commons Attribution-NonCommercial 3.0 Unported | `Terraria_saves/imported/all-boss-battle-arenas/All Boss Battle Arenas Expert.wld` | 619,661 | `0d0ffc776229eee8934b98dea2fda779b67f7be9712878d19ed7ef3e04621a12` |
| SUNV XTRA All Items Hub 1.4.5 Master | Compact all-items / storage hub | https://www.curseforge.com/terraria/maps/sunv-xtra-all-items-hub | SUNVxtra | 7834182 | GNU General Public License version 3 (GPLv3) | `Terraria_saves/imported/compact-all-items-hub-master/SUNV-XTRA-All-ITEMS-HUB-1.4.5-Master.wld` | 714,711 | `2bfadc81c0abb8b21e3154df8699bbaf576b0df6c7cee73e842eb63a8adef8b6` |

## Private-Only Backups

These were downloaded to `private-imports/2026-05-15-curseforge/`, which is intentionally ignored by Git. Their source pages are high-value for the archive, but redistribution should not be pushed publicly unless the user confirms private-repo handling or obtains permission.

| Title | Category | Source | Author | File id | Source license observed | Local private path | Size | SHA-256 | Included saves |
|---|---|---|---|---:|---|---|---:|---|---|
| Builder's Workshop | All-items / canonical storage world | https://www.curseforge.com/terraria/maps/builders-workshop | TelBuilds | 3255348 | All Rights Reserved | `private-imports/2026-05-15-curseforge/builders-workshop/Builder4.5.2.zip` | 351,032 | `1b38b27ce945de8af9f1845e688dee9c8f0593c10da3b37d26ccc6e95c5ae6c8` | 4 worlds: Classic, Expert, Master, Journey |
| Ztorage Zystem | All-items / storage system plus matching players | https://www.curseforge.com/terraria/maps/ztorage-zystem | lathemandrel | 7666417 | All Rights Reserved | `private-imports/2026-05-15-curseforge/ztorage-zystem/Ztorage_Zystem!_v14.55.00.zip` | 477,596 | `cdd7d8065f057db8a5f9abb5ee7f0a29ce86b2b505dbaa09687962fe751360b1` | 2 worlds, 10 players |
| The Shimmer Lands | Visual all-item world / shimmer themed hub | https://www.curseforge.com/terraria/maps/the-shimmer-lands-a-new-beautiful-all-item-world | scopeymopey | 4708979 | All Rights Reserved | `private-imports/2026-05-15-curseforge/the-shimmer-lands/The_Shimmer_Lands_ZIP_Right_click_and_extract.zip` | 551,830 | `0b4ab6c779055ee030056c114d161f4de160f04dd4bb741431e7f5eac5d801fd` | 4 worlds: Classic, Expert, Master, Journey |
| Khaiostomization | Building / customization showcase | https://www.curseforge.com/terraria/maps/khaiostomization | KhaiosLive | 2811084 | All Rights Reserved | `private-imports/2026-05-15-curseforge/khaiostomization/Khaiostomization.zip` | 8,564,240 | `2ba27bbc48e20957306e8e2dd25c6355329f32daa3db95295836d2b9f40247e3` | 2 worlds: normal and expert |
| Scopey 1.4.5 All Items | Current-version all-items world | https://www.curseforge.com/terraria/maps/my-1-4-5-all-items-map | Scopey_Mo | 7652609 | All Rights Reserved | `private-imports/2026-05-15-curseforge/scopey-145-all-items/Scopey1.4.5AllItems.wld` | 11,056,320 | `c71f68067893a61bc2e4b7a321e0141858462d76b242a868f520a28d84e71d85` | 1 world |
| Starter World 1.4.4.9 Master | Starter/progression utility world | https://www.curseforge.com/terraria/maps/starterworld | AkoyPinoy03 | 4705752 | All Rights Reserved | `private-imports/2026-05-15-curseforge/starter-world-1449/Starter_World Master.wld` | 6,986,081 | `13da0ffae4895c1ab952081916bd088bae90126bf65c2af8b888c38d5dc2bf4a` | 1 world |
| The Kingdom | Building / settlement world | https://www.curseforge.com/terraria/maps/the-kingdom | juicebox1023 | 2861690 | All Rights Reserved | `private-imports/2026-05-15-curseforge/the-kingdom/Kingdom.wld` | 7,067,986 | `d48ed8e2b3ecc189e2156539990b1e91f61071f8550edbb8aaa715810c73896f` | 1 world |

## Extracted Private File Hashes

| Backup | Extracted file | Size | SHA-256 |
|---|---|---:|---|
| Builder's Workshop | `BuildersWorkshop_0Classic.wld` | 701,336 | `6e432ec416846a1ffa61fdc654005fbac00daf8d677cbae883d6b2f3702848d5` |
| Builder's Workshop | `BuildersWorkshop_1Expert.wld` | 701,336 | `04b97afd142dc65836c294fa54f644408960e46f55312b30fe919395e1ce6472` |
| Builder's Workshop | `BuildersWorkshop_2Master.wld` | 701,336 | `ca4b4a75315d7926502b5caaf6507e53c24825cce4e09ef2b113256273c198c1` |
| Builder's Workshop | `BuildersWorkshop_3Journey.wld` | 701,336 | `8e56fb089f2507c525d844871758e1f9c0f204a5fbb50edfbd8df106b759ef03` |
| Khaiostomization | `Khaiostimozation.wld` | 11,195,605 | `ebcfabfe663280471992e5afee94d566114d62d3f432241036aa661d2bc2ef30` |
| Khaiostomization | `Khaiostomization Expert.wld` | 11,195,975 | `30f84e16e97f8f232369a597b536fc775d98be0b1dd14dd5a7200ea460db57fb` |
| The Shimmer Lands | `The Shimmer Lands (Classic).wld` | 555,465 | `4f19809029e3dbbc9cf593cc67a89b4865e9f022072a4aa2cc38d2849ac47b07` |
| The Shimmer Lands | `The Shimmer Lands (Expert).wld` | 555,465 | `351920418ab181d8c51ad44133fe3542fd4ce2d52b88a235243b5e1ef8f717a3` |
| The Shimmer Lands | `The Shimmer Lands (Journey).wld` | 555,465 | `90a49be3341a83ccd8a81d851e2ccd4774c17cde2a8b9f55752a7ebe7c6e9b16` |
| The Shimmer Lands | `The Shimmer Lands (Master).wld` | 555,465 | `585bf514fb45c069477bc7506f87885feb5d02656f74c512154715a059133f1f` |
| Ztorage Zystem | `Ztorage_Zystem_ZZ_1455.wld` | 3,589,277 | `392a7a591cc5f3ca16cf8948ecd39f7750562cb153e2d78be758853990e51a51` |
| Ztorage Zystem | `Ztorage_Zystem_ZZ_Jr_1455.wld` | 3,589,222 | `24256c2f0a81cdadc6b911968576be285a092103434ddec3bd3b11508d7e74a1` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_F (softcore).plr` | 3,712 | `6be781eba448fd6facbc07ba5504caa6a8829cdc223334d3fa83bb4bc836d113` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_F (mediumcore).plr` | 3,712 | `4c1122b709391bf9e52165701e03bb325c110829aa3db6e9f06cb3a8d901d90e` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_F (hardcore).plr` | 3,712 | `f5fde002272441cbe57eaedab064920cd54d632a3db7340e6874da6868eb7db2` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_M (softcore).plr` | 3,712 | `18b7f03a81f128dae9840da0682123b7b4d178fd59cd2d1c50ff693592033aff` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_M (mediumcore).plr` | 3,712 | `c59774dccb9a42c6b1c4ec73b333d2506f3b77d468eed3562d301ac3fde47e34` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_M (hardcore).plr` | 3,712 | `4866510bc35f8b6447921441517ce0c41504ccc8cde4d6a0271a36acd92f1b71` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_Jr_F (none researched).plr` | 3,712 | `424430d8ec5a7b56d5366281dfc155ace1529105b30c3f8e717432ceb4073fa4` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_JR_F (6091 researched).plr` | 116,368 | `bde7e584cc1875cb87754e248a179fa8beaa2c1813d1d527a77f2fe11c485890` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_Jr_M (none researched).plr` | 3,712 | `25d753f9dff06b7c94358481581cd6fead1bf7fa55f34cc3c89a5ccb0b057b6a` |
| Ztorage Zystem | `Zoh_Good_the_ZZth_JR_M (6091 researched).plr` | 116,368 | `16fc62228e7bb2a3ff62c38f8bb7e32c52c8fde663a4f049131933b044f34d05` |

## Restore Notes

- `.wld` files belong under the Terraria `Worlds` folder.
- `.plr` files belong under the Terraria `Players` folder.
- Keep extracted files beside their original archives for private backups so a future agent can inspect exact save contents without relying on CurseForge availability.
- If the user later confirms the GitHub repository is private-only, private-only backups may be promoted in batches with their original notices preserved.
