#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import subprocess

for filename in sorted(os.listdir('.')):
    if filename.endswith('.txtp'):
        base_name = filename[:-5]
        wav_name = f'{base_name}.wav'
        mp3_name = f'{base_name}.mp3'

        subprocess.run(['/home/pez/bin/vgm123', '-d', 'wav', '-f', wav_name, filename])
        subprocess.run(['/usr/bin/lame', '--preset', 'standard', wav_name, mp3_name])
        os.unlink(wav_name)

