#!/usr/bin/env python3

# Program to count up numbers and identify primes
import RPi.GPIO as GPIO
from binaryledcounter import BinaryLEDCounter
from sys import argv
from random import randrange
from primecounter import countprime


pinmode = GPIO.BCM
# List of output pins
# The i'th element of this array represents the 2^i bit of our display
outputpins = [4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]
buttonpin = 2

# Set up the GPIO pins and binary counter
GPIO.setmode(pinmode)
GPIO.setwarnings(False)
c = BinaryLEDCounter(outputpins)
GPIO.setup(buttonpin,GPIO.IN)

# Find out where we should start
if len(argv)==1:
    start = c.getvalue()
elif (argv[1]=='random')or(argv[1]=='rand'):
    start = randrange(0,c.maxvalue()+1)
else:
    start = int(argv[1])
c.setvalue(start)
print("Start: {}".format(start))

# Loop infinitely, counting to a new prime every time user hits enter
x = start
while True:
    GPIO.wait_for_edge(buttonpin,GPIO.FALLING)
    y = countprime(x+1,c,0.2)
    print('{s} {d} {e}'.format(s=x,d='.'*(y-x-1),e=y))
    x = y
