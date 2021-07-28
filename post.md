# Overview

I've been digging around in the extracted audio files for Borderlands 3, with an eye
to figuring out what songs aren't present in the official soundtracks, and putting
together some extra playlists for my own purposes.  Specifically, practically none of
the songs with lyrics (generally from "real" bands instead of hired composers)
appear on the soundtracks, which means that none of the Crimson Radio tracks are
on there, or the intro cinematic song by The Heavy, or any of the songs that pop up
in the credits.  Also missing are a few in-game tracks like the electroswing track
in VR-0N1CA's construction area, Ellie's "Project DD" playlist in Neon Arterial,
and the track from the Baby Dancer mission.

So, this basically serves as a master list of all those "real-band" songs which
exist in the game, and the raw sound file names that they map to.  Practically all
of this information is available scattered around various places online -- I've not
really done much new investigation work myself.  I do think it's the first time
the authoritative soundfile-to-song mappings have been posted for some of these,
though, so at least there's that, and I believe that this'll be the first time all
this info's been posted in a single location, rather than having it spread out over
a number of sources.

I've attempted to link to online sources for as many of these as possible.  I link
to Bandcamp when possible, though in some cases that's not possible.  I don't generally
link to streaming services since I don't use any of those.  Some tracks, alas, appear
to be entirely unavailable online, though that's most common for what seem like
internal GBX employee tracks.  If I'm missing any links that would be useful, please
let me know and I'll add 'em in!

Data extraction for sound files is [well-known](https://www.reddit.com/r/borderlands3/comments/d6ggya/how_get_audio_files_from_bl3/)
(you could also use the [methods used by the hotfix modding community](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data)).
Once you've got the `.wem` and `.bnk` files extracted, you'll see that they're all
named incomprehensibly with just strings of numbers.  The [wwiser](https://github.com/bnnm/wwiser)
utility, in conjunction with [this BL3 name-mapping file](https://raw.githubusercontent.com/bnnm/wwiser-utils/master/wwnames/Borderlands%203%20%28PC%29.txt)
can be used to associate those files to more human-readable names, which get output
as `.txtp` files, which might end up combining multiple `.wem` files into a single
song/track.  The majority of the songs here just have a single `.wem` file, and you
can convert those to `.ogg` by using [ww2ogg](https://github.com/hcs64/ww2ogg) and
[ReVorb](https://github.com/ItsBranK/ReVorb).  Playing more complex `.txtp` files
can be done with the [vgmstream project](https://vgmstream.org/), which is also
another way to play (or convert) `.wem` files directly.

# Crimson Radio Songs

**Aeternam**

* Fallen is the Simulacrum of Bel
  * `Aeternam_Fallen_Is_The_Simulacrum.txtp`
  * `882622463.wem`
  * https://aeternam.bandcamp.com/track/fallen-is-the-simulacrum-of-bel

**Arure**

Collab. with Raison Varner; the sound cue name / TXTP name groups this
specifically as Raison Varner, in fact.

* Torii (feat. Raison Varner)
  * `Raison_Varner_ARURE_TORII.txtp`
  * `734043784.wem`
  * https://www.toneden.io/arure/post/arure-torii-feat-raison-varner
  * https://arure.bandcamp.com/track/torii-feat-raison-varner
  * https://soundcloud.com/arure/torii-ft-raison-varner

**The Axes of Kane**

Couldn't find any info about these folks other than the member names, from
the game credits: Jeff Davis and Tony Martinez.  Track name's just inferred
from the TXTP filename.

* Bandit Pre-Raid
  * `The_Axes_of_Kane_Bandit_Pre_Raid.txtp`
  * `877343729.wem`

**Blind the Huntsmen**

* Chapter 1 - Khomorrah's Box
  * `BlindTheHuntsmen_Chapter1.txtp`
  * `480354022.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-1-khomorrahs-box
* Chapter 2 - Emanations Of Light And Shadow
  * `BlindTheHuntsmen_Chapter2.txtp`
  * `141374801.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-2-emanations-of-light-and-shadow
* Chapter 3 - Trial Of The Descendants
  * `BlindTheHuntsmen_Chapter3.txtp`
  * `569097410.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-3-trial-of-the-descendants
* Chapter 4 - The Hidden Puppeteer
  * `BlindTheHuntsmen_Chapter4.txtp`
  * `688531743.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-4-the-hidden-puppeteer
* Chapter 5 - Losing The Anchor
  * `BlindTheHuntsmen_Chapter5.txtp`
  * `249779461.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-5-losing-the-anchor
* Chapter 6 - Lost Wanderer
  * `BlindTheHuntsmen_Chapter6.txtp`
  * `907357423.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-6-lost-wanderer
* Chapter 9 - Death And The Shadowshifter
  * `BlindTheHuntsmen_Chapter9.txtp`
  * `732602673.wem`
  * https://blindthehuntsmen.bandcamp.com/track/chapter-9-death-and-the-shadowshifter

**The Capsules**

* Don't Look Down
  * `JShields_DontLookDown.txtp`
  * `524591126.wem`
  * https://saintmarierecords.bandcamp.com/track/dont-look-down
* Our Apocalypse
  * `JShields_OurApocalypse.txtp`
  * `932106601.wem`
  * https://thecapsules.bandcamp.com/track/our-apocalypse
* Super Symmetry
  * `JShields_SuperSymmetry.txtp`
  * `630968841.wem`
  * https://saintmarierecords.bandcamp.com/track/super-symmetry
* The Heartbreaker
  * `JShields_TheHeartbreaker.txtp`
  * `421608513.wem`
  * https://thecapsules.bandcamp.com/track/the-heartbreaker
* The Lonely End
  * `JShields_TheLonelyEnd.txtp`
  * `855688907.wem`
  * https://saintmarierecords.bandcamp.com/track/the-lonely-end

**captainkeytar**

* Potato
  * `RogierVanEtten_PotatoSong.txtp`
  * `518471707.wem`
  * https://captainkeytar.bandcamp.com/track/potato-from-borderlands-3

**Crimson**

* Don't Stop
  * `Crimson_Don_t.txtp`
  * `277697753.wem`
  * https://crimsonrocks.bandcamp.com/track/dont-stop
* Say Goodbye
  * `Crimson_Say_Goodbye.txtp`
  * `754566752.wem`
  * https://crimsonrocks.bandcamp.com/track/say-goodbye
* Tarnished
  * `Crimson_Tarnished.txtp`
  * `1034544128.wem`
  * https://crimsonrocks.bandcamp.com/track/tarnished

**ESC**

* Another way to live
  * `Esc_AnotherWayToLive.txtp`
  * `748431440.wem`
  * https://escmusic2.bandcamp.com/track/another-way-to-live
* Interstellar
  * `Esc_Interstellar.txtp`
  * `277030463.wem`
  * https://escmusic2.bandcamp.com/track/interstellar
* Reclaim my place
  * `Esc_ReclaimMyPlace.txtp`
  * `894025850.wem`
  * https://escmusic2.bandcamp.com/track/reclaim-my-place
* The day I've started to live
  * `Esc_TheDayIveStartedToLive.txtp`
  * `445269085.wem`
  * https://escmusic2.bandcamp.com/track/the-day-ive-started-to-live

**The Five Hands**

I could only find one of these tracks online, from the band's official site.

* Or Else
  * `The_Five_Hands_OrElse.txtp`
  * `552012169.wem`
  * https://thefivehands.com/track/1760318/or-else
* The Wrench
  * `The_Five_Hands_TheWrench.txtp`
  * `254706038.wem`

**Ghosts From Home**

This band's contributed songs to prior Borderlands titles too, though they've
been extremely inactive online since 2014 or so, and I couldn't find any
mention of these tracks anywhere.  Possibly produced specifically for BL3, or
just unreleased music from an album that's not yet released?  Anyway, song
titles are just inferred from those TXTP filenames.  The band does have
various online resources available, at least: [Soundcloud](https://soundcloud.com/ghostsfromhome),
[Bandcamp](https://ghostsfromhome.bandcamp.com/),
[Facebook](https://www.facebook.com/people/Ghosts-From-Home/100057912977726/).

* Dead
  * `GhostsFromHome_Dead.txtp`
  * `165301299.wem`
* Drive
  * `GhostsFromHome_Drive.txtp`
  * `100503335.wem`
* Floods
  * `GhostsFromHome_Floods.txtp`
  * `504893192.wem`
* The Great and Powerful
  * `GhostsFromHome_TheGreatAndPowerful.txtp`
  * `695404200.wem`

**Hillward**

* Long Way Down
  * `Hillward_Long_Way_Down.txtp`
  * `333640814.wem`
  * https://hillward.bandcamp.com/track/long-way-down

**Hunt the Shark**

* 44
  * `HuntTheShark_44.txtp`
  * `25419656.wem`
  * https://huntthesharkmusic.bandcamp.com/track/44
* Dead Youth
  * `HuntTheShark_DeadYouth.txtp`
  * `539756846.wem`
  * https://huntthesharkmusic.bandcamp.com/track/dead-youth-2018

**James Dwyer**

James Dwyer appears to be a GBX employee; this is a silly electronic track
built around the sampled line "Guns that shoot guns."  Title's just inferred
from the TXTP filename and embellished by myself.

* Give Me All Your Guns
  * `James_Dwyer_Give_Me_All.txtp`
  * `533694317.wem`

**Jeremy Neroes**

Jeremy Neroes appears to be a GBX employee as well; he's got a soundcloud
presence and one of these, at least, is available online there.

* Club Rocking
  * `JNeroes_ClubRocking.txtp`
  * `1006961402.wem`
* Destruction at its Finest
  * `JNeroes_DestrutionAtItsFinest.txtp`
  * `884831544.wem`
  * https://soundcloud.com/jeremy-neroes/destrution-at-its-finest

**Jo Drolet**

Credited as "Jonathan Drolet" in the game credits, but public references seem to prefer Jo.
Pretty sure that Jo Drolet was a GBX employee at the time, so these were "internally
generated" tracks.  They don't seem to be available anywhere online anywhere, so the
track names are just assumed from the TXTP filenames.

* What If
  * `Drolet_What_If.txtp`
  * `271517257.wem`
* Worry Free
  * `Drolet_Worry_Free.txtp`
  * `531956279.wem`

**Man Mountain**

* Memory Trace
  * `Man_Mountain_Infinity_Mirror_02.txtp`
  * `552079260.wem`
  * https://manmountain.bandcamp.com/track/memory-trace
* To Be Made as New
  * `Man_Mountain_Infinity_Mirror_04.txtp`
  * `63709818.wem`
  * https://manmountain.bandcamp.com/track/to-be-made-as-new-2

**Matthew Tote**

These tracks are labelled as "Caleb Tote," who appears to possibly be a GBX employee,
though I found 'em online as Matthew Tote instead.

* 8 Analog Light Years EXP
  * `Caleb_Tote_8_analog_light.txtp`
  * `293463833.wem`
  * https://soundcloud.com/matthew-tote/8-analog-light-years-exp?in=matthew-tote/sets/initialize-exp
* Close Encounters JP8 EXP
  * `Caleb_Tote_close_encounters.txtp`
  * `93261593.wem`
  * https://soundcloud.com/matthew-tote/close-encounters-jp8-exp?in=matthew-tote/sets/initialize-exp
* EXS Kaira Dweller EXP
  * `Caleb_Tote_exs_kaira_dweller.txtp`
  * `736515932.wem`
  * https://soundcloud.com/matthew-tote/exs-kaira-dweller-exp?in=matthew-tote/sets/initialize-exp
* Formants EXP
  * `Caleb_Tote_formants_new.txtp`
  * `677539187.wem`
  * https://soundcloud.com/matthew-tote/formants-exp?in=matthew-tote/sets/initialize-exp
* Resonance Anthem EXP
  * `Caleb_Tote_resonance_anthem.txtp`
  * `307960272.wem`
  * https://soundcloud.com/matthew-tote/resonance-anthem-exp?in=matthew-tote/sets/initialize-exp

**Midnight Revel**

* Keep Your Strut
  * `MidnightRevel_KeepYourStrut.txtp`
  * `24344621.wem`
  * https://midnightrevel.bandcamp.com/track/keep-your-strut
* Lay You Steel
  * `MidnightRevel_LayYouSteel.txtp`
  * `1060769871.wem`
  * https://midnightrevel.bandcamp.com/track/lay-you-steel
* Plaeyon Words & Like a Child *(two tracks concatenated into the same file)*
  * `MidnightRevel_PlayeonWordsLikeAChild.txtp`
  * `297201319.wem`
  * https://midnightrevel.bandcamp.com/track/plaeyon-words
  * https://midnightrevel.bandcamp.com/track/like-a-child

**Raison Varner**

Raison Varner's a GBX employee who's been a pretty major contributor to
the symphonic soundtracks of a few Borderlands games, and appears on the
official soundtracks as well.  The track names here are just inferred
from the TXTP titles, and don't appear to be available anywhere online.

* Angry Mouth
  * `Raison_Varner_Angry_Mouth.txtp`
  * `305863583.wem`
  * Pretty silly track built off of some vocal samples
* Cloud Ocean (v2)
  * `Raison_Varner_Cloud_Ocean_v2.txtp`
  * `374180958.wem`
* GBX Ultra Flying Music
  * `Raison_Varner_GBX_Ultra_Flying_Music.txtp`
  * `277140055.wem`
  * Chiptunes!

**Sean Ahern**

Sean Ahern appears to be a GBX employee; many of these are built around sampled
vocals from Borderlands games.  The track names here are just inferred from the
TXTP filenames; they don't appear to be generally available online.

* Chamber Maiden
  * `Sean_Ahern_ChamberMaiden.txtp`
  * `293569682.wem`
* Claptrap Rap
  * `Sean_Ahern_Claptrap_Rap.txtp`
  * `957392246.wem`
* Claptrap's Dubstep Song
  * `Sean_Ahern_ClaptrapsDubstepSong.txtp`
  * `177410924.wem`
* Claptune: The Wall Sphincters
  * `Sean_Ahern_ClapTuneTheWallSphincters.txtp`
  * `1038150521.wem`
* Frostbite
  * `Sean_Ahern_Frostbite.txtp`
  * `752098460.wem`
* Salvador Gets Down
  * `Sean_Ahern_SalvadorGetsDown.txtp`
  * `1065269571.wem`
* Sanctuary (I Think I Might Stay)
  * `Sean_Ahern_Sanctuary_IThinkIMightStay.txtp`
  * `556033462.wem`
* Take Refuge
  * `Sean_Ahern_TakeRefuge.txtp`
  * `195732664.wem`
* The Soothing Sounds
  * `Sean_Ahern_TheSoothingSounds.txtp`
  * `430945332.wem`

**Somewhere Here**

* Don't Panic
  * `Somewhere_Here_The_Tales_1.txtp`
  * `798306680.wem`
  * https://somewherehere.bandcamp.com/track/dont-panic
* Phoenix
  * `Somewhere_Here_The_Tales_2.txtp`
  * `672274232.wem`
  * https://somewherehere.bandcamp.com/track/phoenix

**Wandermine**

No Bandcamp, alas, though the tracks are available on Amazon.

* Chaser
  * `Wandermine_Chaser.txtp`
  * `25638754.wem`
  * https://www.amazon.com/dp/B07KQN89M3/
* Get Out of my Head
  * `Wandermine_GetOutOfMyHead.txtp`
  * `455583834.wem`
  * https://www.amazon.com/dp/B07KQNBM6L/
* Last Round
  * `Wandermine_LastRound.txtp`
  * `496763286.wem`
  * https://www.amazon.com/dp/B07KQPBSP4/
* Monster
  * `Wandermine_Monster.txtp`
  * `947618535.wem`
  * https://www.amazon.com/dp/B07KQNVNCT/
* So High
  * `Wandermine_SoHigh.txtp`
  * `940577846.wem`
  * https://www.amazon.com/dp/B07KQNHXCM/

# Cinematic/Credits Music

Many of these feature a single `.txtp` file which references multiple `.wem`s to
construct the full credits music sequences, though sometimes it's a bit different.

**Intro Cinematic**

* The Heavy / Put It On The Line
  * https://www.amazon.com/Put-Line-Theme-Borderlands/dp/B07WSJTSXZ
  * https://www.youtube.com/watch?v=CdClSNDqCCg
  * Has two in-game data sources, actually.  First:
    * `Map_Prologue-0360-event.txtp`
    * `901675907.wem`
    * This version's properly isolated and doesn't include intro cinematic
      sound effects.  Interesting that the map event is for "Prologue,"
      because that's The Droughts, and I don't think this song ever shows
      up in there.
  * And then second:
    * `Cin_RnRIntro.txtp`
    * `666851330.wem`
    * This is the actual intro cinematic which includes sound effects.
    * The `.wem` file is actually a ten-channel file (five stereo tracks), with
      the music *mostly* isolated into its own stereo track, but there's a lot
      of bleedthrough, so it can't really be properly isolated from this one.

**Base Game Credits**

* `Mus_Credits_GirlOnFire.txtp`
  * Alicia Keys / Girl on Fire
  * `398067457.wem`
  * I'll leave it to the reader to track this one down, since they're a bigger name.
* `Mus_Credits_Section2_Start.txtp`
  * The first `.wem` file in here is about 30 min of "symphonic" official soundtrack stuff.
    The next two are Actual Songs.
  * Cage the Elephant / Trouble
    * `16608304.wem`
    * I'll leave it to the reader to track this one down, since they're a bigger name.
  * Tyreen doing a jazzy scat version of Claptrap's "stealth time!" sequence from Covenant pass
    * `926395753.wem`
    * Not available online that I'm aware of

**DLC1 (Moxxi's Heist of the Handsome Jackpot) End Sequence / Credits**

This is the first place (in this list) that we run into some tracks from the
[Beat Swing](https://anonymousrecordings.com/music/beat-swing/) series of albums,
which seem to be geared specifically at licensing for remixes and inclusion in
media like video games?  They're made by someone who's alternately credited as
"Mr.Edwardz" or just "Robert Edwards".  I'll use the latter for crediting here.
There's the original version of that, but then also a whole series of remix
versions.

* Caleb Hawley / Wish You Were Mine
  * `Video_Epilogue.txtp`
  * `929106243.wem`
  * The datafile (and the cinematic it's related to) only have a pretty tiny
    snippet of the song.
  * https://www.amazon.com/Wish-Were-Mine-Caleb-Hawley/dp/B01IX0VQRY
  * https://www.youtube.com/watch?v=l4dx_YHjcDo
* `Dandelion_Credits_Music_Start.txtp`
  * `298785046.wem`
  * Contains a few tracks concatenated into a single `.wem`:
    * Robert Edwards & Andrew Griffiths / Feathers
      * https://anonymousrecordings.com/music/beat-swing/
    * Robert Edwards ft. Little Violet / Puppet on a String
      * https://www.amazon.com/Beat-Swing-Remixd-Robert-Edwards/dp/B07PVC7GSY
    * Dave Cleveland, Scott Dente, Ken Lewis, and Blair Masters / Slap Bracelet
      * https://search.upright-music.dk/album/df3604c8-06d7-4afb-b661-ccdc0fbc8943

**DLC2 (Guns, Love, and Tentacles) Credits**

* `End_Credits_Music_Hibiscus_Start.txtp`
  * X-Ray Dog / Faster Than the Man
    * `1050394917.wem`
    * https://www.amazon.com/dp/B07HYGYFBH/
  * X-Ray Dog / Fighter
    * `132660270.wem`
    * https://www.amazon.com/dp/B07HYGDPGC/
  * X-Ray Dog / Freaks and Superpowers
    * `594656018.wem`
    * https://www.amazon.com/dp/B07HYGP4M7/
  * X-Ray Dog / Want It All
    * `421893270.wem`
    * https://www.amazon.com/dp/B07HYHRTNC/
  * X-Ray Dog / I Want to Be Loved (Epic Version)
    * `464924712.wem`
    * https://www.amazon.com/dp/B07HYJ29XW/

**DLC3 (Bounty of Blood) Credits**

* `Mus_Ger_EndCredits_Start.txtp`
  * The first two `.wem` files in here are just "symphonic" soundtrack stuff
  * Then there is: Matt Cox And Jerry Jewell / When The Hunter Comes To Town
    * This is split between *nine* `.wem` files; the first eight are various
      bits of the vocals, whereas the last is the instrumental:
      * `221977428.wem`
      * `259647013.wem`
      * `323814835.wem`
      * `505085173.wem`
      * `517076406.wem`
      * `529933439.wem`
      * `558059219.wem`
      * `822332084.wem`
      * `831884463.wem`
    * This track is actually available from the official Bounty of Blood
      soundtrack, though weirdly *not* from the Amazon mp3-download version.
      The [Juno Download](https://www.junodownload.com/products/julian-peterson-borderlands-3-bounty-of-blood/4653410-02/)
      version has it, though.

**DLC4 (Psycho Krieg and the Fantastic Fustercluck) Credits**

* `Mus_Alisma_EndCredits_Start.txtp`
  * The first four `.wem` files in here are just "symphonic" soundtrack stuff
  * Then: The Creepshow / Blood Blood Blood
    * `1032722956.wem`
    * https://thecreepshow.bandcamp.com/track/blood-blood-blood

# Other Songs

**Ellie's "Project DD" Playlist**

This is the sequence with Maya, driving a Technical through Neon Arterial on your
way to The Rampager.  There's a single TXTP file which references four `.wem`s.

* `Mus_City_Vault_Car_Radio_Start.txtp`
  * Animal Fiction / Hold On
    * `729069572.wem`
    * https://music.apple.com/us/album/oh-no-ep/1360250123
  * Sazz / Animal
    * `59606564.wem`
    * I can find nothing about this band, but this track is found on this one music licensing site:
    * https://search.upright-music.dk/album/8dcedb7b-7974-4d62-bb64-3290c3b08843/nojs
  * Parry Music / Push it Home
    * `99398359.wem`
    * https://www.youtube.com/watch?v=KSR7rLXs5FA
  * Animal Fiction / Explosions
    * `823080097.wem`
    * https://music.apple.com/us/album/oh-no-ep/1360250123

**Claptrap + VR-0N1CA Dance**

This is the song you can trigger in the closet on Sanctuary where Claptrap is
repairing Veronica.  I think it's supposed to trigger somewhat late in the process,
but the only time I've ever seen the button work is *before* you do much Veronica
repairing at all.  Weird.  Anyway, the full song spans a couple of TXTPs, and a
couple of `.wem`s.  It's another track from that "Beat Swing" series of albums that
were first mentioned up in the DLC1 credits section above.

* Robert Edwards ft. Little Violet / PiSk Swing
  * `Mus_Sanctuary_Claptrap_Dance_Start (1754084250=2352536306).txtp`
    * `739128134.wem`
  * `Mus_Sanctuary_Claptrap_Dance_Start (1754084250=Obj_Lock2_ObjVat).txtp`
    * `384558352.wem`
  * https://anonymousrecordings.com/remixes/
  * https://www.amazon.com/Beat-Swing-Remixd-Robert-Edwards/dp/B07PVC7GSY
  * Remix of "Charleston Boogie" from the original Beat Swing album, by
    [PiSk](http://www.freshlysqueezedmusic.com/artist/pisk/)

**Baby Dancer**

This is the track from the base game side quest mission Baby Dancer.  It's split
up between multiple `.txtp` files, and multiple `.wem` files as well, so it'd be
difficult to stitch together properly without vgmstream and probably some TXTP
editing.  Regardless:

* Max R. / Do It Like a Superstar! (unknown mix)
  * This particular mix doesn't seem to be available anywhere online.  Made
    specifically for BL3, perhaps?
    * https://www.youtube.com/watch?v=FZu92frZR5k
    * https://soundcloud.com/maxrofficial/max-r-do-it-like-a-superstar-radio-mix
  * `Mus_Baby_Dancer_Play (248720184=436230322).txtp`
    * `14961495.wem`
    * `209203382.wem`
  * `Mus_Baby_Dancer_Play (248720184=602319225).txtp`
    * `492686768.wem`
  * `Mus_Baby_Dancer_Play (248720184=GrenadeLauncher_Reload_CONFI4).txtp`
    * `355525866.wem`
    * `160810524.wem`

**DLC1: Steel Dragon of Eternal Pain**

This is the metalhead who gets annoyed by Digby Vermouth recording his new track,
in that sidequest in the DLC.  The `.wem` files here are only really a snippet of
the full track.

* Aeternam / Praetor of Mercury
  * `MUS_SteelDragonOfEternalPain.txtp`
  * `458969297.wem`
  * `98249060.wem`
  * https://aeternam.bandcamp.com/track/praetor-of-mercury

# Other Info

This post's markdown is also available [at github](https://github.com/apocalyptech/bl3soundtrackpost/blob/main/post.md).
This data's hereby put this under public domain, or
[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
Enjoy!

