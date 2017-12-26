import src.config as config
import src.archiver as archiver
import src.stats_manager as stats_manager
import src.twitter_stream as twitter_stream
from pubsub import pub


# TODO Use another pub/sub model where components to be totally separated in different processes/projects. e.g. Redis.
pub.subscribe(archiver.new_tweet, config.TWEETS_CHANNEL)
pub.subscribe(stats_manager.new_tweet, config.TWEETS_CHANNEL)


if __name__ == "__main__":
    keywords = "football,egypt"
    stream = twitter_stream.Stream(keywords, pub)
    stream.run()
