import tweepy
import twitter_credentials


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,
                                   twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,
                              twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


# TWITTER STREAMER Class for streaming and processing tweets
class TwitterAPI():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
        self.tweet_count = 0

        # This method handles Twitter authentication and the connection to the twitter API
    def call_twitter_API(self):
        auth = self.twitter_authenticator.authenticate_twitter_app()
        api = tweepy.API(auth, wait_on_rate_limit=True)

        search_words = "#bitcoin"
        date_since = "2019-04-29"

        tweets = tweepy.Cursor(api.search, q=search_words,
                               since=date_since).items(10000)

        '''
        d = vars(tweets)
        print("Number of Tweets: ", len(d))
        '''

        for tweet in tweets:
            self.tweet_count += 1
            # print(self.tweet_count)
            # print(tweet.text)
        print("Number of Tweets: ", self.tweet_count)

    def get_number_of_tweets(self):
        return self.tweet_count

    def normalization(self, number):
        '''
        TO DO: Normalize Data to Score 0-100 as Google Trends
        '''
        normalized_number = number
        return normalized_number

    '''
    Method who handles errors: 402 error from twitter API = hit the rate limit. You have to wait
    a certain time before proceed otherwise Twitter looks the app out
    '''

    def on_error(self, status_code):
        if status_code == 420:
            return False
        print(status_code)


def start():
    print("TWITTER MODULE STARTED")
    twitter_API = TwitterAPI()
    twitter_API.call_twitter_API()
    twitter_API.normalization()


if __name__ == "__main__":
    start()
