""" Open Stream with Twitter, publish new tweet using pypubsub on config.TWEETS_CHANNEL"""

import src.config as config
import src.archiver as archiver
import src.stats_manager as stats_manager
from pubsub import pub
import time

# TODO Use another pub/sub model where components to be totally separated in different processes/projects. e.g. Redis.
pub.subscribe(archiver.new_tweet, config.TWEETS_CHANNEL)
pub.subscribe(stats_manager.new_tweet, config.TWEETS_CHANNEL)

if __name__ == "__main__":
    count = 0
    while count < 1000:
        msg = "Message Number" + str(count)
        pub.sendMessage(config.TWEETS_CHANNEL, tweet=msg)
        print("Sent # " + str(count))
        count += 1
        time.sleep(1)

