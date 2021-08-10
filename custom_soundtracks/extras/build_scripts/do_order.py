#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import sys
import shutil

if not os.path.exists('ordered'):
    os.mkdir('ordered')
with open('order.txt') as df:
    for idx, line in enumerate(df.readlines()):
        filename = line.strip()
        new_filename = 'ordered/{:02d}-{}'.format(idx+1, filename)
        shutil.copyfile(filename, new_filename)

