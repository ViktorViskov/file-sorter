#!/usr/bin/python3
from os import listdir
from os import mkdir
from os.path import isdir
from shutil import move

import settings


def create_folder(path_to_folder: str) -> None:
    if not isdir(path_to_folder):
        mkdir(path_to_folder)

def detect_folder_by_type(file_type: str) -> str:
    # default folder
    targeted_folder = "other"

    for f_type in settings.file_rools:
        if file_type in settings.file_rools[f_type]:
            targeted_folder = f_type
            break

    return targeted_folder

download_folder_path = "%s/%s" % (settings.home_directory, settings.download_folder)
target_folder_path = "%s/%s" % (settings.home_directory, settings.move_to)

# check for target folder
create_folder(target_folder_path)

# get all files in directory
files = listdir(download_folder_path)

# start loop for moving
for file_name in files:
    file_name_splitted = file_name.split(".")
    file_type = file_name_splitted[len(file_name_splitted) - 1].lower()

    folder_for_file = detect_folder_by_type(file_type)

    create_folder(f"{target_folder_path}/{folder_for_file}")

    print("moving %s to %s" % (file_name, folder_for_file))
    move(f"{download_folder_path}/{file_name}", f"{target_folder_path}/{folder_for_file}")

