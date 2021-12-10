# -*- coding: utf-8 -*-

# Deej Helper
# - Sets com port in config and restarts Deej
# - Add device serial to config or leave blank to use first device found
# - https://github.com/omriharel/deej
# WARNING: Currently removes all comments from config - needs switch to ruamel.yaml

import serial.tools.list_ports as ports
import subprocess
import psutil
import yaml

# Get values from config
help_cfg = 'config.yaml'

with open(help_cfg) as cfg:
    elm_list = yaml.safe_load(cfg)
    deej_dir = elm_list['deej_dir']
    ardu_ser = elm_list['ardu_ser']

deej_exe = deej_dir + 'deej.exe'
deej_cfg = deej_dir + 'config.yaml'

# Get com devices
com_ports = list(ports.comports())
for i in com_ports:
    if ardu_ser == '':
        deej_com = i.device
        break
    else:
        if i.serial_number == ardu_ser:
            deej_com = i.device
            break

try:
    deej_com
except NameError:
    print('No device found using ' \
          + 'com device lookup.' \
          if ardu_ser == '' \
          else 'serial no. match.')
    quit()
else:
    print('Device found on port ' + deej_com + '.')

# Exit Deej if runnning
for proc in psutil.process_iter():
    if proc.name() == deej_exe.split('\\')[-1]:
        proc.kill()

# Modify Deej config
with open(deej_cfg) as cfg:
    elm_list = yaml.safe_load(cfg)
    if elm_list['com_port'] != deej_com:
        elm_list['com_port'] = deej_com
        print('Deej config updated.')
        
        with open(deej_cfg, 'w') as cfg:
            yaml.dump(elm_list, cfg)

# Start Deej
# Specify working dir for Deej to load it's config from
process = subprocess.Popen(deej_exe, cwd = deej_dir)
print('Deej started')
