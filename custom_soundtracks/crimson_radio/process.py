#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys
import shutil
import subprocess

wem_re = re.compile(r'^\s*\.\./\.\./(?P<wem>\d+\.wem).*')

with open('songs.txt') as df:
    for filename in df:
        filename = filename.strip()
        found_wems = set()
        with open('../music/{}'.format(filename)) as txtp:
            for line in txtp:
                if match := wem_re.match(line):
                    found_wems.add(match.group('wem'))
        if len(found_wems) != 1:
            print('{}: found {}'.format(filename, len(found_wems)))
        wem = list(found_wems)[0]
        new_wem = '{}.wem'.format(filename[:-5])
        shutil.copyfile('../../{}'.format(wem), new_wem)
        subprocess.run(['/home/pez/bin/ww2ogg.sh', new_wem])

