Borderlands 3: Crimson Radio (unofficial)
=========================================

This soundtrack was put together in a super straightforward way; nothing
fancy at all.  All the tracks here were just converted from the original
extracted `.wem` files to `.ogg` using [ww2ogg](https://github.com/hcs64/ww2ogg)
and [ReVorb](https://github.com/ItsBranK/ReVorb), tagged using my usual
tagging apps, and had [vorbisgain](https://sjeng.org/vorbisgain.html)
run on top, to add [ReplayGain](https://en.wikipedia.org/wiki/ReplayGain)
tags to the files, which does volume normalization without having to do
lossy re-encodes.

There was no attempt whatsoever at sequencing this; it's just in alphabetical
order.  The single script in here reads in `songs.txt` to know which TXTPs
we were interested in, finds the single `.wem` file inside, and then converts
it over into ogg, leaving sequencing/tagging/etc as manual steps.

James Dwyer's "Give Me All Your Guns" has a lot of silence after the main song
has finished; I'd recommend using [mp3splt](http://mp3splt.sourceforge.net/mp3splt_page/home.php)
to chop off the silence, using:

    mp3splt filename 0.0 3.52

Tracklist:

1. Aeternam / Fallen is the Simulacrum of Bel
2. Arure / Torii (feat. Raison Varner)
3. The Axes of Kane / Bandit Pre-Raid
4. Blind the Huntsmen / Chapter 1 - Khomorrah's Box
5. Blind the Huntsmen / Chapter 2 - Emanations Of Light And Shadow
6. Blind the Huntsmen / Chapter 3 - Trial Of The Descendants
7. Blind the Huntsmen / Chapter 4 - The Hidden Puppeteer
8. Blind the Huntsmen / Chapter 5 - Losing The Anchor
9. Blind the Huntsmen / Chapter 6 - Lost Wanderer
10. Blind the Huntsmen / Chapter 9 - Death And The Shadowshifter
11. The Capsules / Don't Look Down
12. The Capsules / Our Apocalypse
13. The Capsules / Super Symmetry
14. The Capsules / The Heartbreaker
15. The Capsules / The Lonely End
16. captainkeytar / Potato
17. Crimson / Don't Stop
18. Crimson / Say Goodbye
19. Crimson / Tarnished
20. ESC / Another way to live
21. ESC / Interstellar
22. ESC / Reclaim my place
23. ESC / The day I've started to live
24. The Five Hands / Or Else
25. The Five Hands / The Wrench
26. Ghosts From Home / Dead
27. Ghosts From Home / Drive
28. Ghosts From Home / Floods
29. Ghosts From Home / The Great and Powerful
30. Hillward / Long Way Down
31. Hunt the Shark / 44
32. Hunt the Shark / Dead Youth
33. James Dwyer / Give Me All Your Guns
34. Jeremy Neroes / Club Rocking
35. Jeremy Neroes / Destruction at its Finest
36. Jo Drolet / What If
37. Jo Drolet / Worry Free
38. Man Mountain / Memory Trace
39. Man Mountain / To Be Made as New
40. Matthew Tote / 8 Analog Light Years EXP
41. Matthew Tote / Close Encounters JP8 EXP
42. Matthew Tote / EXS Kaira Dweller EXP
43. Matthew Tote / Formants EXP
44. Matthew Tote / Resonance Anthem EXP
45. Midnight Revel / Keep Your Strut
46. Midnight Revel / Lay You Steel
47. Midnight Revel / Plaeyon Words + Like a Child
48. Raison Varner / Angry Mouth
49. Raison Varner / Cloud Ocean (v2)
50. Raison Varner / GBX Ultra Flying Music
51. Sean Ahern / Chamber Maiden
52. Sean Ahern / Claptrap Rap
53. Sean Ahern / Claptrap's Dubstep Song
54. Sean Ahern / Claptune: The Wall Sphincters
55. Sean Ahern / Frostbite
56. Sean Ahern / Salvador Gets Down
57. Sean Ahern / Sanctuary (I Think I Might Stay)
58. Sean Ahern / Take Refuge
59. Sean Ahern / The Soothing Sounds
60. Somewhere Here / Don't Panic
61. Somewhere Here / Phoenix
62. Wandermine / Chaser
63. Wandermine / Get Out of my Head
64. Wandermine / Last Round
65. Wandermine / Monster
66. Wandermine / So High

