#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import sys
import subprocess

start_at = 0
#start_at = 2105954000
#start_at = 3461090400
to_play = []
with open('unmapped_wems.txt') as df:
    for wemname in df:
        wemname = wemname.strip()
        id_num = int(wemname.split('.', 1)[0])
        if id_num > start_at:
            to_play.append(wemname)

total = len(to_play)
for idx, wemname in enumerate(to_play):
    do_this_one = True
    while do_this_one:
        print(f'{wemname} ({idx+1}/{total})')
        try:
            subprocess.run(['vgm123', wemname])
        except KeyboardInterrupt:
            pass
        got_response = False
        while not got_response:
            try:
                resp = input('[enter] to continue, a[g]ain, [q]uit> ').strip().lower()
                if resp == 'q':
                    sys.exit(0)
                elif resp == 'g':
                    got_response = True
                elif resp == '':
                    got_response = True
                    do_this_one = False
            except KeyboardInterrupt:
                print('')

