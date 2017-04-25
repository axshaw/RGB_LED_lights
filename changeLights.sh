#!/bin/bash
if [ "$NODE_ENV" == "development" ]; then
	echo $1 $2 $3 > ./devColourState.txt
else
  echo $1 $2 $3
  pigs p 27 $1
  pigs p 17 $2
  pigs p 22 $3
fi
