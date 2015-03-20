#!/usr/bin/env python3

# Program to count up numbers and identify primes
from math import sqrt
from time import sleep
import RPi.GPIO as GPIO
from binaryledcounter import BinaryLEDCounter
from sys import argv
from random import randrange

# List of output pins
# The i'th element of this array represents the 2^i bit of our display
outputpins = [4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]
buttonpin = 2

def isprime(x):
    """Determine if x is prime."""
    if x<=1:
        return False
    elif (x==2 or x==3):
        return True
    elif (x%2==0):
        return False
    s = int(sqrt(x))
    tocheck = range(3,s+1,2)
    for i in tocheck:
        if x%i==0:
            return False
    else:
        return True

def countprime(start,counter,delay):
    """Starting at the specified value, count and display numbers
    until the next prime is reached, delaying the specified number
    of seconds between each number. The numbers are displayed on the 
    specified BinaryLEDCounter."""
    x = start
    seenprime = False
    while not seenprime:
        counter.setvalue(x)
        if isprime(x):
            seenprime = True
        else:
            x += 1
            sleep(delay)
    return x

# Set up the GPIO pins and binary counter
GPIO.setmode(GPIO.BCM)
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
