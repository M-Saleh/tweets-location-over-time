""" Open Stream with Twitter, publish new tweet using pypubsub on config.TWEETS_CHANNEL"""
import tweepy
import src.config as config


class StreamListener(tweepy.StreamListener):

    def setup(self, pubr):
        """ Set the Stream to Stream Listener"""
        self.pub = pubr

    def on_status(self, status):
        """ New tweet for this account stream"""
        self.pub.sendMessage(config.TWEETS_CHANNEL, tweet=status)

    def on_error(self, status_code):
        print("on_error : " + str(status_code))

    def on_timeout(self):
        print("on_timeout")

    def on_connect(self):
        print("on_connect")

    def on_disconnect(self, notice):
        print("on_disconnect")

    def on_closed(self, resp):
        print("on_closed")


class Stream:
    def __init__(self, keywords, pub):
        print("Start streaming with keywords : " + str(keywords.split(',')))
        self.keywords = keywords

        twitter_auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        twitter_auth.set_access_token(config.access_token, config.access_token_secret)
        self.streamListen = StreamListener()
        self.streamListen.setup(pub)
        self.twitterStream = tweepy.Stream(twitter_auth, self.streamListen)

    def run(self):
        while True:
            try:
                # rect.min_lng, rect.min_lat, rect.max_lng, rect.max_lat
                # loc = [-90,-90,90,90]
                # self.twitterStream.filter(locations=loc)
                self.twitterStream.filter(track=self.keywords.split(','))
            except Exception as e:
                print(str(e))
                continue
