#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

grep uri ~/.config/audacious/playlists/1003.audpl | cut -d/ -f3- | sed -e 's:%20: :g' | while read filename; do cp "${filename}" ~/bl3_decrypt/extracted_audio/bl3-txtp/extras/; done

