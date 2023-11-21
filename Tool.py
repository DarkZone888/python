import time
import os
import sys
import pyautogui
import pygetwindow as ex
import subprocess
import requests
from datetime import datetime, timedelta
from colorama import Fore, Back, Style, init
import psutil

init()

hwids = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/tHKGxHJA")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def readname(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def writename(filename, hwid):
    with open(filename, 'w') as file:
        file.write(hwid)

def getname():
    filename = "name"
 
    name = readname(filename)
    if name is not None:
        print(Fore.WHITE + "[INFO] Staring All Function!")
        return name
    else:
        print(Fore.YELLOW + "[INFO] No name found!")
        name = input(Fore.GREEN + "[INFO] Enter your name: ")
        writename(filename, name)
        print(Fore.RED + "[INFO] Name saved!")
        return name


def main():
        num1 = 0
        now = datetime.now()
        current_time = now.strftime("%m/%d/%Y | %H:%M")

        print(Fore.GREEN + "[Exotic Tool] - 21/8/66")
        print(Fore.LIGHTCYAN_EX + "Starting Process at", current_time)
        print("")
        print(Fore.RED + "[Function]")
        print(Fore.YELLOW + "-[Auto Resize]")
        print(Fore.MAGENTA + "-[Auto Minimized]")
        print(Fore.BLUE + "-[Check roblox process]")
        print("")
        print(Fore.LIGHTRED_EX + "[Roblox Process]")
        

        for p in psutil.process_iter(attrs=['pid', 'name']):
            if p.info['name'] == "Windows10Universal.exe":
                num1 += 1
                name = getname()
                roblox = ex.getWindowsWithTitle(f"Roblox {name}")[0]
                os.system("title Exotic Tool [ Roblox : {} ]".format(num1))
                print(Fore.CYAN + "[INFO] - ROBLOX UWP {}".format([num1]), [(p.info['pid'])])
                roblox.minimize()
                time.sleep(10)
        num1 = 0
        time.sleep(3)
        os.system("cls")
        


if __name__ == "__main__":
    while hwids in r.text:
        main()
    else:
        print(Fore.CYAN + "Not found your HWID??")
        print(Fore.GREEN + "HWID: " + hwids)
        os.system('pause >NUL')
       


