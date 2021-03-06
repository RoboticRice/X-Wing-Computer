#!/usr/bin/python

# Created by RoboticRice
# https://github.com/RoboticRice
# Inspired by:
#	https://makezine.com/projects/make-33/simple-soundboard/
#	https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

print "Luke, you've switched off your tageting computer. What's wrong?"

import pygame.mixer
import time
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
GPIO.setup(24, GPIO.OUT) #for LED
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init(48000, -16, 1, 1024)
#Test this later: New in pygame 2(when compiled with SDL2) - size can be 32 (32bit floats).

#Set-Up Sound Files

##No background music will be used
##pygame.mixer.music.load("OTHER/Com chatter.wav")
##pygame.mixer.music.load("OTHER/OST Cantina Band.wav")

#fire = pygame.mixer.Sound("XWING/XWing fire.wav")
fire = pygame.mixer.Sound("XWING/XWing fire 2 mod.wav")
#fire = pygame.mixer.Sound("XWING/XWing fire 3.wav")
fail = pygame.mixer.Sound("XWING/EngineFail.wav")
r2d1 = pygame.mixer.Sound("R2/CurtReply.wav")
r2d2 = pygame.mixer.Sound("R2/HappyConfirmation.wav")
r2d3 = pygame.mixer.Sound("R2/TestyBlowup.wav")

#Set-Up Audio Channels (each channel plays audio seperate from the other)
pygame.mixer.set_num_channels(5)
pygame.mixer.set_reserved(0)
R2D2 = pygame.mixer.Channel(0) #Dedicated channel for R2D2 SFX, any new SFX on this channel interupts previous

#Init the button press stuff
status = [False]*5 #currently using states for 5 inputs
counter = 0
timer = 0
light = True
blinked = False
class tempException(Exception):
    pass

print "Nothing. I'm all right."

#pygame.mixer.music.play(-1) #uncomment to start default with music playing
while True:
    try:
    	inE = GPIO.input(4)  #E-STOP SFX
    	in0 = GPIO.input(17) #Engine
    	in1 = GPIO.input(18) #Fire
    	in2 = GPIO.input(22) #R2
    	in3 = GPIO.input(23) #R2
    	in4 = GPIO.input(25) #R2
    	in5 = GPIO.input(27) #auto-R2

    	#No longer using ambient music
    	#if (pygame.mixer.music.get_busy()):
    	#	GPIO.output(24, GPIO.HIGH)
    	#else:
    	#	GPIO.output(24, GPIO.LOW)

    	#set light to blink
    	if ((int(time.time()*10)%5) == 0):
    		if (blinked == False):
    			blinked = True
    			if (light):
    				GPIO.output(24, GPIO.HIGH)
    				light = False
    			else:
    				GPIO.output(24, GPIO.LOW)
    				light = True
    	else:
    		blinked = False

    	#This will play once, when pressed
        if (in0 == False):
            if (status[0] == False): #not triggered, but should have
    			pygame.mixer.find_channel(True).play(fail)
    			status[0] = True
    	else:
    		status[0] = False

    	#This will play once when pressed, and once every couple dozen loops after (~15ms)
    	if (counter >= 30):
    		status[1] = False
    		counter = 0
    	elif (in1 == False):
    		counter = counter + 1
        	if (status[1] == False): #not triggered, but should have
    			pygame.mixer.find_channel(True).play(fire)
    			status[1] = True
    	else: #elif (in1  == False) && (count != 0): counter++ #add this so it can't be replayed until the time limit has passed, even if you release and re-press
    		status[1] = False
    		counter = 0

    	#This will play WHILE pressed (and interupt previous playings of r2d2 sfx)
        if (in2 == False):
            if (status[2] == False): #not triggered, but should have
    			R2D2.play(r2d1) #R2D2 is a dedicated channel
    			status[2] = True
    	else:
    		status[2] = False

    	#This will play WHILE pressed (and interupt previous playings of r2d2 sfx)
        if (in3 == False):
            if (status[3] == False): #not triggered, but should have
    			R2D2.play(r2d2) #R2D2 is a dedicated channel
    			status[3] = True
    	else:
    		status[3] = False

    	#This will play WHILE pressed (and interupt previous playings of r2d2 sfx)
        if (in4 == False):
            if (status[4] == False): #not triggered, but should have
    			R2D2.play(r2d3) #R2D2 is a dedicated channel
    			status[4] = True
    	else:
    		status[4] = False

    	if (in5 == False):
    		#the blue button is pressed, activate auto mode for R2D2
    		#remove decimal point
    		#remainder after div = 0 when exactly divisable by %num
    		if ((int(time.time())%48) == 0):
    			R2D2.play(r2d2) #R2D2 is a dedicated channel
    		elif ((int(time.time())%24) == 0):
    			R2D2.play(r2d1) #R2D2 is a dedicated channel

		#No longer using ambient music
        #if (in3 == False): #fades out music
        #    pygame.mixer.music.fadeout(250)
        #if (in4 == False): #play music on infinite loop
        #    pygame.mixer.music.play(-1)

        if (inE == True): #Stops all SFX but music continues
        	raise tempException("These aren't the droids you're looking for.")
        #if (in6 == False): #Stops all SFX and fades Music out
        #	pygame.mixer.music.fadeout(250)
        #	raise tempException("These aren't the droids you're looking for.")

        sleep(.01)
    except tempException as e:
    	print str(e)
    	pygame.mixer.stop()
    	#pygame.mixer.music.stop() #this would be used to stop music as well, but no music is being used
    	while (inE == True):
    		try:
    			sleep(.03)
    			inE = GPIO.input(4)  #forgot to check inE status
    			GPIO.output(24, GPIO.HIGH) #set light to be solid when paused
    			#Do nothing, this prevents spamming the console with print statements
    		except KeyboardInterrupt:
    			#pygame.mixer.stop() #technically not needed, as exit stops everything
    			GPIO.cleanup()
    			print "Mind tricks don't work on me, only money."
        		exit()
    	print "You can go about your business. Move along!"
    except KeyboardInterrupt:
    	#pygame.mixer.stop() #technically not needed, as exit stops everything
    	GPIO.cleanup()
    	print "YAHOOOOO! You're all clear, kid."
        exit()