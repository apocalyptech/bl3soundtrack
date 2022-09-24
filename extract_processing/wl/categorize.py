#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import sys
import shutil
import subprocess

dir_mappings = {
        'ambient': set([
            'Amb_',
            'EB_Amb_',
            'Overworld-0588-event',
            'OW_Amb_',
            ]),
        'emitters': set([
            'Emt_',
            'OW_Emt_',
            ]),
        'enemies': set([
            'Crea_',
            ]),
        'cinematics': set([
            'Cin_',
            ]),
        'gear': set([
            'Gear_',
            'Wep_',
            'WEP_',
            ]),
        'invalid': set([
            'Play_FullScreenMovieAudio_Passthrough',
            ]),
        'io': set([
            'IO_',
            'OW_IO_',
            ]),
        'music': set([
            'Mus_',
            'MUS_',
            ]),
        'npc': set([
            'NPC_',
            ]),
        'pc': set([
            'Char_',
            'OW_Char_',
            ]),
        'projectile': set([
            'Proj_',
            ]),
        'seq': set([
            'Main_Menu_Seq_',
            'Man_Menu_Seq_',
            'OW_Seq_',
            'SEQ',
            'Seq_',
            ]),
        'sfx': set([
            # These seem to be pretty consistently SFX.  Lots of unknown names,
            # though, alas!
            '1067095802-0128-event',
            '1159646687-0071-event',
            '1320460105-0083-event',
            '1370006196-0076-event',
            '1410953481-0103-event',
            '1785449766-0090-event',
            '1867863346-0072-event',
            '1905748063-0151-event',
            '2020320797-0016-event',
            '2208990248-0006-event',
            '2211522926-0150-event',
            '2310777307-0143-event',
            '2359339391',
            '2407467318-0005-event',
            '2453176240-0111-event',
            '2517791036-0096-event',
            '2624108603-0016-event',
            '271641266-0038-event',
            '2760271112',
            '2771590703-0005-event',
            '2804727694-0014-event',
            '3046496853-0015-event',
            '3079969831-0182-event',
            '3227800792-0042-event',
            '3275909912-0017-event',
            '3510728305-1639-event',
            '3548811367-0006-event',
            '3632504833',
            '3637127739',
            '3692106434-0074-event',
            '3876741096-0016-event',
            '3876741098-0016-event',
            '3876741099-0016-event',
            '3876741101-0016-event',
            '3967466185',
            '4031640425-0157-event',
            '4131702169-0009-event',
            '4195699098',
            '4226501499',
            '4265580146-0108-event',
            '509222014-0093-event',
            '595079417-0193-event',
            '644673822-0134-event',
            '679870471-0054-event',
            '754164483-0043-event',
            '860844770-0011-event',
            '99191822-0175-event',

            # More ordinary ones.  There's some incorrect name-to-hash
            # mappings here (NtGdiGetAppliedDeviceGammaRam2, SoNh_, etc)
            # but as of yet I don't know what the correct label is.
            'BP_CE_PuppetTransform',
            'Elemental_',
            'Emd_Shark_D_Thunder',
            'Exp_',
            'Foley_',
            'Footstep_',
            'FS_',
            'Gore_',
            'Imp_',
            'Loop_',
            'Loot_Spawn_',
            'Main_Menu_Dracolich_Wingflap',
            'Map_',
            'NtGdiGetAppliedDeviceGammaRam2',
            'OW_Loc_',
            'OW_Mis_',
            'OW_Mission_',
            'Shared_Elemental-',
            'SmithBoss_',
            'SoNh_',
            'Spell_',
            'Spells-',
            'Spells_',
            ]),
        'ui': set([
            'HUD_',
            'Menu_',
            'UI_',
            ]),
        'vo': set([
            'Daf_PLC2_VOBD_',
            'DAF_PLC2_VOBD_',
            'Daf_PLC3_VOBD_',
            'Daf_PLC4_VO_',
            'Daf_PLC4_VOBD_',
            'Daf_VOBD_',
            'DAF_VOBD_',
            'DAF_VOCT_',
            'Daffodil_VO_',
            'Daffodil_VOSQ_',
            'VO_',
            ]),
        }

prefix_mapping = {}
for dir_name, prefixes in dir_mappings.items():
    if len(prefixes) > 0:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
        for prefix in prefixes:
            prefix_mapping[prefix] = dir_name

for filename in os.listdir('.'):
    if filename.endswith('.txtp'):
        for prefix, destination in prefix_mapping.items():
            if filename.startswith(prefix):
                shutil.move(filename, destination)
                break

