This dir is just to hold some scripts that I've used to wrangle the extracted
BL3 audio data in various ways.  Pretty minor stuff, but since I'm extending
this repo quite a bit anyway, I may as well throw 'em in here.

Some brief summaries:

* `wwiser-all.sh` - Runs [wwiser](https://github.com/bnnm/wwiser) against the
  collection of `.bnk` files in the current dir, which generates
  [TXTP](https://github.com/vgmstream/vgmstream/blob/master/doc/TXTP.md) files
  for use with [vgmstream](https://vgmstream.org/).  Make sure you've got
  [this name-suggestion file](https://raw.githubusercontent.com/bnnm/wwiser-utils/master/wwnames/Borderlands%203%20%28PC%29.txt)
  in the current dir with the name `wwnames.txt`, so that the TXTP files are
  named sensibly.
* `hash_to_name.txt` - A text file I can use for quick lookups of what
  wem/bnk numbers map to which known names.  Generated by running a `select`
  against the SQLite DB that wwiser can generate after matching names to
  numbers.
* `categorize.py` - After generating the TXTPs, you're left with a single
  dir with thousands of files in it.  This util categorizes them into some
  subdirs for easier browsing.
* `link_external_vos.py` - A bunch of voiceover-related `.bnk` banks are
  used to trigger arbitrary dialog which is chosen at runtime, so wwiser
  can't generate full TXTPs for those.  This util uses my
  [bl3data Python library](https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers)
  to find associations to those WEM files, and writes out a series of TXTPs
  for the matches that it finds.  Basically only useful inside the `vo`
  directory that `categorize.py` sets up.
* `find_unmapped_wem.py` - Attempts to identify WEM files which are not
  referenced in any TXTP files.
