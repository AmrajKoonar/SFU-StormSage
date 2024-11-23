#Amraj & Amar Koonar Twitter Bot

import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret
from webscrape import get_weather_info, get_weather_update, get_update
import time
from datetime import datetime
from webscrape import get_weather_api_info

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

oneHour = 3600
threeHours = 10800 
previousWeather = ""
prev = ""
while(True):
    current_time = datetime.now()
    time_str = current_time.strftime("%I:%M %p") 
    weatherInfo = get_weather_info()  #returns the a sentence describing the weather 
    

    hour = current_time.hour
    amOrPm = current_time.strftime("%p")
    current = get_update()
    if(current != prev):#check for update
        client.create_tweet(text = weatherInfo + "\n\n" + current)
        print(weatherInfo + "\n\n" + current) 
        

    print()
    print("Twitter Bot Status: ACTIVE | Time: " + time_str + " | Mode: " + nightOrDay)
    prev = get_update()
    
    time.sleep(900)#sleep for 15mins