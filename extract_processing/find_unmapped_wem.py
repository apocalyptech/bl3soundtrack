#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys

wem_re = re.compile(r'^\s*\??../../(?P<wem_name>\d+\.wem).*')
other_wem_re = re.compile(r'.*##(?P<wem_name>\d+\.wem).*')
txtp_re = re.compile(r'^(?P<txtp_name>.*?)(\s+.*)?\.txtp$')
apoc_re = re.compile(r'^(?P<base_name>.*?)-apoc-.*')

# Get a list of wems
wems = {}
for filename in os.listdir('.'):
    if filename.endswith('.wem'):
        wems[filename] = set()

# Loop through .txtps to make a wem mapping
#limit = 100
limit = 9999999999999999
current = 0
for dirname, _, filenames in os.walk('bl3-txtp'):
    if current > limit:
        break
    for filename in filenames:
        if filename.endswith('.txtp'):

            current += 1
            if current > limit:
                break

            # Get the "base" name of the txtp
            match = txtp_re.match(filename)
            assert(match)
            txtp_name = match.group('txtp_name')
            if match := apoc_re.match(txtp_name):
                txtp_name = match.group('base_name')

            # Open it up and create mappings
            with open(os.path.join(dirname, filename)) as df:
                for line in df:
                    if match := wem_re.match(line):
                        wem_name = match.group('wem_name')
                        if wem_name in wems:
                            wems[wem_name].add(txtp_name)
                        else:
                            # Eh, lots of these, just ignore 'em
                            pass
                            #print('Unknown WEM reference: {}, {}'.format(
                            #    wem_name,
                            #    filename,
                            #    ))
                    elif match := other_wem_re.match(line):
                        wem_name = match.group('wem_name')
                        if wem_name in wems:
                            wems[wem_name].add(txtp_name)

# Reports
for wem, links in wems.items():
    if not links:
        print(wem)
