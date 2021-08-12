Borderlands 3 Raw Audio Processing
==================================

This repo serves as a general dumping grounds for information that I've
collected about dealing with raw audio extracts from Borderlands 3.
The general purpose was that I'd already bought all the official
soundtracks, but wanted to know what music in the game *wasn't* present
on those soundtracks, and to put together some unofficial "companion"
soundtracks for my own personal purposes.

To do that, I needed to extract the audio, match the raw audio to the OST
tracks as well as I could, and then categorize the remaining music tracks.

### Step 0: Official Soundtracks

There's a ton of these, and it's actually not super straightforward
to find out where to get them.  They're all available via Spotify (and
apparently Spotify has the most content out of anywhere else), but
Spotify is terrible (and not just for also-important
[privacy reasons like this](https://www.wired.com/story/spotify-tracking-how-to-stop-it/amp),
but because artists get an absolutely shit deal from it).

You can find official links to all the OSTs from here:
[Borderlands 3 Soundtrack Links / Info](soundtrack_sources.md)

### Step 1: Extract and Work With The Songs

I've slapped all this together here: [Processing BL3 Audio](processing_bl3_audio.md).
See in there for all the details, including how to get all the random-number-named
files into a state that's far easier to browse.

### Step 2: Associate Raw Audio With Official Tracks

There's really not a lot to say about this step -- it's just a lot of
manual work once you've got the audio extracted and know what to do
with it.  In the end I was able to map practically every OST track to
its constituent audio files -- there were only a few cases where it
looked like the OSTs might be making use of sources not found in the
game.

Regardless, those mappings can be found here: [Official Soundtrack Mappings](official_st_mapping.txt).

### Step 3: Categorizing The Rest

So once the OST tracks have been pruned out, what remains is to go
through the remaining ones and try and figure out what they all are.
There's a huge chunk which are Crimson Radio tracks, which are pretty
noticeable against all the rest.  For the remainder of the soundtrack
music, it turns out that there's actually quite a lot of
externally-licensed music throughout the game, even outside of the
"obvious" ones like the the songs playing in the credits sequences, etc.

The Internet At Large had already figured out nearly all of the most
obvious ones, but one site that was invaluable in tracking down the
remainder (including a lot of "symphonic" soundtrack instrumental tracks
which I'd orginally assumed were probably "in-house" by one of the usual
soundtrack composers) was [aha-music.com](https://www.aha-music.com/identify-songs-music-recognition-online),
which provides a Shazam-like service where you can upload some music (up
to ten tracks a day) to have it checked versus their database.  On a
few heavily-processed tracks I had to split them up a few times to get
them to work, but in general it came back with results basically right
away.

A lot of the results you'll get from aha-music.com aren't super easily
findable online, to verify, though, because a lot of this music appears
to have come from some commercial-license music sites which don't often
list releases in the public domain (at places like Amazon or Google, etc).
Fortunately, it turns out there's a couple of sites which are pretty
great for doing those lookups: [bmgmusic.sourceaudio.com](https://bmgmusic.sourceaudio.com/#!home)
and [search.upright-music.com](https://search.upright-music.com/).

**Songs w/ Lyrics + Crimson Radio, etc**

So first off, there's Crimson Radio tracks, and the other tracks throughout
the game which have lyrics and basically immediately stand out as being
licensed tracks.  I've posted my results for these files
[over at Reddit](https://www.reddit.com/r/borderlands3/comments/ospmu0/bl3_nonsoundtrackd_real_song_index_crimson_radio/),
but you can also see a copy of that post here: [Crimson Radio and Lyric Songs](crimson_radio_and_lyric_songs.md).

**"Symphonic"/Instrumental Tracks**

Next up is the tracks which largely sound like they'd fit well into the
existing OSTs, and are instrumental in nature.  There's a few pretty
obvious licensed tracks here, and a bunch which surprised me with the
fact that they weren't done in-house.  These are collected (with my own
notes about associations and general feel of the tracks) over here:
[Non-Soundtrack TXTPs](non_soundtrack_txtps.txt).

### Step 4: Unofficial Soundtrack Construction

So at this point I basically had a full picture of the audio available
in the game, so I put together some unofficial soundtracks for my own
personal use.  You won't find any actual music here, but I do have notes
about how I put them together (including tracklists, etc), in the
[`custom_soundtracks`](custom_soundtracks) directory here.  Given the
extraction info in Step 1, the mapping info from Step 3, plus the
information in `songs_construction`, you'd be able to reconstruct the
soundtracks pretty easily (assuming you're somewhat comfortable with
commandline work, anyway).

### License

I'll hereby put all the info in this repo this under public domain, or
[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
Enjoy!

