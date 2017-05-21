#Python Weather Library
#Logan F 2017

import feedparser
import time

class RSSWeather:
	stationName = ''
	currentTemp = 0
	rain = False
	timeStamp = 0
	feed = None

	def __init__(self,stationName):
		self.stationName = stationName
		self.feed = feedparser.parse('http://w1.weather.gov/xml/current_obs/'+self.stationName+'.rss')
		self.timeStamp = time.clock()
		self.getUpdate()

	def getTemp(self,condString):
		tempLocation = condString.find(' F ')
		if(tempLocation<0):
			return -999
		tempString = ''
		for j in range(3):
			currentChar = condString[tempLocation-(j+1)]
			if(currentChar==' '):
				break
			if(currentChar in '0123456789'):
				tempString = currentChar + tempString
		return float(tempString)

	def getRain(self,condString):
		if(condString.find('rain')>-1):
			return True
		else:
			return False

	def getUpdate(self):
		condString = self.feed.entries[0].title
		self.currentTemp = self.getTemp(condString)
		self.rain = self.getRain(condString)
		self.timeStamp = time.clock()