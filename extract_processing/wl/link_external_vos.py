#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys
sys.path.append('/home/pez/git/b2patching/wlmods/python_mod_helpers')
from wldata.wldata import WLData

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

# Refs DB doesn't deal well with "dynamic" number suffixes, which these happen to be
hardcoded_dialogscript_refs = {
        # Overworld Alchemist quests
        '/Game/Audio/Events/VO/VOOW/Alchemist_Bro_1/WE_Daffodil_VO_OW_AlchemistBro_1': ['/Game/Dialog/Scripts/OverworldMissions/DialogScript_OW_AlchemistBro_1'],
        '/Game/Audio/Events/VO/VOOW/Alchemist_Bro_2/WE_Daffodil_VO_OW_AlchemistBro_2': ['/Game/Dialog/Scripts/OverworldMissions/DialogScript_OW_AlchemistBro_2'],
        '/Game/Audio/Events/VO/VOOW/Alchemist_Bro_3/WE_Daffodil_VO_OW_AlchemistBro_3': ['/Game/Dialog/Scripts/OverworldMissions/DialogScript_OW_AlchemistBro_3'],

        # Ancient Powers
        '/Game/Audio/Events/VO/VOSQ/Climb_Ancient_Powers_2/WE_Daffodil_VO_SQ_Climb_AncientPowers_2': ['/Game/Dialog/Scripts/SideMissions/DialogScript_SQ_Climb_AncientPowers2'],
        '/Game/Audio/Events/VO/VOSQ/Climb_Ancient_Powers_3/WE_Daffodil_VO_SQ_Climb_AncientPowers_3': ['/Game/Dialog/Scripts/SideMissions/DialogScript_SQ_Climb_AncientPowers3'],
        '/Game/Audio/Events/VO/VOSQ/Climb_Ancient_Powers_4/WE_Daffodil_VO_SQ_Climb_AncientPowers_4': ['/Game/Dialog/Scripts/SideMissions/DialogScript_SQ_Climb_AncientPowers4'],
        '/Game/Audio/Events/VO/VOSQ/Climb_Ancient_Powers_5/WE_Daffodil_VO_SQ_Climb_AncientPowers_5': ['/Game/Dialog/Scripts/SideMissions/DialogScript_SQ_Climb_AncientPowers5'],
        }

# DialogScript objects which don't seem to be linked properly (or even
# have sound bank objects).  I suspect all this audio never actually
# shows up in the game.
no_bank_scripts = [
        '/Game/Dialog/Scripts/VOBD/DialogScript_VOBD_TORGUE',

        # These *do* have an associated WwiseExternalMediaTemplate, at least, but seemingly no sound bank
        '/Game/Dialog/Scripts/VOBD/DialogScript_VOBD_SALISSA',
        '/Game/Dialog/Scripts/VOBD/DialogScript_VOBD_POLLY',
        ]

# There's also some interesting/fun voiceovers which seem to not exist in
# the data at all, in addition to not having a sound bank.  Since I'd gone
# through them to see what they were, I figured it makes sense to hardcode
# some labels for 'em.
orphan_wems = {
        'vesper': [
            # Some unused Vesper dialogue
            289213242,
            542149245,
            1288369298,
            2496481534,
            2649281356,
            3688567861,
            4066746671,
            ],
        'alt_vesper': [
            # Sounds like placeholder dialogue
            1612462260,
            3542900755,
            ],
        'tina': [
            # Tiny Tina: Quest exclamations and Random Encounters, mostly
            305667454,
            406716555,
            537129449,
            761802241,
            1229542909,
            1391976124,
            1400466093,
            1852910580,
            2061570151,
            2091987477,
            2246620876,
            2340721285,
            2771407286,
            3008124384,
            3093576708,
            3725614124,
            3987615244,
            4052359261,
            ],
        'dragon_lord': [
            # Just some random Dragon Lord stuff; nothing too interesting in here, acutally
            108633447,
            747291814,
            921549248,
            1191262646,
            1986608075,
            2945256808,
            3988696088,
            4083746758,
            ],
        'monk': [
            # Same voice as Ron Rivolte, I think?  Seems to be a cut intro/early-game mission
            121636125,
            449893556,
            716227682,
            790449099,
            797109827,
            1001229657,
            1307552214,
            2373823767,
            2676458114,
            3513315570,
            3726931857,
            3985000236,
            4234024610,
            ],
        'unknown_distorted': [
            # Sounds kind of like a Coiled enemy maybe?  Not sure.
            991298961,
            991298962,
            991298963,
            991298964,
            991298965,
            ],
        'jar': [
            # Just a single unmemorable Jar line, apparently not used.
            3402035313,
            ],
        'intro': [
            # Intro cinematic lines!  Is prerendered when played in-game, but maybe there's
            # a debug mode which renders it all in-engine, perhaps?  Anyway, here they are.
            14392295,
            38921788,
            98245170,
            182054387,
            182819010,
            861344303,
            1075100226,
            1103246918,
            1118165931,
            1139792667,
            1142499092,
            1195705887,
            1300587928,
            1467983001,
            1543640905,
            1593013540,
            1620752254,
            1861072543,
            1861234445,
            1944545956,
            1954634266,
            1982265341,
            2055369583,
            2074389782,
            2168185340,
            2169291209,
            2330896070,
            2340277381,
            2448014986,
            2532221644,
            2557845365,
            2573580100,
            2578140743,
            2696399837,
            2882839378,
            3103627032,
            3151320141,
            3158580595,
            3169996346,
            3233004558,
            3383753659,
            3416509657,
            3503323556,
            3609565140,
            3697889787,
            3890284594,
            3958951259,
            3965804563,
            4005856155,
            4137635270,
            4268577035,
            ],
        'char_creation': [
            # Unused Tina voice lines while doing character creation.  Fun stuff!
            # Spellshot
            3285024418,
            170371984,
            3746078621,

            # Clawbringer
            4134277016,
            361344195,
            3641629967,

            # Brr-zerker
            1193575606,
            835480589,
            2594771634,

            # Spore Warden
            3903825562,
            1828576753,
            3016251403,

            # Graveborn
            2983924063,
            2173744103,
            2700525419,

            # Stabbomancer
            3849795932,
            2177844857,
            2541755233,

            # General customization
            594939340,
            823227938,
            863411137,
            1119720197,
            1496689008,
            1581884309,
            1683737862,
            3018453172,
            3090062777,
            3123071565,
            3256566054,
            3348836330,
            3543054456,
            3548828618,
            3801005960,
            4178223092,
            ],
        'unknown_falling': [
            # No idea, but these mostly reference falling/dropping, and sound vaguely skeletonish?
            2049050592,
            2049050593,
            2049050606,
            2049050607,
            2065828185,
            ],
        'unknown_coiled': [
            # Sounds like Coiled, I guess.  (Not especially interesting, though)
            4003373999,
            ],
        }

def write_dialogperformancedata(export, orig_txtp, wwise_object, base_name, script_name, script_short, counter):
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

    with open(new_filename, 'w') as odf:
        print(f'../../{short_id}.wem', file=odf)
        print('', file=odf)
        print(f'# Original txtp: {orig_txtp}', file=odf)
        print(f'# WwiseEvent Object: {wwise_object}', file=odf)
        print(f'# Dialog Script: {script_name}', file=odf)
        print('# Export: {}'.format(export['_jwp_export_idx']), file=odf)
        print(f'# Transcript: {text}', file=odf)
        print('', file=odf)

data = WLData()
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
        found_multiple = False
        full_names = data.get_refs_objects_by_short_name(we_name)
        if len(full_names) == 0:
            we_name = f'WE_Daffodil_{prefix}'
            full_names = data.get_refs_objects_by_short_name(we_name)
            if len(full_names) != 1:
                print(f'WARNING: {len(full_names)} objects found for WE_Daffodil attempt on {prefix}')
                continue
        elif len(full_names) > 1:
            # This happens once, for WE_Daffodil_VO_SQ_Climb_AncientPowers.  Adding in a loop-across-all-results
            # seems to basically Do The Right Thing, so we're allowing it.  (In the BL3 version, it
            # never pops up.)
            found_multiple = True

        for full_name in full_names:
            if found_multiple:
                print(f'NOTICE: Found multiple for {we_name}, processing {full_name}')
            #full_name = full_names[0]
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
            if full_name in hardcoded_dialogscript_refs:
                scripts = hardcoded_dialogscript_refs[full_name]
                print(f'NOTICE: Using hardcoded refs for {full_name}')
            else:
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
                            write_dialogperformancedata(export, filename, full_name, base_name, script_name, script_short, counter)
                            counter += 1
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

# Process DialogScripts which don't have a soundbank (and thus no .txtp to start with)
for script_name in no_bank_scripts:
    print(f'NOTICE: Processing No-Bank DialogScript: {script_name}')
    script_short = script_name.split('/')[-1]
    script = data.get_exports(script_name, 'DialogPerformanceData')
    count = 0
    for export in script:
        write_dialogperformancedata(export, '(none)', '(none)', 'no_bank', script_name, script_short, counter)
        counter += 1

# Now process "pure" orphans -- just .wem files sitting there on their own.
print('NOTICE: Processing hardcoded "orphan" .wem files')
for label, wems in orphan_wems.items():
    for idx, wem in enumerate(sorted(wems)):
        new_filename = f'orphan-apoc-{label}-{idx:03d}.txtp'
        with open(new_filename, 'w') as odf:
            print(f'../../{wem}.wem', file=odf)
            print('', file=odf)
            print('# "Orphaned" .wem file with no sound bank or apparent reference in the data', file=odf)
            print('# Manually sorted by link_external_vos.py by Apocalyptech', file=odf)
            print('', file=odf)

