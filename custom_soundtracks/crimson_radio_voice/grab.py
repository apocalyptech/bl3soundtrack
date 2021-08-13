#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys
import shutil
sys.path.append('/home/pez/git/b2patching/bl3mods/python_mod_helpers')
from bl3data.bl3data import BL3Data

data = BL3Data()

vo_path = '/games/bl3_decrypt/extracted_audio/bl3-txtp/vo'

for obj_name in data.find('/Game/InteractiveObjects/GameSystemMachines/BroadcastRadio/_Design', 'BroadcastRadio_'):
    last_bit = obj_name.split('/')[-1]
    os.makedirs(last_bit, exist_ok=True)
    obj = data.get_data(obj_name)
    for export in obj:
        if 'ChannelRadio' in export:
            for short, long in export['ChannelRadio']:
                txtp_name = '{}.txtp'.format(short[3:])
                full_txtp = os.path.join(vo_path, txtp_name)
                if not os.path.exists(full_txtp):
                    txtp_name = '{} {{r}}.txtp'.format(short[3:])
                    full_txtp = os.path.join(vo_path, txtp_name)
                    if not os.path.exists(full_txtp):
                        print('NOT FOUND: {} -> {}'.format(last_bit, full_txtp))
                        continue
                shutil.copy(full_txtp, last_bit)

for obj_name in data.find('/Game/InteractiveObjects/GameSystemMachines/BroadcastRadio/_Design', 'MissionRadio_'):
    last_bit = obj_name.split('/')[-1]
    os.makedirs(last_bit, exist_ok=True)
    obj = data.get_data(obj_name)
    for export in obj:
        if 'MissionRadio' in export:
            for mission_audio in export['MissionRadio']:
                we_name = mission_audio['Audio_2_3F0ACAA8484CEE8E4FAF2FB155EE9610'][0]
                txtp_name = '{}.txtp'.format(we_name[3:])
                full_txtp = os.path.join(vo_path, txtp_name)
                if not os.path.exists(full_txtp):
                    print('NOT FOUND: {} -> {}'.format(last_bit, full_txtp))
                    continue
                shutil.copy(full_txtp, last_bit)

