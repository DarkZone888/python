import os
import shutil
import time

script_directory = os.path.dirname(__file__)

source_folder = os.path.join(script_directory, "AC")

user_home = os.path.expanduser("~")

target_folder_base_relative_path = "AppData\\Local\\Packages"

target_folder_base = os.path.join(user_home, target_folder_base_relative_path)

target_folder_prefix = "ROBLOXCORPORATION.ROBLOX"

for folder in os.listdir(target_folder_base):
    if folder.startswith(target_folder_prefix):
        target_folder = os.path.join(target_folder_base, folder)

        shutil.copytree(source_folder, os.path.join(target_folder, "AC"), dirs_exist_ok=True)
        print(f"Copy to '{target_folder}' ")
        print("Auto exec Finished")

while True:
    time.sleep(1)