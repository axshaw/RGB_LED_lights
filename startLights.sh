#!/bin/bash
sleep 15
python /home/pi/kidsLights/changeLightsConsumer.py "*.colour" &

python /home/pi/kidsLights/changeLightsConsumer.py "*.brightness" &
python /home/pi/kidsLights/IR.py &
sleep 10
export NODE_ENV="production"
export REACT_APP_LIGHTS_IP="192.168.42.150"
node /home/pi/kidsLights/lightsGetColour-nodejs/app.js &
sudo http-server /home/pi/kidsLights/lights-web/build/ -p 80 &
