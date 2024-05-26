import os
import subprocess
import sys

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(RED + "Error:" + RESET, stderr.decode())
    else:
        print(stdout.decode())

def print_banner():
    print(CYAN + r"""
  __      _______  _    _  _____ _____ _______ _______ ____  _   _ 
  \ \    / /_   _| | |  | |/ ____|  __ \__   __|__   __/ __ \| \ | |
   \ \  / /  | |   | |  | | |    | |__) | | |     | | | |  | |  \| |
    \ \/ /   | |   | |  | | |    |  _  /  | |     | | | |  | | . ` |
     \  /   _| |_  | |__| | |____| | \ \  | |     | | | |__| | |\  |
      \/   |_____|  \____/ \_____|_|  \_\ |_|     |_|  \____/|_| \_|
    """ + RESET)
    print(MAGENTA + "Author: Likhon Sheikh" + RESET)
    print(GREEN + "TapSwap Bot Installer" + RESET)
    print(YELLOW + "Follow for more cool stuff:" + RESET)
    print(BLUE + "https://t.me/RexxCheat" + RESET)
    print(CYAN + "******************************************\n" + RESET)

# Display the banner
print_banner()

# Setup storage and install required packages
run_command('termux-setup-storage')
run_command('pkg update && pkg upgrade -y')
run_command('pkg install git python -y')

# Ensure pip is updated
run_command('python -m pip install --upgrade pip')

# Clone the GitHub repository
os.chdir('/storage/emulated/0')
run_command('git clone https://github.com/RexxCheat/TapSwap-Auto-Clicker.git')

# Navigate into the cloned directory
os.chdir('TapSwap-Auto-Clicker')

# Install required Python packages
run_command('pip install telethon requests aiocron urllib3')

# Ask for user inputs
api_id = input(GREEN + "Enter your API ID: " + RESET)
api_hash = input(GREEN + "Enter your API Hash: " + RESET)
admin_id = input(GREEN + "Enter your Admin ID: " + RESET)
auto_upgrade = input(GREEN + "Enable auto-upgrade (true/false): " + RESET).lower() in ['true', '1', 't', 'y', 'yes']
max_charge_level = input(GREEN + "Enter max charge level: " + RESET)
max_energy_level = input(GREEN + "Enter max energy level: " + RESET)
max_tap_level = input(GREEN + "Enter max tap level: " + RESET)

# Update config.py
config_content = f'''
{{
    "api_id": {api_id},
    "api_hash": "{api_hash}",
    "admin": {admin_id},
    "auto_upgrade": {auto_upgrade},
    "max_charge_level": {max_charge_level},
    "max_energy_level": {max_energy_level},
    "max_tap_level": {max_tap_level}
}}
'''
with open('config.py', 'w') as config_file:
    config_file.write(config_content)

# Install dependencies from requirements.txt (if exists)
if os.path.exists('requirements.txt'):
    run_command('pip install -r requirements.txt')

# Run the main script
run_command('python clicker.py')
