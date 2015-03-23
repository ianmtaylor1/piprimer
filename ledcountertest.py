#!/usr/bin/env python3

from binaryledcounter import BinaryLEDCounter
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

outputpins = [7,8,10,11,12,13,15,16,18,19,21,22]

c = BinaryLEDCounter(outputpins)
b = BinaryLEDCounter(outputpins[0:4])
g = BinaryLEDCounter(outputpins[4:8])
r = BinaryLEDCounter(outputpins[8:12])

while True:
    for x in range(16):
        b.setvalue(x)
        g.setvalue(x)
        r.setvalue(x)
        sleep(0.25)
    #for x in range(c.maxvalue()):
    #    c.setvalue(x)
    #    sleep(600/2**12)
