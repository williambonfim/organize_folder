# Organize Files by Extension

This script is designed to organize all the files in a specified folder into new folders, with each folder being named after the file extension of the files it contains. The script will also handle files without an extension, placing them in a folder named "No_Extension". Hidden files and existing folders will be ignored.

To use the script, you will first need to specify the path to the folder you want to organize:

```
folder_path = 'path/to/folder'
```

The script will then use the os and shutil modules to get a list of all the files in the specified folder and iterate through them. For each file, the script will:

1. Get the file extension using os.path.splitext(file)[1].
2. Check if the file is hidden or is an existing folder using file.startswith('.') or os.path.isdir(os.path.join(folder_path, file)). If it is, the script will ignore the file and move on to the next one.
3. If the file does not have an extension, it will be moved to a folder named "No_Extension", which will be created if it does not already exist.
4. If the file does have an extension, the script will create a new folder with the same name as the extension (without the "."), and move the file into it. If the folder already exists, the file will simply be moved into it.
Finally, the script will print a message to confirm that all the files have been organized into folders by file type.
```
print("All files organized into folders by file type.")
```
