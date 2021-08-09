Borderlands 3: The Songs (unofficial)
=====================================

Just a collection of scripts and notes that I'd used to construct a
personal-use unofficial soundtrack named "Borderlands 3: The Songs".
This basically includes all the songs catalogued in the main post
which *aren't* part of the Crimson Radio set.  (So: intro/outro
cinematics, credits, Ellie's "Project DD" playlist, the Baby Dancer
track, and VR-0N1CA's electroswing dance track).  I may put together
something for Crimson Radio as well, but these were the ones I
actually wanted to get together.

I used the raw game audio for nearly all of these, and the construction
process should result in a soundtrack which doesn't have any lossy
re-encodes.  The audio data should be basically identical to the game files
themselves.  My one exception for this was Caleb Hawley's "Wish You Were
Mine," which is quite fragmentary in the game data.  For that, I just
grabbed the audio from youtube and did a lossy re-encode to Ogg Vorbis.

The construction work was all done on Linux, and is entirely
commandline-based.  The utilities in question probably exist on Windows
too, though.  The general pipeline looked like this:

1. Convert extracted `.wem` files to `.ogg` using [ww2ogg](https://github.com/hcs64/ww2ogg)
   and [ReVorb](https://github.com/ItsBranK/ReVorb)
2. For the DLC1 (Dandelion) credits `.ogg`, split it into separate songs
   using [mp3splt](http://mp3splt.sourceforge.net/) (despite the name,
   it losslessly splits Ogg Vorbis files, too).
3. For the Baby Dancer track (Max R.'s "Do It Like A Superstar!"),
   concatenate multiple `.ogg` files and add some trailing silence using
   [ffmpeg](https://www.ffmpeg.org/).
4. Trim some unnecessarily-long silence at the end of a few other tracks,
   using mp3splt.
5. Sequence into the order I want and add basic tags via [vorbiscomment](https://wiki.xiph.org/Vorbis-tools)
6. Use [vorbisgain](https://sjeng.org/vorbisgain.html) to add
   [ReplayGain](https://en.wikipedia.org/wiki/ReplayGain) tags to the
   files, which does volume normalization without having to do
   lossy re-encodes.

The `construction_scripts` dir contains some commands to help with
the more complex steps there, such as splitting the DLC1/Dandelion
file, and joining up all the Baby Dancer files.  (And also doing the
initial tagging.)  See also `notes.txt` in there, which includes
the specific cuts I'd made in step #4.

My tracklist, which IMO works quite well:

1. The Heavy / Put It on the Line
2. Sazz / Animal
3. Robert Edwards & Andrew Griffiths / Feathers
4. Sarah McIntosh and Thom Robson / Fighter
5. Max R. / Do It Like a Superstar! (Borderlands 3 mix, Apocalyptech edit)
6. Animal Fiction / Explosions
7. Sarah McIntosh and Thom Robson / Freaks and Superpowers
8. Alicia Keys / Girl On Fire
9. Robert Edwards ft. Little Violet / Puppet on a String
10. Dave Cleveland, Scott Dente, Ken Lewis, and Blair Masters / Slap Bracelet
11. Brad Marrapodi and Sarah McIntosh / Faster Than The Man
12. Parry Music / Push It Home
13. Animal Fiction / Hold On
14. The Creepshow / Blood Blood Blood
15. Sarah McIntosh and Thom Robson / Want It All
16. Caleb Hawley / Wish You Were Mine
17. Cage the Elephant / Trouble
18. Sarah McIntosh, Steve Williams, and Thom Robson / I Want to Be Loved (Epic Version)
19. Robert Edwards ft. Little Violet / PiSk Swing
20. Tyreen Calypso / Stealth Time!

