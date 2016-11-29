import lirc
import os
import threading
import subprocess

sockid = lirc.init("/home/pi/kidsLights/IR.py","/home/pi/.lircrc")
print("Ready")
thread='stopped'


def doit(arg):
      t = threading.currentThread()
      thread="running"
      while getattr(t, "do_run", True):
          print('================= thread =====================')
          print (arg)
          os.system(arg)
          


while True:
#wait for button press - this will need changing to queue to accept non IR changes
	code = lirc.nextcode()
#when IR pressed check if threads are running and kill
        if thread=='running':
            t.do_run = False
            t.join()
            thread='stopped'
 	
        if code:  print(code[0])
#set command to run         
        argsCmd=code[0]
        print('args')
        print(argsCmd)
#        os.system(argsCmd)
#run command in thread
        t = threading.Thread(target=doit, args=(argsCmd,))
        t.daemon = True
        t.start()
