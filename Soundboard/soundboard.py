import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_upp_down=GPIO.PUD_UP)
#GPIO.setup(23, GPIO.IN)
#GPIO.setup(24, GPIO.IN)
#GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound("Wilhelm Scream.wav")
sndB = pygame.mixer.Sound("R2/WEEEOOOOWW.wav")
sndC = pygame.mixer.Sound("OTHER/Cantina band.wav")

soundChannelA = pygame.mixer.Channel(1)
#soundChannelB = pygame.mixer.Channel(2)
#soundChannelC = pygame.mixer.Channel(3)

print "Sampler Ready."

while True:
   try:
      if (GPIO.input(23) != True):
         soundChannelA.play(sndA)
      #if (GPIO.input(24) == True):
      #   soundChannelB.play(sndB)
      #if (GPIO.input(25) == True):
      #   soundChannelC.play(sndC)
      sleep(.01)
   except KeyboardInterrupt:
      exit()