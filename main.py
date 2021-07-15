# PiicoDev VEML6030 minimal example code
# This program reads touch data from the PiicoDev CAP1203 capacitive touch sensor and displays the result

import sys
from PiicoDev_CAP1203 import PiicoDev_CAP1203
from time import sleep

touchSensor = PiicoDev_CAP1203(touchmode="multi",sensitivity=6) #touchmode="multi") #single/multi sensitivity (7 - 0), where 0 is most sensitive
touchSensor2 = PiicoDev_CAP1203(bus=1, touchmode="multi",sensitivity=6)
sleep(1)

while True:
    buttons = touchSensor.read()
    try:
        print(str(buttons[0]) + " S1  " + str(buttons[1]) + " S2  " + str(buttons[2]) + " S3")
    except:
        print(".")
        
    buttons = touchSensor2.read()
    try:
        print(str(buttons[0]) + " S1  " + str(buttons[1]) + " S2  " + str(buttons[2]) + " S3")
    except:
        print(".")
    #touchSensor.readDeltaCounts()
    print('------------------')
    
    sleep(1)