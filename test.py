import subprocess
from getmac import get_mac_address as gma
import keyboard
import machineid
import requests
import configparser

# while not keyboard.is_pressed('e'):
#     print('1')

# subprocess.Popen('dmidecode.exe -s system-uuid'.split())
# current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# print(gma())
# print(current_machine_id)
# print(machineid.id())

# result = requests.get('http://localhost:8095/check_link', data={'token': '272364c8-f0a5-414e-96cd-3f13d726f19e'})
# print(result.json())

config = configparser.ConfigParser()
config.read('conf.conf')
print(config['DEFAULT']['Token'])
# token = config['DEFAULT']['Token']
# exit_hotkey = config['DEFAULT']['ExitHotkey']
# print(token)
# print(exit_hotkey)