# Deej Helper

Updates Deej COM port and restarts the app.  
https://github.com/omriharel/deej  

Requirements (`python -m pip install MODULE`):  
- `pyserial`
- `psutil`

CLI arguments:  
- `--cfg_path`: (optional) manual Deej folder path, uses script path if not specified
- `--com_port`: (optional) manual COM port
- `--ard_sn`: (optional) device serial number to determine COM port

Notes:  
`com_port` takes priority over `ard_sn`.  
If neither is specified, Arduino Micro hwid is used to find the device port.