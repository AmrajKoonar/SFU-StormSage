import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret
from webscrape import get_weather_info, get_weather_update
import time

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


while(True):
    weatherInfo = get_weather_info()  #returns the a sentence describing the weather 
    weather = get_weather_update()    #returns the weather (dry, snow, rain etc)

    client.create_tweet(text = "Hello world")







