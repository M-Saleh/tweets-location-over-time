""" Subscribe using pypubsub on config.TWEETS_CHANNEL for any new tweet, then get its location and write to stats file
id, longitude, latitude, dateTime
"""
import src.tweet_location_extractor as location_extractor
import src.config as config
import datetime

stats_file = open(config.stats_file_name, 'a')


def new_tweet(tweet):
    tweet_json = tweet._json
    location = location_extractor.get_tweet_location(tweet_json)
    if location:
        time_stamp = int(tweet_json["timestamp_ms"])/1000
        tweet_time = datetime.datetime.fromtimestamp(time_stamp).isoformat()
        stats_line = str(tweet_json["id"]) + "," + str(location[0])+"," + str(location[1])+"," + tweet_time
        print(stats_line, file=stats_file)
        stats_file.flush()
    else:
        print("NO location for : " + str(tweet_json))
