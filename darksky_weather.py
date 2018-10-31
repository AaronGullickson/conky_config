import requests
import json
import os
import time
from datetime import datetime


conditions_weather_font = {
		"tornado": u"1", #Tornado
		#"1": u"2", #Tropical Storm
		"hurricane": u"3", #Hurricane
		#"3": u"n", #Severe Thunderstorms
		"thunderstorm": u"m", #Thunderstorms
		#"5": u"x", #Mixed Rain and Snow
		#"6": u"x", #Mixed Rain and Sleet
		#"7": u"y", #Mixed Precipitation
		#"8": u"s", #Freezing Drizzle
#		"9": u"h", #Drizzle
#		"10": u"t", #Freezing Rain
#		"11": u"h", #Light Rain
		"rain": u"i", #Rain
#		"13": u"p", #Snow Flurries
#		"14": u"p", #Light Snow Showers
#		"15": u"8", #Drifting Snow
		"snow": u"q", #Snow
#		"17": u"u", #Hail
		"sleet": u"w", #Sleet
#		"19": u"7", #Dust
		"fog": u"0", #Fog
#		"21": u"9", #Haze
#		"22": u"4", #Smoke
#		"23": u"6", #Blustery
#		"24": u"6", #Windy
#		"25": u"-", #N/A
		"cloudy": u"f", #Cloudy
#		"27": u"D", #Mostly Cloudy - night
#		"28": u"d", #Mostly Cloudy - day
		"partly-cloudy-night": u"C", #Partly Cloudy - night
		"partly-cloudy-day": u"c", #Partly Cloudy - day
		"clear-night": u"A", #Clear - night
		"clear-day": u"a", #Clear - day
#		"33": u"B", #Fair - night
#		"34": u"b", #Fair - day
#		"35": u"v", #Mixed Rain and Hail
#		"36": u"5", #Hot
#		"37": u"k", #Isolated Thunderstorms - day
#		"38": u"k", #Scattered Thunderstorms - day
#		"39": u"g", #Scattered Showers - day
#		"40": u"j", #Heavy Rain
#		"41": u"o", #Scattered Snow Showers - day
#		"42": u"r", #Heavy Snow
#		"43": u"r", #Heavy Snow
#		"44": u"-", #N/A
#		"45": u"G", #Scattered Showers - night
#		"46": u"O", #Scattered Snow Showers - night
#		"47": u"K", #Isolated Thunderstorms - night
#		"na": u"-", #N/A
#		"-": u"-" #N/A
	}

url = 'https://api.darksky.net/forecast/53471ed8c7937bb735401d5f71dfb0d2/44.052151,-123.091187'

current= open(os.path.expanduser('~') + "/.conky/weather/curr_cond","w+")
forecast= open(os.path.expanduser('~') + "/.conky/weather/tod_ton","w+")


response = requests.get(url)
weather = json.loads(response.text)

#TODO: figure out font name for first line
current.write("Current\n")
current.write(conditions_weather_font[weather["currently"]["icon"]])
current.write("\n")
current.write('{:.0f}'.format(weather["currently"]["temperature"]))
current.write("\n")
current.write(weather["currently"]["summary"])
current.write("\n")
current.write(weather["minutely"]["summary"])
current.write("\n")
current.close()


daily = weather["daily"]["data"]
for day in daily:
    dayname = datetime.fromtimestamp(day["time"]).strftime("%A")
    forecast.write(dayname.upper())
    forecast.write("\n")
    forecast.write(conditions_weather_font[day["icon"]])
    forecast.write("\n")
    forecast.write('{:.0f}'.format(day["temperatureHigh"]))
    forecast.write("\n")
    forecast.write('{:.0f}'.format(day["temperatureLow"]))
    forecast.write("\n")
    forecast.write(day["summary"])
    forecast.write("\n")

forecast.close()
