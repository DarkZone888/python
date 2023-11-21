import os
import shutil
import time


user_home = os.path.expanduser("~")

root_folder_relative_path = 'AppData\\Local\\Packages'


root_folder = os.path.join(user_home, root_folder_relative_path)

def find_and_delete_http_and_logs_folders(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for directory in dirs:
            if directory.startswith('ROBLOXCORPORATION.ROBLOX'):
                package_folder = os.path.join(root, directory)
                local_state_folder = os.path.join(package_folder, 'AC')
                http_folder = os.path.join(local_state_folder, 'autoexec')

                if os.path.exists(http_folder):
                    try:
                        shutil.rmtree(http_folder)
                        print(f'Successfully deleted "{http_folder}"')
                    except Exception as e:
                        print(f'Error deleting "{http_folder}": {str(e)}')

while True:
    find_and_delete_http_and_logs_folders(root_folder)
    time.sleep(5)