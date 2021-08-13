Borderlands 3: Crimson Radio Vocal Segments
===========================================

I didn't actually put these in a soundtrack or anything, but I *was*
interested in pulling out the vocal segment audio from CoV/Crimson
Radio and giving those a listen, since I never really spent much
time listening to them in-game.  This dir has a few scripts that
I'd used to do so.

First up: `grab.py` makes use of my [bl3data](https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers)
library to find all the relevant non-music Crimson Radio TXTPs and
copy them into the current dir.  (As such, it requires extracted
game data to actually do anything, not just the audio.)  It also
requires that my `categorize.py` script has been run so that the
voiceover-specific tracks are in their own `vo` directory, or at
least that they're not in the same dir as the music tracks (since
otherwise this will also pull in the music tracks).

(Alternatively, `vo_txtp_list.txt` contains a list of the TXTPs
which were pulled in, so you could just copy those by hand.)

Once the TXTPs have been copied over, I used the `--fix-mixed-samplerate`
option of my `txtp_process.py` script, which can be found in the
"Extras" dir here.  Some of the radio segments (*mostly* in the
Crimson Radio area) mix up `.wem` files with multiple samplerates,
which vgmstream doesn't really handle properly.  That
`--fix-mixed-samplerate` option makes use of `vgmstream123` and
[SoX](http://sox.sourceforge.net/) to resample the audio where
appropriate so that all files mentioned in the TXTPs have the same
samplerate.

Then, finally, I used `convert.sh` to loop over all the TXTPs and
use `vgmstream123` and [lame](https://lame.sourceforge.io/) to
convert 'em to mp3.  That's it!  Didn't bother with tagging or
arranging or anything, since these were going to be a listen-once kind
of thing.
