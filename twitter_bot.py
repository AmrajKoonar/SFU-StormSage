#Amraj & Amar Koonar Twitter Bot

import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret
from webscrape import get_weather_info, get_weather_update, get_update
import time
import re
from datetime import datetime
from webscrape import get_weather_api_info, download_images


client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
oneHour = 3600
threeHours = 10800 
previousWeather = ""
prev = ""


def post_tweet_with_multiple_images_thread(image_paths, first_caption, thread_caption):
    """
    Uploads multiple images to Twitter and posts them as a thread if more than 4 images are provided.

    Parameters:
        image_paths (list): List of paths to the image files.
        first_caption (str): Text to include in the first tweet.
        thread_caption (str): Text to include in the subsequent tweets in the thread.
    """
    try:
        # Split images into chunks of 4
        chunks = [image_paths[i:i + 4] for i in range(0, len(image_paths), 4)]
        first_tweet_id = None

        for i, chunk in enumerate(chunks):
            # Upload images in the current chunk
            media_ids = [api.media_upload(image_path).media_id for image_path in chunk]
            
            # Set caption for the current tweet
            if i == 0:
                text = first_caption  # First tweet uses the provided first caption
            else:
                text = thread_caption  # Subsequent tweets use the thread caption

            # Post the tweet
            if i == 0:
                # First tweet
                response = client.create_tweet(text=text, media_ids=media_ids)
                first_tweet_id = response.data['id']
            else:
                # Reply to the previous tweet
                response = client.create_tweet(
                    text=text, media_ids=media_ids, in_reply_to_tweet_id=first_tweet_id
                )
                first_tweet_id = response.data['id']  # Update the thread ID for the next reply

        print("Thread posted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")




image_paths = ['img_url_AQ_North.jpg', 'img_url_Gaglardi_intersection.jpg', 'img_url_Tower_Road_North.jpg', 'img_url_Tower_Road_South.jpg', 'img_url_University_Drive_North.jpg', 'img_url_AQ_SouthWest.jpg', 'img_url_AQ_SouthEast.jpg', 'img_url_Blusson_Hall_Roof.jpg']


weather_prefixes = {
    "very hot": "🌡️ It's a scorching hot day at SFU — stay hydrated! 🌡️",
    "sunny": "☀️ It's a bright and sunny day at SFU ☀️",
    "heavy snow": "🚨❄️ Extreme weather alert! It’s heavy snow at SFU! ❄️🚨",
    "rain": "🌧️ Don't forget your umbrella — it’s rainy at SFU 🌧️:",
    "snow": "❄️ Winter wonderland alert! It’s snowing at SFU ❄️:",
    "wind": "💨 Hold on to your hats — it’s windy at SFU! 💨:",
}

def get_weather_prefix(weather_update):
    # Check if temperature is > 25 degrees
    temp = extract_temperature(weather_update)
    if temp is not None and temp > 25:
        return weather_prefixes["very hot"]

    # Normal priority-based matching
    priorities = ["heavy snow", "rain", "snow", "wind", "sunny"]  # Set priorities
    weather_update_lower = weather_update.lower()
    
    for keyword in priorities:
        if keyword in weather_update_lower:  # Match based on priority
            return weather_prefixes[keyword]
    return "☁️ Here's the latest weather update from SFU ☁️: "  # Default message

def extract_temperature(weather_update):
    """
    Extracts the temperature from the weather update string.

    Assumes the temperature is in the format: "<number>°C".
    For example: "Sunny and warm, 27°C expected today."
    """
    import re
    match = re.search(r"(\d+)\s*°C", weather_update)
    if match:
        return int(match.group(1))
    return None

while(True):
    current_time = datetime.now()
    time_str = current_time.strftime("%I:%M %p").lstrip('0')
    weatherInfo = get_weather_info()  #returns the a sentence describing the weather 
    download_images()

    hour = current_time.hour

    amOrPm = current_time.strftime("%p")

    current = get_update()

    current_time = "Current time: " + time_str

    if(current != prev): #check for NEW update
        
        prefix = get_weather_prefix(current)

        first_caption = f"{prefix}\n\n{weatherInfo}\n\n{current_time}"
        thread_caption = "Additional live SFU webcam updates: 📸"

        post_tweet_with_multiple_images_thread(image_paths, first_caption = first_caption, thread_caption=thread_caption)
        # client.create_tweet(text = weatherInfo + "\n\n" + current)
        print(weatherInfo + "\n\n" + current_time) 
    else:
        # No new weather update, tweet just the images with a basic caption
        basic_caption = "No new weather update.\n\nLive SFU webcam updates: 📸"

        # Tweet with images and basic caption
        post_tweet_with_multiple_images_thread(
            image_paths, first_caption=basic_caption, thread_caption=basic_caption
        )
        print(f"No weather update. Posted basic image tweet:\n{basic_caption}")
        

    print()
    print("Twitter Bot Status: ACTIVE | Time: " + time_str + " | Mode: ")
    prev = get_update()
    
    time.sleep(1800)#sleep for 30mins