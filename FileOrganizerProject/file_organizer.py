import os
import shutil

folder_path = input("Enter the folder path to organize: ")

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1]

        new_folder = os.path.join(folder_path, extension.upper())

        # create folder if it does not exist
        os.makedirs(new_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(new_folder, file))

print("Files organized successfully!")