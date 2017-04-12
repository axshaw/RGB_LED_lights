#!/bin/bash
sleep 15
python /home/pi/kidsLights/changeLightsConsumer.py "*.colour" &

python /home/pi/kidsLights/changeLightsConsumer.py "*.brightness" &
python /home/pi/kidsLights/IR.py &
sleep 10
EXPORT NODE_ENV="production"
node /home/pi/kidsLights/lightsGetColour-nodejs/app.js &
sudo http-server /home/pi/kidsLights/lights-web/build/ -p 80
