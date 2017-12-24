""" Subscribe using pypubsub on config.TWEETS_CHANNEL for any new tweet, then get its location and write to stats file
id, latitude, longitude, dateTime
"""


def new_tweet(tweet):
    print("New tweet to stats manager")

