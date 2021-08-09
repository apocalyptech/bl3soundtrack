Borderlands 3: The Extras (unofficial)
======================================

This is some info about an "extras" soundtrack that I'd put together for my
own purposes, and how you'd go about constructing it yourself, given an
extract of the game audio data.

This soundtrack was basically intended to include all extra relevant
"orchestral" soundtrack type music present in the game which doesn't appear on
the official soundtracks.  This excludes Crimson Radio tracks, tracks that
appear in the intro/credits sequences, and a few other bits and bobs, but it
otherwise fills out the official soundtracks quite nicely.

While putting it together I was surprised by the amount of licensed music
that was left in the game -- I'd been assuming that the majority of the
instrumental tracks left soundtrackless would've been written by the various
BL3 composers, but in the end, 11 of the 39 tracks in this soundtrack were
licensed from external composers.

For those licensed tracks, the on-disk extracted audio is often processed
to sound like it's coming out of low-quality speakers, or otherwise be not
very clean.  They'd often be truncated on the on-disk versions, too.  So for
these, I actually just ended up using some browser extensions to download the
low-bitrate "preview" mp3s available at the music-licensing sites where I'd
found the tracks.  Those range from 112-128 kbps, so they're not great, but
it's good enough for my own purposes.  The remainder of the music was taken
directly from the game audio extracts and stitched together using
[vgmstream](https://vgmstream.org/) using custom [TXTP
files](https://github.com/vgmstream/vgmstream/blob/master/doc/TXTP.md).  You
can find those TXTP files in the `custom_txtp` dir in this archive.  You can
also find the other soundtrack-processing scripts I used in the `build_scripts`
dir.

Given that the game's extracted audio contains no tagging information, and
these tracks generally don't seem to be available "officially" online, I had
to make a number of guesses as to who actually wrote/performed the tracks,
based on the zone/map where the music appears, and occasionally just a gut
feel for how the music sounds.  I would be shocked if there weren't a number
of mistakes in this regard throughout the tracklisting.

So, whenever you see a `,possibly` in the Artist name, know that I could
be completely wrong about who wrote it.  The track names for those tracks
have been similarly made up entirely by myself, and are unlikely to match
what the artists themselves would've assigned to the tracks.

One bigger point of contention in terms of information is who wrote the
music for "Act 0," namely the Droughts ambiance/combat music and Mouthpiece's
battle.  Finishing Move Inc. is credited as doing all the Pandora music, but
they generally include "Act 3" in those credits, which wouldn't include these.
The Droughts music had been posted online at Youtube with a few people
expressing great confidence that the Droughts Ambiance track, at least, was
composed by Michael McCann (who did the Promethea/Athenas music on the OST).
The guitar in that track certainly sounds a lot like McCann's Sanctuary
track, and eventually I came around to the idea that McCann might've done the
whole Act 0 score in addition to Promethea/Athenas, rather than Finishing
Move Inc.  Time will tell if I'm right about that, perhaps!

In-Game-Sources
===============

The level-based tracks generally tell you where they're found right in the
titles, but for the licensed tracks especially it might not be clear.

See `non_soundtrack_txtps.txt` out in the main dir for more details on all
these (and other tracks in here).

* **Sandblast Scar Convoy With Vaughn**
  * Christophe Dal Sasso and Dominique Mandin / Shake Up
  * Nigel Thomas / Jazz City
* **Agent Dee's Dance Party in Ambermire**
  * Erik Mikkelsen / Party Night
* **Atlas HQ Muzak + Lectra City Porta-Pooper Muzak**
  * Christopher John White and Peter Denham Dixon / Riviera Retro (60 Sec)
* **Agonizer 9000 Pre-Fight Music Selection**
  * Blood: Paul Whitehead and Emily Taylor / Plasma Storm
  * Fire Skull: Richard Florio and Nick Nolan / Crank
  * Laughing: Robert Edwards / Street Level
* **Krieg's Ska Track From DLC4**
  * Freddie Reid, John Robert Beck, Tim Hutton, and William Arthur / Buster Two Tone (Lite)
* **Sparrow and Grouse Dance Party**
  * Mariano Dimonte, Riccardo Gibertini, Antonio Vezzano, and Marco Zaghi / Little Young Lover
* **Tern's Therapy Session**
  * Suzanne Hansen / Sweet Breaths
* **Claptrap Salvage: Dubstep Library, on Skywell-27**
  * Ilana Tarutina, Jeffrey Fayman, and Yoav Goren / Pink Ferrari

Tracklisting
============

1. Finishing Move Inc., possibly / Agonizer 9000 Commercial Break
  * `Mus_9K_Boss_Start (Mus_Scripted_Motorcade_A9K_Fight=Phase_Commercial_Break)-apoc.txtp`
2. Christophe Dal Sasso and Dominique Mandin / Shake Up
  * https://search.upright-music.com/album/addafcf8-5707-4c88-9fa3-9879d4aa747b
3. Michael McCann, possibly / The Rampager Emerges / Graveward Guardian Fake-Out
  * `Mus_City_Vault_Boss_Play (Mus_Scripted_City_Vault_Boss=Phase_01)-with-Mus_Wetlands_Vault_EdenBoss_Fake_On-apoc.txtp`
4. Finishing Move Inc., possibly / Cartel Infiltration
  * `Mus_Cartels_Run_01_Start (Mus_System_Sections=Mus_Section_01)(Mus_System_Parts=Mus_Part_02)-apoc.txtp`
5. Erik Mikkelsen / Party Night
  * https://bmgmusic.sourceaudio.com/#!details?id=21953807
6. Julian Peterson, possibly / Secrets of Scryer's Crypt
  * `Play_Mus_NekroMystery (Mus_NekroMystery=Cemetery)-apoc.txtp`
7. Finishing Move Inc., possibly / Splinterlands Ambiance
  * `Mus_Motorcade_Start (Mus_System_Sections=Mus_Section_00)-apoc.txtp`
8. Finishing Move Inc., possibly / Splinterlands Combat
  * `Mus_Motorcade_Start (Mus_System_Sections=Mus_Section_01)-apoc.txtp`
9. Michael McCann, possibly / Mouthpiece Meets His End
  * `Mus_Prologue_FinalBoss_Play-apoc.txtp`
10. Christopher White and Peter Dixon / Riviera Retro (60 Sec)
  * https://search.upright-music.dk/album/8e6578d4-0694-4026-94bf-29bec6233c45
11. Raison Varner, possibly / Citizen Science
  * `MUS_CitizenScience (Citizen_Science_MUS=GamePlay) (Citizen_Science_MUS=Attract)-apoc.txtp`
12. Robert Edwards / Street Level
  * https://bmgmusic.sourceaudio.com/#!details?id=24904008
13. Raison Varner / Dark Mix
  * `Mus_Bar_Start (Mus_Hibiscus_Bar=Mus_Bar_DarkMix)-apoc.txtp`
14. Michael McCann, possibly / Killavolt (demo) / The Rave Cave
  * `Mus_Demo_VS_Scripted_Start (Mus_Scripted_VS=Mus_Script_Killavolt_Phase_01)-apoc.txtp`
15. Michael McCann, possibly / Droughts Ambiance
  * `Mus_Prologue_Play (Mus_System_Sections=Mus_Section_01)-apoc.txtp`
16. Raison Varner, possibly / Demo Music (unknown)
  * `Mus_Demo_VS_Start-apoc.txtp`
17. Richard Florio and Nick Nolan / Crank
  * https://bmgmusic.sourceaudio.com/#!details?id=301192
18. Julian Peterson, possibly / Let the Arms Race Begin
  * `Mus_FrostSite_GameShow-apoc.txtp`
19. Jesper Kyd, possibly / Tannis and Splorghuld, Part 4
  * `Mus_Marshfields_Tannis_Egg_Start-apoc.txtp`
20. Freddie Reid, John Robert Beck, Tim Hutton, and William Arthur / Buster Two Tone (Lite)
  * https://bmgmusic.sourceaudio.com/#!details?id=26490746
21. Finishing Move Inc., possibly / Castle Crimson
  * `Mus_Alisma_Anger_Start (Mus_Alisma_Override=on)[Alisma_Mus_System_Combat=-]-apoc.txtp`
22. Michael McCann, possibly / Metroplex - Section 5
  * `Mus_City_Play (Mus_System_Sections=Mus_Section_05)-apoc.txtp`
23. Julian Peterson, possibly / Blastplains Tension
  * `MUS_Frontier_Play-apoc.txtp`
24. Julian Peterson, possibly / Opening the Diamond Armory
  * `Mus_Diamond_Loot_Start (Mus_DLoot=Phase_01)-apoc.txtp`
25. Julian Peterson, possibly / Looting the Diamond Armory
  * `Mus_Diamond_Loot_Start (Mus_DLoot=Phase_02)-apoc.txtp`
26. Mariano Dimonte, Riccardo Gibertini, Antonio Vezzano, and Marco Zaghi / Little Young Lover
  * https://bmgmusic.sourceaudio.com/#!details?id=23332187
27. Finishing Move Inc., possibly / Devil's Razor - Section 2
  * `Mus_Desert_Start (Mus_System_Sections=Mus_Section_02)-apoc.txtp`
28. Finishing Move Inc., possibly / Devil's Razor - Section 3
  * `Mus_Desert_Start (Mus_System_Sections=Mus_Section_02)-apoc.txtp`
29. Julian Peterson, possibly / Gehenna at Sunrise
  * `custom-gehenna-piano-apoc.txtp`
30. Raison Varner, possibly / Rose at Crater's Edge
  * `Mus_Crater_Boss_Start (Mus_Geranium_Crater_Boss=Rose_Fight_Phase_01)-apoc.txtp`
31. Nigel Thomas / Jazz City
  * https://search.upright-music.com/album/a52e5c9f-c463-4ace-83d2-a81614774eae/nojs
32. Raison Varner, possibly / La Cage O' Tinks (Dirty Love)
  * `Mus_Motorcade_Festival_CageOTinks_DirtyLove-apoc.txtp`
33. Jesper Kyd, possibly / Menu (demo)
  * `Mus_Menu-0017-event-apoc.txtp`
34. Paul Whitehead and Emily Taylor / Plasma Storm
  * https://bmgmusic.sourceaudio.com/#!details?id=19811223
35. Suzanne Hansen / Sweet Breaths
  * https://bmgmusic.sourceaudio.com/#!details?id=14831407
36. Raison Varner, possibly / Ashfall Peaks Unease
  * `Mus_Lodge_Start (Mus_System_Sections=Mus_Section_01)(Mus_System_Parts=Mus_Part_00)-apoc.txtp`
37. Michael McCann, possibly / Droughts - Section 2
  * `Mus_Prologue_Play (Mus_System_Sections=Mus_Section_02)-apoc.txtp`
38. Michael McCann, possibly / Droughts - Section 3
  * `Mus_Prologue_Play (Mus_System_Sections=Mus_Section_03)-apoc.txtp`
39. Ilana Tarutina, Jeffrey Fayman, and Yoav Goren / Pink Ferrari
  * https://bmgmusic.sourceaudio.com/#!details?id=23497490

