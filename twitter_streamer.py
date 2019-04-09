from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

import twitter_credentials

'''
TWITTER AUTHENTICATOR
Authenticate code  and the application
'''


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,
                            twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


'''
TWITTER STREAMER
Class for streaming and processing tweets
'''


class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    # This method handles Twitter authentication and the connection to the twitter Streaming API
    def stream_tweets(self, hash_tag_list):
        print("STREAMING STARTET")
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()

        # create a data stream
        stream = Stream(auth, listener)

        # Define words for filtering Twitter streams
        stream.filter(track=hash_tag_list)


'''
TWITTER STREAM LISTENER
Class that inherit from StreamListener
Listening to tweets and an print the data 
'''


class TwitterListener(StreamListener):
    def __init__(self):
        self.tweet_counter = 0

    def on_data(self, raw_data):
        try:
            json_load = json.loads(raw_data)
            text = json_load['text']
            coded = text.encode('utf-8')
            s = str(coded)
            print("########## NEW TWEET: Nr: %i ########## \n" %
                  (self.i), s[2:-1])

            self.tweet_counter += 1
            text = json_load['geo']
            s = str(text)
            print("LOCATION", s)
            print()

            '''MORE CODE HERE'''

        except BaseException as e:
            print("Error on raw_data: %s" % str(e))
        return True

    def get_tweet_counter():
        # return self.tweet_counter
        return 50

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
