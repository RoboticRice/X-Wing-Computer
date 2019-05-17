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
#Test this later: New in pygame 2(when compiled with SDL2) - size can be 32 (32bit floats).

#Set-Up Sound Files
pygame.mixer.music.load("OTHER/Com chatter.wav")
#pygame.mixer.music.load("OTHER/OST Cantina Band.wav")
fire1 = "XWING/XWing fire.wav"
fire2 = pygame.mixer.Sound("XWING/XWing fire 2 mod.wav")
fire3 = pygame.mixer.Sound("XWING/XWing fire 3.wav")

#Set-Up Audio Channels (each channel plays audio seperate from the other)
pygame.mixer.set_num_channels(5)
pygame.mixer.set_reserved(0)
ChannelA = pygame.mixer.Channel(0) #Sound Effects
#ChannelB = pygame.mixer.Channel(2) #Sound Effects
#ChannelC = pygame.mixer.Channel(2) #Sound Effects
#pygame.mixer.music.play(-1) #uncomment to start default with music playing

print "Nothing. I'm all right."

while True:
    try:
        if (GPIO.input(4)  == False):
            pygame.mixer.find_channel(True).play(pygame.mixer.Sound(fire1))
        if (GPIO.input(17) == False):
            ChannelA.play(fire2)
        if (GPIO.input(18) == False):
            ChannelA.play(fire3)
        if (GPIO.input(22) == False):
            pygame.mixer.music.fadeout(250)
        if (GPIO.input(23) == False):
            pygame.mixer.music.play(-1)
        sleep(.1)
    except KeyboardInterrupt:
    	pygame.mixer.music.stop()
    	print "YAHOOOOO! You're all clear, kid."
        exit()