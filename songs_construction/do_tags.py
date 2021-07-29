#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
import subprocess

tag_re = re.compile("""^
        (?P<filename>.*\.ogg):\s+
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
            subprocess.run(['/usr/bin/vorbiscomment',
                '-a', filename,
                '-t', 'ARTIST={}'.format(artist),
                '-t', 'TITLE={}'.format(title),
                ])
        else:
            raise Exception('not matched: {}'.format(line))

