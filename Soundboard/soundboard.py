#!/usr/bin/python

# Created by RoboticRice
# https://github.com/RoboticRice
# Inspired by:
#	https://makezine.com/projects/make-33/simple-soundboard/

print "Luke, you’ve switched off your targeting computer. What’s wrong?"

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
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init(48000, -16, 1, 1024)

#Set-Up Sound Files
sndA = pygame.mixer.Sound("Wilhelm Scream.wav")
sndB = pygame.mixer.Sound("R2/WEEEOOOOWW.wav")
#sndC = pygame.mixer.Sound("OTHER/Cantina band.wav")

#Set-Up Audio Channels (each channel plays audio seperate from the other)
bChannel = pygame.mixer.Channel(1) #Background Sound
sChannel = pygame.mixer.Channel(2) #Sound Effects

print "Nothing. I'm all right."

while True:
   try:
      if (GPIO.input(4)  == False):
         bChannel.play(sndA)
      if (GPIO.input(17) == False):
         sChannel.play(sndB)
      sleep(.01)
   except KeyboardInterrupt:
      exit()