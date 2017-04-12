#!/usr/bin/env python
import colorsys
import os
import time
import sys

os.system('pigs p 17 0')
os.system('pigs p 27 0')
os.system('pigs p 22 0')

n = 200
while True:
    for i in range(0, n):
        r, g, b = colorsys.hsv_to_rgb(float(i) / float(n), 0.99,1.0)
#        print int(round(r*255,0)), int(round(g*255)), int(round(b*255))
        os.system('pigs p 17 ' + str(int(round(r*255))))
        os.system('pigs p 22 ' + str(int(round(g*255))))
        os.system('pigs p 27 ' + str(int(round(b*255))))
#        time.sleep(0.01)
