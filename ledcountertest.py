#!/usr/bin/env python3

from binaryledcounter import BinaryLEDCounter
import RPi.GPIO as GPIO
from time import sleep
from random import randrange

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

outputpins = [7,8,10,11,12,13,15,16,18,19,21,22]

c = BinaryLEDCounter(outputpins)
# Counters for individual colors
b = BinaryLEDCounter(outputpins[0:4])
g = BinaryLEDCounter(outputpins[4:8])
r = BinaryLEDCounter(outputpins[8:12])

testnumbers = [0,1,2,4,8,16,32,64,128,256,512,1024,2048,
                 1024,512,256,128,64,32,16,8,4,2,1,
               0,273,546,1092,2184,1092,546,273,546,1092,2184,
                 1092,546,273,546,1092,2184,
               0,15,240,3840,240,15,240,3840,240,15,240,3840,
               0,1,3,7,15,31,63,127,255,511,1023,2047,4095,
                 4094,4092,4088,4080,4064,4032,3968,3840,3584,3072,2048,
               0,2048,3072,3584,3840,3968,4032,4064,4080,4088,4092,4094,
                 4095,2047,1023,511,255,127,63,31,15,7,3,1,
               0,1365,2730,1365,2730,1365,2730,1365,2730,
               0]
for x in range(8):
    testnumbers.append(randrange(c.maxvalue()+1))
testnumbers.append(0)

print("Begin {0} second test pattern.".format(len(testnumbers)/4))
for x in testnumbers:
    c.setvalue(x)
    sleep(0.25)
