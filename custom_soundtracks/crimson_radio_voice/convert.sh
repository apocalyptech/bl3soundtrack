#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

for file in *.txtp
do
    base_file="$(basename "${file}" .txtp)"
    wav_file="${base_file}.wav"
    vgm123 -d wav -f "${wav_file}" "${file}"
    lame --preset standard "${wav_file}"
    rm "${wav_file}"
done
