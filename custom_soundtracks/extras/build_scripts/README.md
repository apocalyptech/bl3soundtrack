Some scripts I used to help wrangle this soundtrack into existence.
As a warning, these weren't written with anyone else in mind, so don't
expect great code or comprehensible workflows.  Still, a quick summary
follows:

### TXTP Creation

* `txtp_process.py` - CLI app / library I used to process the level-based
  soundtrack files, since those were generally built up from rather complex
  source TXTPs with lots of randomized layered components (unlike most of
  the "real" licensed songs, etc).

### Soundtrack Processing

* `move_to_here.sh` - Moves files from a specific [Audacious](https://audacious-media-player.org/)
  playlist into the current dir for processing.
* `convert_txtp_to_mp3.py` - Converts all `.txtp` files in the current
  directory to wav, with the help of [vgmstream](https://vgmstream.org/)
  and [lame](https://lame.sourceforge.io/).
* `do_tags.py` - Applies some id3v2 tags to files in the current dir,
  based on `taginfo.txt`, using [mid3v2](https://mutagen.readthedocs.io/en/latest/man/mid3v2.html).
  Note that these might not be my exact final tags
* `do_order.py` - Moves files in the current dir to an `ordered` dir,
  prefixed by their new track number.

