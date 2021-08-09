#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
import subprocess

tag_re = re.compile("""^
        (?P<filename>.*\.mp3):\s+
        (?P<artist>.*?)
        \s+/\s+
        (?P<title>.*)
        $""", re.VERBOSE)

with open('taginfo.txt') as df:
    for line in df:
        if match := tag_re.match(line):
            filename = match.group('filename')
            artist = match.group('artist')
            title = match.group('title')
            print('Tagging {}'.format(filename))
            subprocess.run(['/usr/bin/mid3v2',
                '-D',
                filename,
                ])
            subprocess.run(['/usr/bin/mid3v2',
                '-a', artist,
                '-t', title,
                filename,
                ])
        else:
            raise Exception('not matched: {}'.format(line))

