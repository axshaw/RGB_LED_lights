#!/usr/bin/env python
import colorsys
import os
import time
import sys
import subprocess

#os.system('pigs p 17 0')
#os.system('pigs p 27 0')
#os.system('pigs p 22 0')

currentLights = subprocess.check_output(['/home/pi/kidsLights/getLights.sh'],shell=True)
print(currentLights)
currentLights = [int(i) for i in currentLights.split()]

while True:
    os.system('pigs p 27 ' + str(0))
    os.system('pigs p 17 ' + str(0))
    os.system('pigs p 22 ' + str(0))
    time.sleep(1)
    os.system('pigs p 27 ' + str(currentLights[0]))
    os.system('pigs p 17 ' + str(currentLights[1]))
    os.system('pigs p 22 ' + str(currentLights[2]))
    time.sleep(1)        
