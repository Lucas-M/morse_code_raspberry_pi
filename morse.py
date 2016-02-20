# Morse Code for Raspberry Pi 2
# 
# Code will ask for a word, iterate through each letter in the word. 
# As it does so, it fires of GPIO 17 for the long and short signals
# of the letters.
# 
# I should redo this code with django and use web interface...with material
# design. I think using Polymer components would be the most fun.


# Author: Lucas Macdonald

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

short_beep = .1
long_beep  = .3 

alphabet = {
    "a":[ 1, 0],
    "b":[ 0, 1, 1, 1],
    "c":[ 0, 1, 0, 1],
    "d":[ 0, 1, 1],
    "e":[ 1],
    "f":[ 1, 1, 0, 1],
    "g":[ 0, 0, 1],
    "h":[ 1, 1, 1, 1],
    "i":[ 1, 1],
    "j":[ 1, 0, 0, 0],
    "k":[ 1, 0, 1, 1],
    "l":[ 1, 0, 1, 1],
    "m":[ 0, 0],
    "n":[ 0, 1],
    "o":[ 0, 0, 0],
    "p":[ 1, 0, 0, 1],
    "q":[ 0, 0, 1, 0],
    "r":[ 1, 0, 1],
    "s":[ 1, 1, 1],
    "t":[ 0],
    "u":[ 1, 1, 0],
    "v":[ 1, 1, 1, 0],
    "w":[ 1, 0, 0],
    "x":[ 0, 1, 1, 0],
    "y":[ 0, 1, 0, 0],
    "z":[ 0, 0, 1, 1]
        }

def beep(length):
#    print ("LED on")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(length)
#    print ("LED off")
    GPIO.output(17,GPIO.LOW)
    time.sleep(.4)

def mprint(word):
    for letter in word:
        print(chr(13) + letter)
        for bit in alphabet[letter]:

            if bit == 0:
                beep(short_beep)
            if bit == 1:
                beep(long_beep)

word = ""
print(chr(27) + "[2J")
while word != "quit":
    word = input("Your word: ")
    mprint (word)

GPIO.cleanup()







