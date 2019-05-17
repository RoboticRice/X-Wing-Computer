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
fire2 = "XWING/XWing fire 2 mod.wav"
fire3 = pygame.mixer.Sound("XWING/XWing fire 3.wav")

#Set-Up Audio Channels (each channel plays audio seperate from the other)
pygame.mixer.set_num_channels(5)
pygame.mixer.set_reserved(0)
ChannelA = pygame.mixer.Channel(0) #Sound Effects
#ChannelB = pygame.mixer.Channel(2) #Sound Effects
#ChannelC = pygame.mixer.Channel(2) #Sound Effects


#Init the button press stuff
status = [False]*5 #currently using 5 inputs
counter = 0

print "Nothing. I'm all right."

#pygame.mixer.music.play(-1) #uncomment to start default with music playing
while True:
    try:
    	in0 = GPIO.input(4)
    	in1 = GPIO.input(17)
    	in2 = GPIO.input(18)
    	in3 = GPIO.input(22)
    	in4 = GPIO.input(23)

    	#This will play once, when pressed
        if (in0  == False):
            if (status[0] == False): #not triggered, but should have
    			pygame.mixer.find_channel(True).play(pygame.mixer.Sound(fire1))
    			status[0] = True
    	else:
    		status[0] = False

    	#This will play once when pressed, and once every 15 loops after (~15ms)
    	if (counter >= 15):
    		status[1] = False
    		counter = 0
    	elif (in1  == False):
    		counter = counter+1
            if (status[1] == False): #not triggered, but should have
    			pygame.mixer.find_channel(True).play(pygame.mixer.Sound(fire2))
    			status[1] = True
    	else:
    		status[1] = False
    		counter = 0

    	#This will play WHILE pressed
        if (in2 == False):
            ChannelA.play(fire3)


        if (in3 == False):
            pygame.mixer.music.fadeout(250)
        if (in4 == False):
            pygame.mixer.music.play(-1)
        sleep(.01)
    except KeyboardInterrupt:
    	pygame.mixer.music.stop()
    	print "YAHOOOOO! You're all clear, kid."
        exit()