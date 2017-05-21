import pyRSSWeather

localWeather = pyRSSWeather.RSSWeather('KSJC')

print(localWeather.currentTemp)
print(localWeather.rain)