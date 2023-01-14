# organize_folder

The above code is a python script that organizes all files in a specified folder into new folders based on their file type. The script starts by importing the os and shutil modules, which are used to interact with the file system.

The first step is to specify the path to the folder that you want to organize. This is done by setting the value of the folder_path variable to the desired path.

Next, the script gets a list of all files in the specified folder using the os.listdir() function. It then iterates through each file in the list using a for loop.

For each file, the script first extracts the file extension using the os.path.splitext() function. The os.path.splitext() function returns a tuple containing the file name and the file extension. The script then uses indexing to retrieve only the extension.

The script then checks whether the file is hidden by using the file.startswith('.') condition. If the file name starts with a period, it is considered a hidden file and is skipped. The script also checks if the file is a directory using os.path.isdir(os.path.join(folder_path, file)), if it is, it is also skipped.

If the file has no extension, the script creates a new folder called "No_Extension" in the specified folder and moves the file to this folder using the shutil.move() function. If the file has an extension, the script creates a new folder with the same name as the extension and moves the file to this folder. If the folder with the same name as the extension already exists, the file is moved to that folder.

Once the for loop completes, the script prints a message to indicate that the files have been organized into folders by file type.
