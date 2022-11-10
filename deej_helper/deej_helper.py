# -*- coding: utf-8 -*-

import serial.tools.list_ports as ports
import subprocess
import argparse
import psutil
import yaml
import os

def get_com_by_sn(serial = ''):
    com_ports = list(ports.comports())
    for i in com_ports:
        if serial == '' or serial == i.serial_number:
            return i.device

def get_com_by_id():
    # Arduino Micro
    pid = '2341'
    hid = '8037'
    com_ports = list(ports.comports())
    for i in com_ports:
        if pid and hid in i.hwid:
            return i.device

# Retrieve CLI arguments
parser = argparse.ArgumentParser(description='Updates Deej config and reloads the app.')
parser.add_argument('--com_port', type=str, help='Manual COM port (optional).')
parser.add_argument('--cfg_path', type=str, help='Manual config path (optional).')
parser.add_argument('--ard_sn', type=str, help='Arduino serial number (optional).')
args = parser.parse_args()

# Setup paths
if args.cfg_path != None:
    deej_dir = args.cfg_path
    print('Manual config path ' + deej_dir + '.')
else:
    deej_dir = os.path.abspath(os.path.dirname(__file__))
    print('Config path ' + deej_dir + '.')

deej_exe = deej_dir + '\deej.exe'
deej_cfg = deej_dir + '\config.yaml'

if not (os.path.exists(deej_exe) and os.path.exists(deej_cfg)):
    print('Deej files not found at the specified path!')
    quit()
    
# Get com device
if args.com_port != None:
    deej_com = args.com_port
elif args.ard_sn != None:
    deej_com = get_com_by_sn(args.ard_sn)  
else:
    deej_com = get_com_by_id()

if deej_com == None:
    print('No device found!')
    quit()
else:
    if args.com_port != None:
        print('Manual device port ' + deej_com + '.')
    elif args.ard_sn != None:
        print('Device s/n ' + args.ard_sn + ' found on port ' + deej_com + '.')
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
