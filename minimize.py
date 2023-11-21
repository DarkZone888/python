import pyautogui
import time
import sys
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import subprocess
import requests
from datetime import datetime, timedelta
import os



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
        print(Fore.GREEN + "[INFO] Starting")
        return name
    else:
        print(Fore.YELLOW + "[INFO] No name found!")
        name = input(Fore.GREEN + "[INFO] Enter your name: ")
        writename(filename, name)
        print(Fore.RED + "[INFO] Name saved!")
        return name

def main():
    name = getname()
    pyautogui.getWindowsWithTitle(f"Roblox {name}")[0].minimize()
    time.sleep(10)


if __name__ == "__main__":
    while hwids in r.text:
        main()
    else:
        print(Fore.CYAN + "Not found your HWID??")
        print(Fore.GREEN + "HWID: " + hwids)
        os.system('pause >NUL')