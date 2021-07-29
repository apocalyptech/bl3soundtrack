#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

if [ ! -f 2secsilence.ogg ]; then
    ffmpeg -f lavfi -i anullsrc=r=48000 -t 2 -c:a libvorbis 2secsilence.ogg
fi
ffmpeg -f concat -i babydancer.txt -c copy Max_R_-_Do_It_Like_A_Superstar_BL3_mix_apoc_edit.ogg
