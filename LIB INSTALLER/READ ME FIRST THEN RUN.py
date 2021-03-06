# Intro: This code allows me to install my packages easily on other computers so I can get to programming quicker. 
# Requirements: Python and Curl before installation (Obviosuly).
# Recomended: Git (Obviously)
# Python:https://www.python.org/
# Curl:https://curl.se/download.html
# Git: https://git-scm.com/downloads
# once visual studio is installed I recomend installing Python and any c++ package 

#imports necessary packages
import os
import zipfile
os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py") #downloads pip
os.system("py get-pip.py") # execute pip for windows
os.system("python get-pip.py") # execute pip for linux
os.system("py -m pip install -u pip") #update pip for windows
os.system("python -m pip install -u pip") #update pip for linux
os.system("pip install pysimplegui") #for gui stuff
os.system("pip install pysimpleguiweb") #for lazy web development
os.system("pip install pyfirmata") #for arduino projects
os.system("pip install 2to3") #To convert outdated python code to recent
os.system("pip install easycv") #To do computer vision easily 
os.system("pip install pywebview") #To build web applications that can also run on dekstop
os.system("pip install OpenCV") #To do computer vision
os.system("pip install flask") #for easy web development
os.system("pip install gunicorn") #for easy web deployment
os.system("curl https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Windows_32bit.zip") #installs arduino command line interface
os.system("curl https://downloads.arduino.cc/arduino-1.8.13-windows.exe") #install standard arduino IDE
os.system("curl https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2021-06/R/eclipse-inst-jre-win64.exe&mirror_id=1281") #installs eclipse
os.system("curl https://atom.io/download/windows_x64") #installs atom
os.system("curl sudo snap install atom --classic") #installs atom
os.system("curl -k -O -L https://npmjs.org/install.sh") #Installs npm
os.system("npm install --global coffeescript") #Installs coffeescript
os.system("curl https://www.autohotkey.com/download/ahk-install.exe") #Installs AutoHotKey
arduino = ZipFile('arduino-cli_latest_Windows_32bit.zip') #creates extraction variable for arduino CLI
arduino.extractall() #extracts arduino CLI
