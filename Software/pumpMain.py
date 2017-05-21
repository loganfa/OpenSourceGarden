#!/usr/bin/python
#Garden Pump Control Script
#tm_hour/tm_min/tm_sec
#Logan F 2017

import time
import RPi.GPIO as GPIO

#Script constants
LOOPINTERVAL = 1
TIMETHRESHOLD = 3
WATERINGTIME = 30

#Time to water at
waterSecond = 30
waterMinute = -1
waterHour = -1

#Configure GPIO
GPIO.setmode(GPIO.BCM) #Use BCM numbering of the pins
GPIO.setwarnings(False) #Squelch pin config warnings
GPIO.setup(pumpPin, GPIO.OUT, initial=GPIO.LOW) #Config pin 26 for pump control/init to 1

#Check if proper time
def isTime():
	#Get current time
	currentTime = time.localtime()
	#Break the time struct into hour/minute/second
	hour = currentTime.tm_hour
	minute = currentTime.tm_min
	second = currentTime.tm_sec

	if((hour == waterHour) or (waterHour < 0)):
		if((minute == waterMinute) or (waterMinute < 0)):
			#The second conditional has a threshold to guarantee hitting the mark
			if(abs(second-waterSecond) < TIMETHRESHOLD):
				return True
			else:
				return False
		else:
			return False
	else:
		return False

#Check if you should pump water
def pumpWater():
	if(isTime()):
		print("watering for "+str(WATERINGTIME)+" seconds.")
		GPIO.output(pumpPin, GPIO.HIGH)
		time.sleep(WATERINGTIME)
		GPIO.output(pumpPin, GPIO.LOW)

#Main Loop
while(1):
	pumpWater()

	#Loop sleep interval (to save system resources)
	time.sleep(LOOPINTERVAL)
GPIO.cleanup()
