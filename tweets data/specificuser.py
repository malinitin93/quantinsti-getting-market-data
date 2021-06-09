# Import libraries
import os
import sys
sys.path.append("..")
from tabulate import tabulate
# Import the get_twitter_tokens from the FMDA_quantra module
# The code of this module can be found in the downloads (last section) of this course
# You need to edit FMDA_quantra.py file and add your Twitter tokens manually before you continue
from data_modules.FMDA_quantra import get_twitter_tokens

# Method in sentiment_analysis_quantra module to get the dictionary of consumer key and consumer secret
twitter_tokens = get_twitter_tokens()

# Set the consumer key and secret from the twitter_tokens dictionary
consumer_key = twitter_tokens['consumer_key']
consumer_secret = twitter_tokens['consumer_secret']

import tweepy
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#function takes input as tweet
def print_tweet_info(tweet):
    tweet_info=[
        ['Tweet ID:',tweet.id_str],
        ['Created At (UTC):',tweet.created_at],
        ['User Screen Name:',tweet.user.screen_name],
        ['Tweet Text:',tweet.full_text],
        ['Retweet Count:',tweet.retweet_count],
        ['Favourite Count',tweet.favorite_count],
        ['Language:',tweet.lang]
    ]
    print("..............")
    print(tabulate(tweet_info))
#fuction ends here

#search method
#    tweet by specific user
tweets_by_user=api.user_timeline(screen_name='@vivbajaj',tweet_mode='extended')

#print function  call
print_tweet_info(tweets_by_user[0])