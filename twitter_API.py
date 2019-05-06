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
    def __init__(self, search_words, date):
        self.twitter_authenticator = TwitterAuthenticator()
        self.tweet_count = 0
        self.twitter_words = search_words
        self.date_since = date

        # This method handles Twitter authentication and the connection to the twitter API
    def call_twitter_API(self):
        auth = self.twitter_authenticator.authenticate_twitter_app()
        api = tweepy.API(auth, wait_on_rate_limit=True)

        tweets = tweepy.Cursor(api.search, q=self.twitter_words,
                               since=self.date_since).items(10000)

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


def start(search_words, start_date):
    print("...twitter module starte")
    twitter_API = TwitterAPI(search_words, start_date)
    twitter_API.call_twitter_API()
    twitter_API.normalization()


if __name__ == "__main__":
    search_words = "#bitcoin"
    start_date = "2019-04-29"
    start(search_words, start_date)
