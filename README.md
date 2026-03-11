# Export PNG Scratch Draw

This Python program lets you export to PNG a file created with the Scratch project [Scratch Draw](https://scratch.mit.edu/projects/782765473/).
To run the script, download it first. Also make sure the required libraries are installed (see [Libraries used](#libraries-used)).

## Open and export an image

To open an image, click "Open and export a file" in the main menu.

### Opening
You have two ways to open your file:
- [Open from clipboard](#open-from-clipboard)
- [Open a plain text file](#open-a-plain-text-file)

#### Open from clipboard
Click "Open a file by pasting from the clipboard".
Paste the Scratch Draw file into the text input, then click "Validate".

#### Open a plain text file
Click "Open a plain text file", then "Open the file".
Select the file you want to open. Warning: it must be a plain text file.

### Opening complete
When opening is finished, click "Save image" and choose the directory where you want to save your image.
Once your image is saved, the export is complete.
You can return to the main menu, or click "Show in File Explorer".

## Libraries used

This program uses the following libraries:

- Tkinter
- PIL
- logging
- os
- platform
- subprocess
- pathlib

Make sure these libraries are installed on your computer. Otherwise, you won't be able to run the script.

## Settings

You can configure this application.
Note that the settings are stored in the file "Réglage.txt". If you modify / delete / move this file, the application may misbehave. This file must be in the same directory as the script main.py.

### Language setting
You can choose French or English for the language.

### Log setting
You can choose the logging level:
- Debug
- Info
- Warning
- Error
- Fatal

If you want to modify the script, set the log level to Debug to get usage information. If you only want to use the application, set it to Error for example.