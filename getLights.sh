#!/bin/bash
if [ "$NODE_ENV" == "development" ]; then
	if [ ! -f ./devColourState.txt ]; then
		echo "0 0 0"
	else
	  cat ./devColourState.txt
  fi
else
    redLight=$(pigs gdc 27)
    greenLight=$(pigs gdc 17)
    blueLight=$(pigs gdc 22)

    echo $redLight $greenLight $blueLight
fi
