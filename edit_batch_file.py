import requests

COMMANDS = """
@echo off
cd C:\\GayApe
gay_ape.exe
"""

enabled = requests.get('https://raw.githubusercontent.com/CalebWebsterJCU/GayApe/master/enabled.txt')
enabled.raise_for_status()

if enabled.text == 'True':
    # Write commands
    with open('C:\\GayApe\\run_gay_ape.bat', 'w') as batch_file:
        print(COMMANDS, file=batch_file)
else:
    # Erase batch file
    with open('C:\\GayApe\\run_gay_ape.bat', 'w') as batch_file:
        print('', file=batch_file)
