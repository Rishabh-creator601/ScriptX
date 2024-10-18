## Scriptx 

- It is a pyqt5 application used to write files for rough purposes 

## Versions 

- currenty it has three  tabs as follows 

<img src="./assets/tab1.png" width="500px" height="500px" />
<img src="./assets/tab2.png" width="500px" height="500px" />

- Third Tab is settings which is your personal paths 


## For code 

- Just do as follows :
<code> git clone https://github.com/Rishabh-creator601/ScriptX.git </code> <br />
<code> python main.py</code>


## For exe

1) ENV settings 
- Save the ".env" file in C:/users/<yourname>/.Scripts/ || choose the path that is editable & not required by admin
- Change the same path in "main.py" | "enlarged_windows .py" | "file_tools.py" of VAR "DOT_ENV_PATH"

2) Build by PyInstaller 
 - <code> python -m PyInstaller --onedir --windowed main.py </code> 
 - Save the "exe" and "_internal" under C:/Program Files/Scriptx/
 - Save the "assets" folder under C:/Program Files/Scriptx/dist/
 > under dist folder the exe will detected by antivirus but it is only one time 

3) Add the exe to "regedit" for custom access 



## Some good things about GUI 

- Any change to the ui will need the whole app to rebuild just the replace the new ui to the assets folder (hence you can edit it on your own ) or just download from upcoming ui's
- only when change in functionality is required when to rebuild the app 



**Feel free to offer suggestion**
