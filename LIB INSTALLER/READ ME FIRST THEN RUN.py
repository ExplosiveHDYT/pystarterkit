# Intro: This code allows me to install my packages easily on other computers so I can get to programming quicker. 
# Requirements: Python and Curl before installation (Obviosuly).
# Recomended: Git (Obviously)
# Python:https://www.python.org/
# Curl:https://curl.se/download.html
# Git: https://git-scm.com/downloads


#imports necessary packages
import os
os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py") #downloads pip
os.system("py get-pip.py") # execute pip for windows
os.system("python get-pip.py") # execute pip for linux
os.system("py -m pip install -u pip") #update pip for windows
os.system("python -m pip install -u pip") #update pip for linux
os.system("pip install pysimplegui") #for gui stuff
os.system("pip install pysimpleguiweb") #for lazy web development
os.system("pip install pyfirmata") #for arduino projects
os.system("pip install 2to3") #To convert outdated python code to recent
os.system("pip install SimpleCV")#To do computer vision easily (when its eventually updated)
os.system("pip install OpenCV") #To do computer vision