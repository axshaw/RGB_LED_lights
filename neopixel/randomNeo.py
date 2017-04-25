# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import random
import pygame
from neopixel import *


# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 15     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def randomise(strip):
	blankAll(strip)		

        for i in range(0, 5):
                strip.setPixelColorRGB(random.randint(0,16),0, 255, 0)
	strip.show()
	time.sleep(0.1)
	
def blankAll(strip):
	for i in range(0, strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,0)
	strip.show()

# Main program logic follows:
	# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
strip.begin()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
pygame.mixer.init()
pygame.mixer.music.load("computerwarble.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
	randomise(strip)
	continue

blankAll(strip)
	#while True:
	#	randomise(strip)

#	colorWipe(strip, Color(0, 0, 0))        
#	print ('Press Ctrl-C to quit.')
#	while True:
		# Color wipe animations.
#		colorWipe(strip, Color(255, 0, 0))  # Red wipe
#		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#		colorWipe(strip, Color(0, 0, 255))  # Green wipe
		# Theater chase animations.
#		theaterChase(strip, Color(127, 127, 127))  # White theater chase
#		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
#		rainbow(strip)
#		rainbowCycle(strip)
#		theaterChaseRainbow(strip)
