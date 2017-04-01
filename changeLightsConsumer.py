#!/usr/bin/env python
import pika
import sys
import os 
import subprocess
import signal

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='changeLights',type='topic')
result = channel.queue_declare(exclusive=True, durable=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='changeLights',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    global submode;
    try:
        print("trying submode kill")
        submode.terminate()
    except Exception, e:
        print("failed kill ")
        print sys.exc_info()
        pass

    if body=="rainbow":
        print("entering rainbow mode")
        submode=subprocess.Popen(['python','/home/pi/kidsLights/rainbow.py'],preexec_fn=os.setsid)
    else:
        submode=subprocess.Popen('/home/pi/kidsLights/changeLights.sh ' + body,preexec_fn=os.setsid, shell=True)
        #os.system('/home/pi/kidsLights/changeLights.sh ' + body)


channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()
