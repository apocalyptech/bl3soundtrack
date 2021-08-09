#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import sys
import shutil
import subprocess

dir_mappings = {
        'ambient': set([
            'Amb_',
            'BH_Main_Menu_Amb',
            ]),
        'emitters': set([
            'Emt_',
            ]),
        'enemies': set([
            'ClearSelectior',
            'Crea_',
            'HyperionTurret_',
            ]),
        'cinematics': set([
            'CIN2070_',
            'CIN_',
            'Cin_',
            ]),
        'gear': set([
            'Gear_',
            'Wep_',
            'WEP_',
            ]),
        'invalid': set([
            'leportUserEdgeData_Staticr',
            ]),
        'io': set([
            'IO_',
            ]),
        'music': set([
            'Aeternam_',
            'BlindTheHuntsmen_',
            'Caleb_Tote_',
            'Crimson_',
            'Dandelion_Credits_Music_Start',
            'Drolet_',
            'End_Credits_Music_Hibiscus_Start',
            'Esc_',
            'GhostsFromHome_',
            'Hillward_',
            'HuntTheShark_',
            'James_Dwyer_',
            'JNeroes_',
            'JShields_',
            'Man_Mountain_',
            'MidnightRevel_',
            'Mus_',
            'MUS_',
            'Play_Mus_',
            'Raison_Varner_',
            'RogierVanEtten_',
            'Sean_Ahern_',
            'Somewhere_Here_',
            'The_Axes_of_Kane_',
            'The_Five_Hands_',
            'Video_',
            'Wandermine_',
            ]),
        'npc': set([
            'NPC_',
            ]),
        'pc': set([
            'Cha_',
            'Char_',
            'Pet_',
            ]),
        'projectile': set([
            'Proj_',
            ]),
        'seq': set([
            'SEQ',
            'Seq_',
            ]),
        'sfx': set([
            '1231911762-0004-event',
            '86670768-0005-event',
            'ASB_',
            'bPathFindingBasedTest_SetBitEPq',
            'DecrementActivityCountValueEs',
            'DroneShield_Lp',
            'Elemental_',
            'Emote_',
            'Exp_',
            'Firebal4',
            'Foley_',
            'Footstep_',
            'FS_',
            'Gore-',
            'Gore_',
            'Grenade_',
            'Hib_',
            'Imp_',
            'Impound-0112-event',
            'L_Crawa',
            'League_Travel_',
            'Loop_',
            'Loot_Spawn_',
            'Map_',
            'Mission_',
            'MissionPlaceable_',
            'Mode_',
            'Mov_',
            'Negq',
            'OnReserve_',
            'Phys_Imp_',
            'Play_Mission_',
            'Player_Shared_Anim_',
            'PrepareGameSyncE11AkGroupTypejjbs',
            'Puddle_Leech_',
            'Room_Deco_',
            'SM_Hib_Floor_Custon',
            'SpawnMesh_',
            'Strip-',
            'TC_',
            'TeslaSpike_Lp',
            'TrashTown-',
            'TtAvoidanceSolvet',
            'White_Portal_MemorySpawn',
            'WineBarrel_Knock',
            ]),
        'ui': set([
            'ABS_',
            'HUD-',
            'HUD_',
            'Menu-',
            'Menu_',
            'MenuMap-',
            'UI-',
            'UI_',
            ]),
        'vehicle': set([
            'Veh_',
            ]),
        'vo': set([
            # This first one is various Killavolt lines, though many reference
            # .wem files which don't actually exist
            '2858837790-',
            'Claptrap_Classifieds-',
            'DLC2_VOBD_',
            'ECHO_Logs-',
            'Oak_DLC1_VO_',
            'Oak_DLC1_VOBD_',
            'Oak_DLC1_VOCT_',
            'Oak_DLC1_VOMisc_',
            'Oak_DLC1_VOSQ_',
            'Oak_DLC2_VOBD_',
            'Oak_DLC2_VOCT_',
            'Oak_DLC3_VOBD_',
            'Oak_DLC3_VOCT_',
            'Oak_DLC4_VOBD_',
            'Oak_DLC4_VOCT_',
            'Oak_Live_',
            'Oak_MainMenu_',
            'Oak_Takedown_MAL_VOBD_',
            'Oak_VO_',
            'Oak_VOBD_',
            'Oak_VOCT_',
            'Play_Oak_VO_',
            'VO_',
            'VOBD_',
            'VOSQ_',
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

