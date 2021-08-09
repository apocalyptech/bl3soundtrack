#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys
sys.path.append('/home/pez/git/b2patching/bl3mods/python_mod_helpers')
from bl3data.bl3data import BL3Data

# Some sound banks don't have specific dialog events coded into them; they
# just basically serve as a redirect-or-whatever which the engine can use
# to play arbitrary `.wem` files.  There's no way to find out what possible
# files there are by looking at *just* the wem/bnk files themselves; you've
# got to dig into the game data to do so.
#
# In wwiser context, these are "external IDs", and the generated txtp files
# have a "{e}" at the end of their filenames, and there's just question marks
# for where a filename might go.  This utility makes use of our refs DB and
# data-extraction methods to find what *should* be all the possible dialog
# lines which go through these redirecty bnk files, and we'll write out new
# .txtp files which reference them.
#
# There's still various cases which we don't understand, so it's not 100%,
# but it's pretty good.

hardcoded_name_tweaks = {
        #'WE_DLC2_VOBD_FB_Mumbler': 'WE_Oak_DLC2_VOBD_FB_Mumbler',
        #'WE_DLC2_VOBD_FB_Psycho': 'WE_Oak_DLC2_VOBD_FB_Psycho',
        #'WE_VO_Watership': 'WE_Oak_VO_Watership',
        }

data = BL3Data()
seen_names = set()
for filename in sorted(os.listdir('.')):
    if filename.endswith(' {e}.txtp'):
        base_name = filename[:-9]
        prefix = base_name.split('-')[0]
        we_name = f'WE_{prefix}'

        # Hardcoded tweaks
        if we_name in hardcoded_name_tweaks:
            we_name = hardcoded_name_tweaks[we_name]

        # Check to make sure we haven't already seen this
        if we_name in seen_names:
            print(f'WARNING: Seen {we_name} more than once...')
            continue
        seen_names.add(we_name)

        # Look up the full object name
        full_names = data.get_refs_objects_by_short_name(we_name)
        if len(full_names) == 0:
            we_name = f'WE_Oak_{prefix}'
            full_names = data.get_refs_objects_by_short_name(we_name)
            if len(full_names) != 1:
                print(f'WARNING: {len(full_names)} objects found for WE_Oak attempt on {we_name}')
                continue
        elif len(full_names) > 1:
            # This actually never happens
            print(f'ERROR: {len(full_names)} objects found for {we_name}')
            continue
        full_name = full_names[0]
        full_lower = full_name.lower()

        # Get the data and look for a ShortID
        # (errr, wait, don't bother -- this'd just be the ShortID of the .bnk)
        #we_name_lower = we_name.lower()
        #obj_data = data.get_data(full_name)
        #short_id = None
        #for export in obj_data:
        #    if export['export_type'] == 'WwiseEvent' and export['_jwp_object_name'].lower() == we_name_lower:
        #        if 'ShortID' in export:
        #            #print('{} -> {}'.format(
        #            #    we_name,
        #            #    export['ShortID'],
        #            #    ))
        #            short_id = export['ShortID']
        #            break
        ## Break out if we didn't find the short ID
        #if short_id is None:
        #    print(f'{we_name} -> ?')
        #    continue

        # Get references to the full object name, specifically looking
        # for DialogScript objects.  There are often more than one (for
        # banks which support more than one gender, for instance), and
        # in a handful of cases there are zero (so the objects don't
        # really seem to be in-use by the game).
        scripts = []
        for ref_name in data.get_refs_to(full_name):
            if 'DialogScript' in ref_name:
                scripts.append(ref_name)

        # Loop through scripts and find IDs
        counter = 0
        for script_name in scripts:
            script_short = script_name.split('/')[-1]
            unused_export_count = 0
            #print(script_name)
            script = data.get_exports(script_name, 'DialogPerformanceData')
            for export in script:
                #print(export['_jwp_export_idx'])
                if 'WwiseExternalMediaTemplate' in export:
                    if export['WwiseExternalMediaTemplate'][1].lower() == full_lower:
                        if 'Text' in export:
                            text = export['Text']['string']
                        else:
                            text = '[unknown]'
                        short_id = export['WwiseEventShortID']
                        #print(f'{short_id}: {text}')

                        new_text = re.sub('[\[\]\(\)\!\?\. ]', '_', text)
                        new_text = re.sub('[^A-Za-z0-9_]', '', new_text)
                        new_filename = '{}-apoc-{}-{:03d}-{}.txtp'.format(
                                base_name,
                                script_short,
                                counter,
                                new_text[:50],
                                )
                        counter += 1

                        if True:
                            with open(new_filename, 'w') as odf:
                                print(f'../../{short_id}.wem', file=odf)
                                print('', file=odf)
                                print(f'# Original txtp: {filename}', file=odf)
                                print(f'# WwiseEvent Object: {full_name}', file=odf)
                                print(f'# Dialog Script: {script_name}', file=odf)
                                print('# Export: {}'.format(export['_jwp_export_idx']), file=odf)
                                print(f'# Transcript: {text}', file=odf)
                                print('', file=odf)
                else:
                    # If WwiseEvent is present, we've already got a non-{e} txtp using it.
                    if 'WwiseEvent' not in export:
                        #print('{} -> {}'.format(
                        #    script_name,
                        #    export['_jwp_export_idx'],
                        #    ))
                        # Honestly not sure what's up with these.
                        unused_export_count += 1

            # Just reporting on these
            #if unused_export_count > 10:
            #    print(f'{script_name} -> {unused_export_count}')

