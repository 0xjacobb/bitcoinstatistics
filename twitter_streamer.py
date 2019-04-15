from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import twitter_credentials

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import twitter_credentials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        print("TWITTER AUTHENTICATER CREATED\n")
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# TWITTER STREAMER Class for streaming and processing tweets
class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        self.tweet_count = 0
        print("TWITTER STREAMER CREATED\n")

    # This method handles Twitter authentication and the connection to the twitter Streaming API
    def stream_tweets(self, hash_tag_list):
        print("STREAMING STARTS")
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()

        # create a data stream
        stream = Stream(auth, listener)

        # Define words for filtering Twitter streams
        stream.filter(track=hash_tag_list)

        self.tweet_count = listener.get_tweet_counter()

    def get_number_of_tweets(self):
        return self.tweet_count


# TWITTER STREAM LISTENER Class that inherit from StreamListener Listening to tweets and an print the data
class TwitterListener(StreamListener):
    def __init__(self):
        self.tweet_counter = 0
        print("TWITTER LISTENER CREATED")

    def on_data(self, raw_data):
        try:
            json_load = json.loads(raw_data)
            text = json_load['text']
            coded = text.encode('utf-8')
            s = str(coded)
            print("########## NEW TWEET: Nr: %i ########## \n" %
                  (self.tweet_counter), s[2:-1])

            self.tweet_counter += 1
            text = json_load['geo']
            s = str(text)
            print("LOCATION", s)
            print()

        except BaseException as e:
            print("Error on raw_data: %s" % str(e))
        return True

    def get_tweet_counter(self):
        return self.tweet_counter

    '''
    Method who handles errors: 402 error from twitter API = hit the rate limit. You have to wait
    a certain time before proceed otherwise Twitter looks the app out
    '''

    def on_error(self, status_code):
        if status_code == 420:
            return False
        print(status_code)


if __name__ == "__main__":
    hash_tag_list = [
        "bitcoin",
    ]
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(hash_tag_list)


class listener(StreamListener):

    def __init__(self):
        self.tweet_counter = 0
        print("TWITTER LISTENER CREATED")

    def on_data(self, raw_data):
        try:
            json_load = json.loads(raw_data)
            text = json_load['text']
            coded = text.encode('utf-8')
            s = str(coded)
            print("########## NEW TWEET: Nr: %i ########## \n" %
                  (self.tweet_counter), s[2:-1])

            self.tweet_counter += 1

        except BaseException as e:
            print("Error on raw_data: %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
        print(status_code)

    def get_number_of_tweets(self):
        return self.tweet_counter


auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                    twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                      twitter_credentials.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["bitcoin"])
