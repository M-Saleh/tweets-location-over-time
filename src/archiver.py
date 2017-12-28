""" Subscribe using pypubsub on config.TWEETS_CHANNEL for any new tweet, then save it in a file or DB!"""
import src.config as config
import json

file = open(config.archiver_file_name, 'a')


def new_tweet(tweet):
    tweet_json = json.dumps(tweet._json)
    print(tweet_json, file=file)
