# -*- coding: utf-8 -*-

# Deej Helper
# - Sets com port in config and restarts Deej
# - Add device serial to config or leave blank to use first device found
# - https://github.com/omriharel/deej
# WARNING: Currently removes all comments from config - needs switch to ruamel.yaml

import serial.tools.list_ports as ports
import subprocess
import argparse
import psutil
import yaml

def get_com_device(serial = ''):
    com_ports = list(ports.comports())
    for i in com_ports:
        if serial == '' or serial == i.serial_number:
            return i.device

# Retrieve CLI arguments
parser = argparse.ArgumentParser(description='Updates Deej config and restarts the app.')
parser.add_argument('--com_port', type=str, help='Enforces COM port.')
args = parser.parse_args()

# Get values from config
help_cfg = 'config.yaml'

with open(help_cfg) as cfg:
    elm_list = yaml.safe_load(cfg)
    deej_dir = elm_list['deej_dir']
    ardu_ser = elm_list['ardu_ser']

deej_exe = deej_dir + 'deej.exe'
deej_cfg = deej_dir + 'config.yaml'

# Get com device
if args.com_port != None:
    deej_com = args.com_port
else:
    deej_com = get_com_device(ardu_ser)  

if deej_com == None:
    print('No device found using ' \
          + 'com device lookup.' \
          if ardu_ser == '' \
          else 'serial no. match.')
    quit()
else:
    if args.com_port != None:
        print('Device port enforced ' + deej_com + '.')
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
