""" Subscribe using pypubsub on config.TWEETS_CHANNEL for any new tweet, then get its location and write to stats file
id, latitude, longitude, dateTime
"""
import src.tweet_location_extractor as location_extractor


def new_tweet(tweet):
    tweet_json = tweet._json
    location = location_extractor.get_tweet_location(tweet_json)
    print(location)
