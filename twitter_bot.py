#Amraj & Amar Koonar Twitter Bot

import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret
from webscrape import get_weather_info, get_weather_update
import time
from datetime import datetime
from webscrape import get_weather_api_info

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

oneHour = 3600
threeHours = 10800 
previousWeather = ""
nightOrDay = ""

while(True):
    current_time = datetime.now()
    time_str = current_time.strftime("%I:%M %p") 
    weatherInfo = get_weather_info()  #returns the a sentence describing the weather 
    weather = get_weather_update(weatherInfo)    #returns the weather (dry, snow, rain etc)
    
    #hour = int(time_str[:2])
    #amOrPm = time_str[-2:]

    hour = current_time.hour
    amOrPm = current_time.strftime("%p")
    
    if (hour == 12 or (1 <= hour <= 6 and amOrPm == "AM")): # Night time condition (12 AM - 6 AM)
        client.create_tweet(text = weatherInfo + "\n\n" + "Current time: " + time_str)
        print(weatherInfo + "\n\n" + "Current time: " + time_str)
        nightOrDay = "Night Time"
        next_sleep = threeHours  
    else:                                                   # Day time condition
        client.create_tweet(text = weatherInfo + "\n\n" + "Current time: " + time_str)
        print(weatherInfo + "\n\n" + "Current time: " + time_str)
        nightOrDay = "Day Time"
        next_sleep = oneHour 

    print()
    print("Twitter Bot Status: ACTIVE | Time: " + time_str + " | Mode: " + nightOrDay)
    previousWeather = weather
    time.sleep(next_sleep)  
