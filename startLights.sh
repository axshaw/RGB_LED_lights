#!/bin/bash
sleep 15
python /home/pi/kidsLights/changeLightsConsumer.py "*.colour" &
python /home/pi/kidsLights/changeLightsConsumer.py "*.brightness" &
python /home/pi/kidsLights/IR.py &
node /home/pi/kidsLights/lightsGetColour-nodejs/app.js &
