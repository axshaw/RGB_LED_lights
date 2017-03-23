#!/usr/bin/env python
import colorsys
import time
import subprocess

#hsv = colorsys.rgb_to_hsv(int(1),int(0),int(1))

#print(hsv)

output=subprocess.check_output('/home/pi/kidsLights/getLights.sh')
#subprocess.call(["/home/pi/kidsLights/getLights.sh"], stdout=subprocess.PIPE)
print('original read from gpio RGB values')
print(output)
rgb = map(int, output.split())

i=0
while i < 3: 
  print(rgb[i])
  hsvValue = rgb[i] / float(255)
  rgb[i]=float(hsvValue)
  i += 1

print('RGB version ranged between 0 - 1')
print(rgb)

print('------------------------------------------')

#convert curent rgb colour to hsv
h,s,v=colorsys.rgb_to_hsv(*rgb)
print('RGB converted to HSV')
print(h)
print(s)
print(v)

#reduce the number of v 
i=0
hsv2=[]
while i < 3:
  if(i==0):
    hsvValue2 = float(h)*360
  elif i==2:
    hsvValue2 = float(v)*100
    if(v>0.2):
      v = v-0.10
  
  else:
    hsvValue2 = float(s)*100
    
  hsv2.append(int(hsvValue2))
  
  i += 1
print("hsv readable")
print(hsv2)

#convert hsv to rgb
print('RGB New values')
r,g,b=colorsys.hsv_to_rgb(h,s,v)

print(r*255)
print(g*255)
print(b*255)
#return new rgb

nR = int(r*255)
nG = int(g*255)
nB = int(b*255)

subprocess.call('/home/pi/kidsLights/changeLights.sh '+ str(nR) +' '+ str(nG) +' '+ str(nB), shell=True)
