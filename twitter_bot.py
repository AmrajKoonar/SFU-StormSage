import tweepy
from keys_test import api_key, api_secret, bearer_token, access_token, access_token_secret

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text = "Hello world")

# client.like("1613078224539615233")

# client.retweet("1613078224539615233")

# client.create_tweet(in_reply_to_tweet_id="1613078224539615233", text = "Keep learning Simplilearners")

# for tweet in api.home_timeline():
#     print(tweet.text)

# person = client.get_user(username = "narendramodi").data.id

# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)







