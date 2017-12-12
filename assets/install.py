import os
import sys
import urllib.request
import winreg
import subprocess
import pip


files = ["comaJudgeHandler.py",
         "commandLineHandler.py",
         "remoteHandler.py",
         "remoteLoop.py",
         "systemHandler.py",
         "testHandler.py"]
starter = "comajudgetool.bat"
localfolder = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\sinsam\\comajudgetools\\"
libfolder = localfolder + "lib\\"
base_url = "http://ramsesoriginal.info/assets/"

if not os.path.exists(localfolder):
    print("Creating Application Folder")
    os.makedirs(localfolder)
if not os.path.exists(libfolder):
    os.makedirs(libfolder)
for file in files:
    print("Downloading " + file)
    urllib.request.urlretrieve(base_url + file, libfolder + file)
print("Downloading " + starter)
urllib.request.urlretrieve(base_url + starter, localfolder + starter)

print("Installing ssh library")
pip.main(['install', "paramiko"])

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_READ)
val = winreg.QueryValueEx(key, "PATH")[0]

res = command = 'setx PATH "' + val + ';' + localfolder + ''
if localfolder not in val:
    print("Adding to %PATH%")
    try:
        subprocess.run(command, shell=True, timeout=30)
        print("Added")
    except Exception:
        pass
print("Installation Complete, enjoy the comajudgetool")