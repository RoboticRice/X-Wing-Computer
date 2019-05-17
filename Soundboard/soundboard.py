#!/usr/bin/python

# Created by RoboticRice
# https://github.com/RoboticRice
# Inspired by:
#	https://makezine.com/projects/make-33/simple-soundboard/

print "Luke, you've switched off your tageting computer. What's wrong?"

import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)

#Set-Up Usable Inputs for Buttons
#2 = SDA
#3 = SCL
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#7 = CE1
#8 = CE0
#9 = MISO
#10 = MOSI
#11 = SCLK
#14 = TXD0
#15 = RXD0
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init(48000, -16, 1, 1024)

#Set-Up Sound Files
#pygame.mixer.music.load("OTHER/Comm chatter.wav") #future implimentation - for now, it's too quite to test with
pygame.mixer.music.load("OTHER/Cantina band.wav")
pygame.mixer.music.queue("OTHER/Cantina band 2.wav")
pygame.mixer.music.queue("OTHER/Cantina band 3.wav")
fire1 = pygame.mixer.Sound("XWING/XWing fire.wav")
fire2 = pygame.mixer.Sound("XWING/XWing fire 2.wav") #need to edit wav file to remove leading dead space
fire3 = pygame.mixer.Sound("XWING/XWing fire 3.wav")

#Set-Up Audio Channels (each channel plays audio seperate from the other)
ChannelA = pygame.mixer.Channel(2) #Sound Effects
#ChannelB = pygame.mixer.Channel(2) #Sound Effects
#ChannelC = pygame.mixer.Channel(2) #Sound Effects
pygame.mixer.music.play(-1)

print "Nothing. I'm all right."

while True:
    try:
        if (GPIO.input(4)  == False):
            ChannelA.play(fire1)
        if (GPIO.input(17) == False):
            ChannelA.play(fire2)
        if (GPIO.input(18) == False):
            ChannelA.play(fire3)
        if (GPIO.input(22) == False):
            pygame.mixer.music.fadeout(250)
        if (GPIO.input(23) == False):
            pygame.mixer.music.play(-1)
        sleep(.01)
    except KeyboardInterrupt:
    	pygame.mixer.music.stop()
    	print "YAHOOOOO! You're all clear, kid."
        exit()