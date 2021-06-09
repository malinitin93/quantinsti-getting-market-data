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

#new code
#search method
tweets_search_result=api.search(q='$INFY -filter:retweets', count=5, tweet_mode='extended', language='en')

#print tweet info
#function takes as input tweet
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
#def function  end here
#function call
print_tweet_info(tweets_search_result[2])

#other
#max 100 tweets will be fetched
#data type
print(type(tweets_search_result))
print("..............")
print(tweets_search_result)
print("..............")
#length of search
print(len(tweets_search_result))

#get the tweet text
#store the first tweet info in tweet varible
tweet=tweets_search_result[2]
#access the text using property text of the variable tweet
tweet_text=tweet.full_text
#print the text of tweet
print("..............")
print(tweet_text)

