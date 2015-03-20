#!/usr/bin/env python3

# Program to count up numbers and identify primes
import RPi.GPIO as GPIO
from binaryledcounter import BinaryLEDCounter
from sys import argv
from random import randrange
from primecounter import countprime
from threading import Thread, Lock

# Mode that pin numberings will be in
pinmode = GPIO.BCM
# List of output pins
# The i'th element of this array represents the 2^i bit of our display
outputpins = [4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]
# Pin which is connected to the button, with a PULL UP resistor
buttonpin = 2
# Speed at which the primer should count (numbers/second)
speed = 5

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

# Lock to keep threads from counting at the same time and global value
counterlock = Lock()
value = start

# Function for thread that waits on button press
def buttonwait():
    global value
    global c
    global speed
    while True:
        GPIO.wait_for_edge(buttonpin,GPIO.FALLING)
        with counterlock:
            y = countprime(value+1,c,1.0/speed)
            print('{s} {d} {e}'.format(s=value,d='.'*(y-value-1),e=y))
            value = y

# Function for thread that waits on enter key
def keyboardwait():
    global value
    global c
    global speed
    while True:
        input()
        with counterlock:
            y = countprime(value+1,c,1.0/speed)
            print('{s} {d} {e}'.format(s=value,d='.'*(y-value-1),e=y))
            value = y

# Start all input threads, then wait to join
threads = [Thread(target=buttonwait), Thread(target=keyboardwait)]
for t in threads:
    t.daemon=True
    t.start()
try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print()

