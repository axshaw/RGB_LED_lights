#!/usr/bin/env python
import lirc
import pika
import sys

sockid = lirc.init("/home/pi/kidsLights/IR.py","/home/pi/.lircrc")
#print("IR Ready")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='ChangeLights',type='topic')
routing_key = '*.colour'

while True:
#wait for button press - this will need changing to queue to accept non IR changes
	code = lirc.nextcode()
	#check if out of range
	try:
		message = code[0]
	except IndexError:
		message = '0 0 0'
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='ChangeLights',type='topic')
        routing_key = '*.colour'

        channel.basic_publish(exchange='changeLights',routing_key=routing_key,body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
#        connection.close()
        if code:  print(code[0])
