import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret
from webscrape import get_weather_info, get_weather_update
import time
from datetime import datetime

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

thirtyMins = 1800
previousWeather = ""
count = 1

while(True):
    current_time = datetime.now()
    time_str = current_time.strftime("%I:%M %p") 
    weatherInfo = get_weather_info()  #returns the a sentence describing the weather 
    weather = get_weather_update(weatherInfo)    #returns the weather (dry, snow, rain etc)

    print("Twitter Bot Status: ACTIVE | Time: " + time_str)

    if(weather != previousWeather):
        client.create_tweet(text = weatherInfo + "\n\n" + "Current time: " + time_str)
        
    
    previousWeather = weather
    count+=1
    time.sleep(thirtyMins)  #Tweet every 30mins












