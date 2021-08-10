Processing Borderlands 3 Audio
==============================

Processing the raw audio files from Borderlands 3 isn't difficult really,
but it does require a bunch of tools that you may not be familiar with
yet.  This document aims to go over the usual methods you can use to
manage and listen to the music in the game.

* [Extracting the Audio](#extracting-the-audio)
* [Processing WEM Files](#processing-wem-files)
* [Processing BNK Files](#processing-bnk-files)
* [Converting BNK to TXTP](#converting-bnk-to-txtp)
* [Understanding TXTP Files](#understanding-txtp-files)
* [Categorizing TXTPs](#categorizing-txtps)
* [Code-Based TXTP Processing](#code-based-txtp-processing)

Extracting the Audio
--------------------

There's a couple of ways to go about extracting the game audio.
[One method, described here on reddit](https://www.reddit.com/r/borderlands3/comments/d6ggya/how_get_audio_files_from_bl3/)
involves using an app called QuickBMS and Ravioli Game Tools to get the
job done.  I'm not personally familiar with those at all, but that
post should have all the info you need to do it that way.

Personally, I use the methods described at
[the BLCMods wiki](https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data),
which is more geared towards BL3 modders, but which work just as well
for extracting audio.  The `unpack_bl3.py` script linked in there is
my usual method for doing so.  The script's default configuration is
geared towards game data, not audio, and in fact explicitly *skips*
doing audio extraction, so you'll need to make a couple of changes.

First off, near the top you'll see this:

```python
# Files/Directories to remove after doing the extraction (to
# save on some diskspace)
EXTRACTED_FILES_TO_DELETE: list[str] = [
    "*.wem",
    "*.bnk",
    "*ShaderArchive*",
]
```

You want to *keep* `.wem` and `.bnk` files, so you'll want to delete
those lines, or comment them out.  Commented lines would end up looking
like this, instead:

```python
# Files/Directories to remove after doing the extraction (to
# save on some diskspace)
EXTRACTED_FILES_TO_DELETE: list[str] = [
    #"*.wem",
    #"*.bnk",
    "*ShaderArchive*",
]
```

Secondly, just a little further down:

```python
# Skip pakfiles which *only* have .wem audio data?  Be sure to remove "*.wem"
# from the auto-delete list, above, if you set this to False
SKIP_AUDIO_PAKS = True
```

Change that `SKIP_AUDIO_PAKS = True` to `SKIP_AUDIO_PAKS = False`.

At this point, you can run `unpack_bl3.py` against the pakfiles you want
to extract.  All pakfiles starting with `pakchunk2-` contain base-game
audio, so you'll want that.  Pakfiles starting with `pakchunk3-` are
generally English-language-related files, but they also include things
like all the Crimson Radio music tracks, so you may want those as well.
If you'd like a language other than English, you might want one of
these as well:

* pakchunk85 - French
* pakchunk86 - Italian
* pakchunk87 - German
* pakchunk88 - Spanish
* pakchunk89 - Japanese
* pakchunk90 - Korean
* pakchunk91 - Chinese

Note that those pakfiles don't contain things like the Crimson radio
tracks, so they're pretty likely to be *just* dialogue sounds, so
if you don't care about dialogue, you can probably ignore those.

Finally, if you want to be sure you've got everything, you probably
want to unpack the main DLC pakfiles as well.  It *looks* like in
general all the DLC soundfiles end up getting added to base-game
patch pakfiles in the next release after the DLC's released, but I'm
not sure if that can be counted on.  So, if you want audio from
the DLCs, be sure to include (from the `AdditionalContent` directory):

* DLC1 (Moxxi's Heist of the Handsome Jackpot): `Dandelion.pak`
* DLC2 (Guns, Love, and Tentacles) - `Hibiscus.pak`
* DLC3 (Bounty of Blood) - `Geranium.pak`
* DLC4 (Psycho Krieg and the Fantastic Fustercluck) - `Alisma.pak`
* DLC5 (Designer's Cut) - `Ixora.pak`
* DLC6 (Director's Cut) - `Ixora2.pak`

For instance, when I extract the soundfiles, I'd basically collect
the pakfiles in a single dir and do:

    ./unpack_bl3.py pakchunk2-* pakchunk3-* Dandelion.pak Hibiscus.pak Geranium.pak Alisma.pak Ixora.pak Ixora2.pak

Once that's done, you'll have an `extracted_new` directory containing
a bunch of data (assuming you included the DLC pakfiles), plus all
the soundfiles.  The audio files will all be under the path `/Game/WwiseAudio`,
so you can safely remove everything else that was extracted, if you're
only interested in the audio.  The data from the language-specific
pakfiles will be in a subdirectory under there, named by the language.

Processing WEM Files
--------------------

So: via whatever method, you've got the audio extracted.  The first
thing you'll notice is that all the files are named pretty incomprehensibly,
with long numbers for filenames, and `.wem` and `.bnk` for extensions.

First up: `.wem` files are "bare" audio files, similar to a single mp3 file,
but they're stored in a custom [Wwise](https://www.audiokinetic.com/products/wwise/)
file format which usual desktop sound-playing apps don't understand
directly.

Fortunately, internally, these `.wem` files are [Ogg Vorbis](https://xiph.org/vorbis/)
files, which *is* a well-supported format like mp3, which your current
audio player probably *does* support.  Converting a `.wem` (which
you probably can't play directly) into an `.ogg` is pretty straightforward,
and uses two tools:

1. [ww2ogg](https://github.com/hcs64/ww2ogg) - This is the main util to
   get it done, and will result in an `.ogg` file that you can probably
   play just fine.
2. [ReVorb](https://github.com/ItsBranK/ReVorb) - This is used to "clean
   up" the Ogg files that ww2ogg generates.  The freshly-converted Ogg
   files can have a bit of weirdness internally, and running them through
   this app makes sure that they're in as good a shape as possible.

Alternatively, there's another app (which will become even more important
when we talk about `.bnk` files) called [vgmstream](https://vgmstream.org/),
which is a project that's geared towards playing audio that's come from
video games.  It supports a ton of different formats, including `.wem`.
If you've got vgmstream installed on one of its supported players, you'll
be able to just play `.wem` files directly.  It's a recommended install
even if you're using ww2ogg to do Ogg Vorbis conversions.

It's worth noting that the game engine never *directly* plays a specific
`.wem` file, and the raw audio in the `.wem` files might not be exactly
what gets played while the game runs.  For that, we need to look into
the `.bnk` files instead.

Processing BNK Files
--------------------

`.bnk` files are "Sound Bank" files, and these are actually super complex
and interesting.  When the game wants to play audio, it will *always*
go through one of these Sound Bank objects, and the sound bank might
redirect over to one of those `.wem` files (or it might contain other
`.wem` files *inside* the `.bnk` as well).  The `.bnk` file might also
turn out to be extraordinarily simple and just play a *single* `.wem`
file without much processing at all.  (That's often the case for
Crimson Radio and Credits songs, for instance.)

The `.bnk` files can act as an in-game
[Digital Audio Workstation](https://en.wikipedia.org/wiki/Digital_audio_workstation)
(DAW), which allows game designers/developers to do some real fancy
things to their audio processing.  Here's
[one description](https://github.com/bnnm/wwiser/blob/master/doc/WWISER.md)
of some of the things that the Wwise sound bank format is capable of.

In Borderlands 3's case, for instance, the in-level music is usually split up
into its individual parts (so: a track for the main melody, a track for the
main drums, a track for bassline, etc...), and further split up into multiple
variants of each of those parts.  So you may have five different variations for
one section of drums, or three different main melody parts.  And that's just
for one 30-second bit of audio -- a full *song* is then comprised of multiple
parts, each of them containing all these layered and split-out components.

Then the BL3 engine can dynamically switch between all these parts
to allow the music to follow the flow of the action in-game.  They've
actually got two separate variables called "Interest" and "Threat Level,"
and each level of those affect which parts inside all these disparate
tracks will be getting played at any given point.  It's a lot to keep
track of!

Converting BNK to TXTP
----------------------

`.bnk` files can't really be "played" in the same way that a `.wem` file can,
even with vgmstream, but there *is* a utility out there which can convert
them to a format that vgmstream *does* understand:
[wwiser](https://github.com/bnnm/wwiser).

Basically, once you've got Wwiser installed, you run it against the entire
set of `.bnk` files that you extracted, and it'll output a bunch of `.txtp`
files which can then be played with vgmstream.  The command that I usually
use to do this conversion is:

    wwiser.py -g -go bl3-txtp -gw .. Init.bnk *.bnk

Let's take those arguments one-by-one:

* `-g` - This is the argument which tells Wwiser to generate `.txtp` files
* `-go bl3-txtp` - This tells Wwiser to output the `.txtp` files into a
  new directory named `bl3-txtp`.  Obviously you can use any directory name
  you like here.
* `-gw ..` - When the `.txtp` files are generated, they will often need to
  refer back to the `.wem` files you extracted.  This tells Wwiser to use
  the path `..` to find them -- because we're outputting the `.txtp` files
  into the `bl3-txtp` directory, we'd find the `.wem` files one level up.
  The default value here is `wem`, which would mean you'd need to copy
  the relevant `.wem` files into a `bl3-txtp/wem`, which seems like a hassle
  to me.
* `Init.bnk *.bnk` - Wwiser recommends processing `Init.bnk` first, so I
  just specify it first and then use the wildcard for everything else.  That
  means that `Init.bnk` might be getting processed twice, but it doesn't
  seem to hurt anything.

Once you've run `wwiser.py`, you'll have a `bl3-txtp` dir with a ton of
`.txtp` files in them, but you'll see that they're still named quite
incomprehensibly, with big ol' numbers in the filenames rather than anything
useful.  For instance, you might have:

    3029262992 (2385001308=245432218).txtp

This is due to how Wwiser stores its data -- we need to supply
wwiser with a list of names that we expect to show up in the data, so that
it can associate the numbers to the names.  I've put together a file to
use for that which you can find here: [Borderlands 3 (PC).txt](https://raw.githubusercontent.com/bnnm/wwiser-utils/master/wwnames/Borderlands%203%20%28PC%29.txt).

Save that file in the same directory as all the `.wem` and `.bnk` files,
with the filename `wwnames.txt`.  Then when you run `wwiser.py`,
it'll automatically make those number-to-name associations and generate
filenames which make a lot more sense.  For instance, our example above
becomes:

    Mus_Marshfields_Honey_Pot_Start (Mus_Scripted_Marshfields=Honey_Pot_On).txtp

... which is the song that plays while Agent Dee distracts a group of
CoV in the Ambermire while in disguise.

Regardless, once you have these `.txtp` files, they'll be directly playable
with the vgmstream app that we talked about in the `.wem` section.  So,
make sure that you've got vgmstream installed, and you'll be good to go!

Understanding TXTP Files
------------------------

Some very complete (though sometimes confusing) docs for the TXTP format
can be found [at the vgmstream github page](https://github.com/vgmstream/vgmstream/blob/master/doc/TXTP.md),
so that should be considered your best source of information for how these
work.  However, the TXTP files generated by Wwiser generally only use a
subset of the total TXTP format, and the examples below will show you
most of what you'd need to know to be able to interpret the ones you'll
see in the Borderlands 3 data.

If we take a look at at `Mus_Marshfields_Honey_Pot_Start (Mus_Scripted_Marshfields=Honey_Pot_On).txtp`
in a text editor, near the top is where all the useful information is:

     ../752876681.wem #i #b 0.9375
     ../752876681.wem #i #b 90.9375 #r 0.9375 #@loop
    group = -S2  #v -11.0dB  ##loop

Because we specified `-gw ..`, it's looking for the `.wem` files in the
parent directory, which is generally how I like it.  The bottom
line which starts with `group = -S2` is saying that Wwise should play
the preceeding two wem files in a segment (so: one after the other).
The `#v -11.0dB` directive is saying to lower the volume by 11dB.

For each of the `.wem` entries, you'll see a `#b` parameter which is
setting the length to play.  The first one plays for 0.9375 seconds,
and the second plays for 90.9375 seconds.  Additionally, the second
entry uses `#r 0.9375` to "cut off" the first 0.9375 seconds.  If
we look closely at the `.wem` filenames themselves, we notice that
it's actually the same file twice.  So we play the first 0.9375
seconds, and then skip 0.9375 seconds to play the rest?  What gives?

Well basically that's down to the `#@loop` parameter on the second
one.  The first 0.9375 seconds of the file is an "intro" to the
track, and then everything *beyond* that point can be looped
indefinitely.

Taking a look at a different TXTP file, we might see something like:

      ../196791315.wem #i #b 3.2
      ../280173883.wem #i #b 3.2 #v -9.0dB
      ../513861638.wem #i #b 3.2 #v -5.0dB ##fade
     group = -L3 #@layer-v
      ../196791315.wem #i #b 28.8 #r 3.2
      ../280173883.wem #i #b 28.8 #r 3.2 #v -9.0dB
      ../513861638.wem #i #b 28.8 #r 3.2 #v -5.0dB ##fade
     group = -L3 #@layer-v #@loop
    group = -S2  #v -9.0dB ##loop

The first three `.wem` files are grouped together with `group = -L3`.
Note the `L` in there, and the `#@layer-v`.  That means that all
three of those `.wem` files are mixed together right on top of each
other, so that they form one "combined" track of their own.

Then the next three `.wem` files are similarly combined into a
`group = -L3 #@layer-v` construct, which does the same thing (and
happens to be where the looping starts).  And then at the end, we
have a `group = -S2`, which is playing those previous two layered
groups one after the other (looping over the second).

As one final example, you may see this kind of group as well:

     ../828674333.wem #i #b 2.5531914893616996
     ../997629975.wem #i #b 2.5531914893616996
     ../574466156.wem #i #b 2.5531914893616996
     ../659770987.wem #i #b 2.5531914893616996
     ../290672607.wem #i #b 2.5531914893616996
     ../631412921.wem #i #b 2.5531914893616996
     ../186472671.wem #i #b 2.5531914893616996
     ../784989600.wem #i #b 2.5531914893616996
    group = -R8>1  #v 5.0dB  ##fade

Note the `-R8>1` in the group arguments -- that means that this
is a *random selection* group.  There's eight total bits which
can be randomly selected, and right now it's hardcoded to play
the very first one (so it'll sound the same every time).  You can
change that `1` to be any number from `1` to `8` to hardcode a
specific option, or set it to `0` to make it be truly random.
(You can also set it to a dash (`-`) instead, to instead pretend
it's a segment group, as if it had said `group = -S8`.)

These groups can be nested and sequenced all over the place,
and you can have a random group whose options are *other* groups,
mixed in with occasional "straight" `.wem` references, and so
on.  You can also find references to `.wem` files which are stored
*inside* `.bnk` files, though those don't generally show up in
the music TXTPs.

The nice thing about this text format is that it's actually not
too bad to figure out how to sequence and arrange things
yourself.  I'd ended up doing a fair bit of arranging while
putting together the "Extras" soundtrack, since I needed to
string together a number of TXTP files, and a number of different
bits from *inside* the TXTPs as well.

Categorizing TXTPs
------------------

The Wwiser command I run to create the TXTP files outputs into `bl3-txtp`,
but I tend to like categorizing the generated files into more subfolders,
because I find them much easier to deal with.  For instance, I've got
a separate subfolders for `music` and `enemies`, etc.  I've got a script
to do this categorization for me in `extract_processing/categorize.py`,
so check that out if you'd like to do the same.

One side-effect of that is that my TXTP files are actually *two* levels
deeper than the `.wem` files they reference, so my actual command that
I use to generate TXTP files is:

    wwiser.py -g -go bl3-txtp -gw ../.. Init.bnk *.bnk

So the `.wem` references have `../../` in front of them instead of just
`../`

Code-Based TXTP Processing
--------------------------

One final thing I'll mention is that for processing the "Extras"
soundtrack, I ended up making use of some code to assist in wrangling
the TXTP files into use for track creation.  Surprising nobody familiar
with my usual habits, this is a Python script.  It can be found at
`custom_soundtracks/extras/build_scripts/txtp_process.py`, and could
be useful to anyone trying to do similarly complicated things to the
level soundfiles.

It's set up to be usable as a commandline tool, and has a bunch of
actions which are rather custom-built for the kind of soundtrack
processing that I'd settled on while working with them myself.  The
script itself does contain some classes which can read in the
Wwiser-generated BL3 TXTP files and work with them as native Python
objects, though, which can be quite powerful and useful.  Note that it
is *not* a general-purpose TXTP processor; the TXTP format allows for
a lot more functionality than this supports.  It's very custom-built
for these specific BL3 TXTPs.  (One example of a trivial thing that
TXTP supports but this one doesn't: the `Txtp` class requires that
there only be a single top-level object, since that's how Wwiser
generates the BL3 TXTP files.  But TXTP itself is perfectly happy to
just have an ungrouped list of elements, etc.)

Anyway, I mostly just wanted to mention that it exists.  If you want
more details, check out the code.  Here's its `--help` output, though:

    usage: txtp_process.py [-h]
                           (-o OUTPUT | -s SPLIT | -c | --find-leadins | --do-transforms | --soundtrack SOUNDTRACK | --soundtrack-simple SOUNDTRACK_SIMPLE | --soundtrack-leadin SOUNDTRACK_LEADIN | --gen-leadin-randoms)
                           [-i] [--lowest-random] [--schema SCHEMA] [-n] [--nopad]
                           [--random-count RANDOM_COUNT]
    
    Performs various actions on TXTP files
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            Output our parsed version of the specified file
      -s SPLIT, --split SPLIT
                            Split the the segmented file into multiple txtp files. Will
                            write to numbered files starting with 1.txtp
      -c, --check           Check all TXTP files in the cur directory for parseability
      --find-leadins        Report on files in the current dir which have what appear to
                            be 'leadin' intro segments.
      --do-transforms       Do the transforms I like to do on freshly-extracted music.
                            Namely: adjust volumes to try and avoid super-quiet music,
                            set random groups to actually randomize, and remove loop
                            parameters.
      --soundtrack SOUNDTRACK
                            Attempt to process files in the current dir into a
                            soundtrack track. Loops through as many variants as
                            possible, per part. String should be the output filename
      --soundtrack-simple SOUNDTRACK_SIMPLE
                            Attempt to process files in the current dir into a
                            soundtrack track. Just picks a single variant for each part.
                            String should be the output filename
      --soundtrack-leadin SOUNDTRACK_LEADIN
                            Attempt to process files in the current dir into a
                            soundtrack track. Handles soundtracks which have a "lead-in"
                            at the beginning, and processes similarly to the non-simple
                            soundtrack version. String should be the output filename
      --gen-leadin-randoms  Given a collection of leadin-based TXTPs, generate a set of
                            leadin+body TXTPs for each random possibility (not, like,
                            permutations, but just N files where N is the max
                            randomization for a single group).
      -i, --include-comments
                            Include TXTP comments in output, if present
      --lowest-random       When in simple soundtrack mode, choose the lowest random
                            element, rather than the highest (for some collections, this
                            might lead to more "exciting" tracks).
      --schema SCHEMA       Comma-separated segment list to use in soundtrack-leadin
                            mode. Has no effect in other modes. Without this option, a
                            hardcoded list will be used instead, which is unlikely to
                            make sense (or even work) with arbitrary music sets.
      -n, --nofade          When processing soundtracks, don't fade out -- instead,
                            allow the full end-of-track to play.
      --nopad               Don't add 2 seconds of padding at the end of soundtrack
                            processing Currently does not apply to leadin soundtracks.
      --random-count RANDOM_COUNT
                            In basic soundtrack mode, override our detected min. random
                            count.

