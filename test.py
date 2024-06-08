import subprocess

import keyboard

# while not keyboard.is_pressed('e'):
#     print('1')

# subprocess.Popen('dmidecode.exe -s system-uuid'.split())
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print(current_machine_id)