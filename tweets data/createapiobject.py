#import libraries
import os
import sys
sys.path.append("..")

#import twitter tokens from FDMA_quantra module
from data_modules.FDMA_quantra import get_twitter_tokens
#method in module
twitter_tokens=get_twitter_tokens()

#set manually
consumer_key=twitter_tokens['consumer_key']
consumer_secret=twitter_tokens['consumer_secrete']

#import tweepy
import tweepy
#authenticate
auth=tweepy.AppAuthHandler(consumer_key,consumer_secret)

#cretate api object
api=tweepy.API(
      auth,
      wait_on_rate_limit=True,
      wait_on_rate_limit_notify=True
)