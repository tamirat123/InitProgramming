from re import I
import subprocess
import time 
import datetime
import os 
#from Colorama import *
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
ping_web = input("Input site: ")

ip = subprocess.call("ipconfig",shell=True)
#print("Your ip address is " + str(ip))

while True:
    output = os.popen("ping " + ping_web)
    stream = output.read()
    print("ping to " + ping_web + " completed") 
    pingsave = open("output.txt","w")
    pingsave.writelines(stream) 
    time.sleep(10) 

pringsave.close()