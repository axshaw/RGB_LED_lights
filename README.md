
Youll need to install RabbitMQ
http://www.rabbitmq.com/install-debian.html

PiGPIO
follow instructions here http://popoklopsi.github.io/RaspberryPi-LedStrip/#!/

nodejs (for web interface)
https://www.raspberrypi.org/forums/viewtopic.php?p=1106738#p1106738

reactjs


changeLightsConsumer.py - listens to queues for messages with instructions to change lights - calls changeLights.sh
manualChangeLightsEmitter.py - allows lights to be changed via the queues
IR.py catches the Infrared remote commands and translates these into queue commands

getlights.sh - returns the current colour
changeLights.sh - calls pigs with is a PIGPIO command that sets the RGB value for the lights

startlights.sh is run from /etc/rc.local at startup


********* WEB ADMIN ******************
lightsGetColour-nodejs - express service to access and set light state (included in startup.sh)
lights-web - React web app for website - current start with npm start (not included in startup.sh)



to change lights run ./changeLights.sh with RGB vaules e.g
./changeLights.sh 255 0 255
the above command should light up in purple.


