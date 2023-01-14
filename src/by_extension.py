import os
import shutil

# specify the folder path to organize
folder_path = 'path/to/folder'

# get a list of all files in the folder
files = os.listdir(folder_path)

# iterate through the files
for file in files:
    # get the file extension
    extension = os.path.splitext(file)[1]
    # check if file is hidden
    if file.startswith('.') or os.path.isdir(os.path.join(folder_path, file)):
        continue
    if extension == "":
        # handle files without extension
        new_folder = os.path.join(folder_path, "No_Extension")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        # move the file to the new folder
        shutil.move(os.path.join(folder_path, file), os.path.join(new_folder, file))
    else:
        # create a new folder with the file extension as the name (if it doesn't already exist)
        new_folder = os.path.join(folder_path, extension[1:])
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        # move the file to the new folder
        shutil.move(os.path.join(folder_path, file), os.path.join(new_folder, file))

print("All files organized into folders by file type.")
