# Deej Helper
# - Sets com port in config and restarts Deej
# - https://github.com/omriharel/deej
# WARNING: Currently removes all comments from config - needs switch to ruamel.yaml

import serial.tools.list_ports as ports
import subprocess
import psutil
import yaml

deej_dir = r'C:\Users\FilipK\AppData\Local\Portable\Deej\\'
deej_exe = deej_dir + 'deej.exe'
deej_cfg = deej_dir + 'config.yaml'
ardu_ser = '9&359448A7&0&4' # Leave blank to get first COM device instead

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
    print('No device found with matching serial number.')
    quit()
else:
    print('Device found on port ' + deej_com)

# Exit Deej if runnning
for proc in psutil.process_iter():
    if proc.name() == deej_exe.split('\\')[-1]:
        proc.kill()

# Modify Deej config
with open(deej_cfg) as cfg:
    elm_list = yaml.safe_load(cfg)
    if elm_list['com_port'] != deej_com:
        elm_list['com_port'] = deej_com
        
        with open(deej_cfg, 'w') as cfg:
            yaml.dump(elm_list, cfg)

# Start Deej
# Specify working dir for Deej to load it's config from
process = subprocess.Popen(deej_exe, cwd = deej_dir)
