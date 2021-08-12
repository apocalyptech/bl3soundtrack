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
  * The tracks in here are often attributed to the band "X-Ray Dog," but that's
    really a *label* which specializes in commercial for-license music.  The
    Amazon links below make this mistake, in fact.
  * You can see a big chunk X-Ray Dog's catalog
    [at sourceaudio.com](https://bmgmusic.sourceaudio.com/#!label?l=551393&page=albums),
    and you'll see that the composers vary from album to album.
  * The two most prominent names on these tracks, Sarah Louise McIntosh and
    Thom Robson, are [now releasing music as "Wnderland"](https://www.fadedglamour.co.uk/2020/12/wnderland-new-music-sarah-mcintosh-thom-robson.html),
    but the formation of that band seems to post-date these track by quite a bit.
  * Regardless, these tracks can be seen [here](https://bmgmusic.sourceaudio.com/#!explorer?b=5101899)
    or [here](https://search.upright-music.com/album/8921d31d-93b0-4d41-9c4f-ac9011b17ef7?selected=db349c12-3fb9-4717-84cc-c55131eff59d)
  * Brad Marrapodi and Sarah McIntosh / Faster Than the Man
    * `1050394917.wem`
    * https://www.amazon.com/dp/B07HYGYFBH/
  * Sarah McIntosh and Thom Robson / Fighter
    * `132660270.wem`
    * https://www.amazon.com/dp/B07HYGDPGC/
  * Sarah McIntosh and Thom Robson / Freaks and Superpowers
    * `594656018.wem`
    * https://www.amazon.com/dp/B07HYGP4M7/
  * Sarah McIntosh and Thom Robson / Want It All
    * `421893270.wem`
    * https://www.amazon.com/dp/B07HYHRTNC/
  * Sarah McIntosh, Steve Williams, and Thom Robson / I Want to Be Loved (Epic Version)
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
    * I can find nothing about this band, but the track can be found on a few
      commercial one music licensing sites:
      * https://search.upright-music.dk/album/8dcedb7b-7974-4d62-bb64-3290c3b08843/nojs
      * https://app.bmgproductionmusic.co.uk/carrier/141731
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
    * `739128134.wem` *(this is a very short end bit to the song)*
  * `Mus_Sanctuary_Claptrap_Dance_Start (1754084250=Obj_Lock2_ObjVat).txtp`
    * `384558352.wem` *(this is the actual full song; does *not* actually
      need the end bit to be complete, though the game cues themselves cut
      off this file prematurely and use the end from the other `.wem`
      instead)*
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
  * It's not super straightforward to put together a "full" song from those,
    and there's no real "ending" part since the game just fades out.  This
    sequence makes a pretty decent song when concatenated together, though:
    1. `355525866.wem`
    2. `209203382.wem`
    3. `14961495.wem`
    4. `160810524.wem`
    5. `492686768.wem`
    6. `14961495.wem`
    7. `160810524.wem`

**Salvaged Claptrap Dubstep**

On Skywell-27, the Claptrap Salvage mission on there has you rescuing a dubstep
library for Claptrap.  This is the song that plays from the dead Claptrap.

* Ilana Tarutina, Jeffrey Fayman, and Yoav Goren / Pink Ferrari
  * `Mus_Orbital_Claptrap_Dubstep_Start (Mus_Scripted_Orbital_Claptrap=Claptrap_Dubstep_On).txtp`
  * `608497537.wem`
  * From 1 Revolution Music's "1RM069 Summer Pop EDM"
  * https://bmgmusic.sourceaudio.com/#!details?id=23497490
  * https://www.amazon.com/Pink-Ferrari/dp/B07PGF74QX
  * https://www.youtube.com/watch?v=LDlHVLi3UBA

**Agent Dee Dance Music**

The "Going Rogue" mission in Ambermire leads you to Agent Dee, undercover among
the CoV and leading a dance party.  This is the track playing then.  It's
just an instrumental.

* Erik Mikkelsen / Party Night
  * `Mus_Marshfields_Honey_Pot_Start (Mus_Scripted_Marshfields=Honey_Pot_On).txtp`
  * `752876681.wem`
  * From Anonymous Recordings' "AR004 EDM Heaven" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=21953807
  * https://www.amazon.com/Party-Night/dp/B07F4538KV

**Agonizer 9000 Song Selection**

Prior to the A9K fight, you can choose one of three songs to play.  These are
all commercially-licensed tracks for the game -- all instrumentals.  They're
also composed of a couple different TXTPs and a few different WEMs, each.

* "Blood" Option: Paul Whitehead and Emily Taylor / Plasma Storm
  * `Mus_Motorcade_Interior_A9K_Blood (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Looping).txtp`
    * `383710197.wem`
    * `102114354.wem`
  * `Mus_Motorcade_Interior_A9K_Blood (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Outro).txtp`
    * `455060268.wem`
  * From Beds & Beats' "BNB172 Neon Hyperdrive" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=19811223
  * https://www.youtube.com/watch?v=1uPOxLqDDAY
* "Fire Skull" Option: Richard Florio and Nick Nolan / Crank
  * `Mus_Motorcade_Interior_A9K_Fire (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Looping).txtp`
    * `72654236.wem`
    * `551453748.wem`
  * `Mus_Motorcade_Interior_A9K_Fire (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Outro).txtp`
    * `650765155.wem`
  * From Music Beyond's "BYND130 - Rock Aggressive" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=301192
* "Laughing" Option: Robert Edwards / Street Level
  * `Mus_Motorcade_Interior_A9K_Maniac (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Looping).txtp`
    * `854783025.wem`
    * `649644305.wem`
  * `Mus_Motorcade_Interior_A9K_Maniac (Mus_Scripted_Motorcade_A9KIntro=Mus_Scripted_Motorcade_A9KIntro_Outro).txtp`
    * `903160824.wem`
  * From Anonymous Recordings' "AR009 Trapped!" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=24904008
  * https://www.amazon.com/Street-Level/dp/B07PN7N6SG

**Sandblast Scar**

During the mission where you and Vaughn are driving through Sandblast Scar,
there's a few jazz tracks playing.  These are just instrumental and had
escaped my notice until later on.  First up:

* Christophe Dal Sasso and Dominique Mandin / Shake Up
  * `Mus_Convoy_Sax (Mus_Scripted_Convoy_Sax=Mus_Scripted_Convoy_Sax_Step01).txtp`
  * `576300338.wem`
  * From BAM Library's "BAM-AL 041 Brooklyn Coffee"
  * https://search.upright-music.com/album/addafcf8-5707-4c88-9fa3-9879d4aa747b/nojs
  * https://www.amazon.com/Shake-Up/dp/B08SQJWNWV
  * The track is processed to sound rather tinny and far away
* Nigel Thomas / Jazz City
  * This is split over three TXTPs, though it's the middle one which has the
    vast majority of the song:
    * `Mus_Convoy_Sax (Mus_Scripted_Convoy_Sax=Mus_Scripted_Convoy_Sax_Step02).txtp` / `635776072.wem`
    * `Mus_Convoy_Sax (Mus_Scripted_Convoy_Sax=Mus_Scripted_Convoy_Sax_Step03).txtp` / `609967766.wem`
    * `Mus_Convoy_Sax (Mus_Scripted_Convoy_Sax=Mus_Scripted_Convoy_Sax_Step05).txtp` / `506780064.wem`
  * From Production Music Online's "PMOL 197 Just Real Jazz" commercial-license album:
    * https://search.upright-music.com/album/a52e5c9f-c463-4ace-83d2-a81614774eae/nojs

**Sparrow and Grouse Songs**

There's a couple of licensed songs in the game relating to Sparrow+Grouse
quests.  They're both just instrumentals.

* Therapy Music w/ Tern
  * Suzanne Hansen / Sweet Breaths
  * `Mus_Desolate_Therapy.txtp`
  * `698416583.wem`
  * From Music Beyond's "BYND299 - Eastern Hemisphere 2" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=14831407
* "Celebration" music after saying goodbye to Typhon
  * Mariano Dimonte, Riccardo Gibertini, Antonio Vezzano, and Marco Zaghi / Little Young Lover
  * `Mus_Desolate_BetterTimes.txtp`
  * `1054920389.wem`
  * Processed to sound very different and muffled
  * From 101 Dark Orchid Music's "101DOM057 - Vintage Beats" commercial-license album
  * https://bmgmusic.sourceaudio.com/#!details?id=23332187
  * https://www.amazon.com/Little-Young-Lover/dp/B07Y42GJM7

**Carnivora Fairgrounds**

A random collection of fairground-style music is played when you enter
Carnivora.  These are all instrumentals, and they've been processed with
varying degrees of distortion.

* `Mus_Motorcade_Festival_Misc {r}.txtp`
  * `361835298.wem` - Rolf Eriksson / Big Top (ADD062 oddball and comedy)
    * https://bmgmusic.sourceaudio.com/#!details?id=15730738
  * `496936868.wem` - Johann Strauss (arr. Carl S Zittrer) / Blue Danube Waltz (PML172A Really Useful 2 Disc 1)
    * https://bmgmusic.sourceaudio.com/#!details?id=12631566
  * `659766963.wem` - Eric Allen / Dance of the Pipes (PML148 Comicals)
    * https://bmgmusic.sourceaudio.com/#!details?id=12630009
  * `1028152471.wem` - Niklas Edberger / House of Fun (ADD062 oddball and comedy)
    * https://bmgmusic.sourceaudio.com/#!details?id=15730734
  * `542450637.wem` - Roger Roger / Magic Fairground No. 1 (PML118 From The Archives 3)
    * https://bmgmusic.sourceaudio.com/#!details?id=12627198
  * `129569866.wem` - Roger Roger / Magic Fairground No. 2 (PML118 From The Archives 3)
    * https://bmgmusic.sourceaudio.com/#!details?id=12627200
  * `940996888.wem` - Denis Hawksworth / Merry Go Round (30) (PML134 Jingles 8)
    * https://bmgmusic.sourceaudio.com/#!details?id=12629245
    * full version: https://bmgmusic.sourceaudio.com/#!details?id=12622628
  * `112969551.wem` - Roger James Limb / On The Carousel (30) (PML134 Jingles 8)
    * https://bmgmusic.sourceaudio.com/#!details?id=12629247
    * full version: https://bmgmusic.sourceaudio.com/#!details?id=12619743
  * `410646284.wem` - Niklas Edberger, Anders Kampe / Pigalle (ADD009 Burlesque & Cabaret)
    * https://bmgmusic.sourceaudio.com/#!details?id=15779154
  * `602521095.wem` - Harry Gordon Forbes / Switchback (PML016 The Comedy Collection)
    * https://bmgmusic.sourceaudio.com/#!details?id=12618886
  * `930574999.wem` - Niklas Edberger, Anders Kampe / Thunderpants (ADD062 oddball and comedy)
    * https://bmgmusic.sourceaudio.com/#!details?id=16397103

**Atlas HQ Muzak**

There's two TXTPs containing this song; the first is relatively clean (though it's got
some processing on top of it), whereas the first is very noisy (made to sound like it's
coming out of a bad speaker inside a Porta Potty, in fact).  This plays at least
during the Lectra City mission with the person trapped in the Porta Potty, but given
the other cue name, it probably shows up in Atlas HQ somewhere, too.

* Christopher John White and Peter Denham Dixon / Riviera Retro (60 Sec)
  * `Mus_Mission_AtlasHQ_Musak_Lp.txtp`
    * `229826151.wem`
  * `Mus_Mission_PortaPrison_Potty_Bossa_Lp_Start.txtp`
    * `455499396.wem`
  * From Production Music Online's "PMOL 020 Comedy & Kitsch"
  * https://search.upright-music.dk/album/8e6578d4-0694-4026-94bf-29bec6233c45
    * The version used in the WEM file is the "60 Sec" version specifically, though
      a full-length track is available there as well.

**DLC1: Steel Dragon of Eternal Pain**

This is the metalhead who gets annoyed by Digby Vermouth recording his new track,
in that sidequest in the DLC.  The `.wem` files here are only really a snippet of
the full track.

* Aeternam / Praetor of Mercury
  * `MUS_SteelDragonOfEternalPain.txtp`
  * `458969297.wem`
  * `98249060.wem`
  * https://aeternam.bandcamp.com/track/praetor-of-mercury

**DLC4: Krieg's Ska Track**

A sidequest in DLC4 features a Ska track put on by Krieg's jailers in an attempt
to demoralize and psychologically torture their prisoners, but Krieg likes it.
I remember the in-game audio as being really dour and weird-sounding, but the
on-disk audio here is honestly not that bad (and sounds much more ska-like than
my memories would suggest).  The actual full track is even more so.

* Freddie Reid, John Robert Beck, Tim Hutton, and William Arthur / Buster Two Tone (Lite)
  * `MUS_KreigCell_SkaTrack.txtp`
    * `613144459.wem` - The main body of the track.  Is just a segment of the
      "real" full track, not the full thing
    * `924504323.wem` - Just a short intro-or-something (this does *not* complete
      the full track)
  * From Editone Production Music's "ET010 Brass Grooves"
  * https://bmgmusic.sourceaudio.com/#!details?id=26490746
  * https://search.upright-music.com/album/04004347-16c5-451b-b74f-5570105e214a
  * The non-"Lite" original version is also available:
    * https://bmgmusic.sourceaudio.com/#!details?id=26490811

# Other Info

This post's markdown (and a ton of other detailed info about dealing with BL3
audio extracts and processing these things into unofficial "companion"
soundtracks is also available [at github](https://github.com/apocalyptech/bl3soundtrack).
This data's hereby put this under public domain, or
[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
Enjoy!

