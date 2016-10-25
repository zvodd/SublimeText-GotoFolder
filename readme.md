Goto Folder - For SublimeText
===========

Set up custom launchers from the command pallete, useing file or folder name as input variables.
i.e. Launches programs in the **current file's** folder. e.g Console or File Explorer


### How to:

Ctrl+Shift+P then...

 - Sane defaults are included for Windows:

   - "Goto Folder: Explorer" Opens Windows Explorer in folder of current file.

   - "Goto Folder: Terminal" Opens cmd in folder of current file.



### Install

 - Install package

 - Use `Preferences -> Package Settings -> GotoFolder -> Edit Settings` to edit shell "launchers".
   This allows you to set up a shell command to launch with variable arguments e.g. "file name" or "directory name".

 - Use `Preferences -> Package Settings -> GotoFolder -> Edit Commands` to add command pallete commands to execute "launchers".
   (This is just for adding the shortcut to the command pallete)
   In Linux uncomment the "bash" line and comment the "cmd" line. *untested*
