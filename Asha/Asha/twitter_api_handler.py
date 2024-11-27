import tweepy

# Placeholder credentials; replace with actual credentials for a real bot
CONSUMER_KEY = "your_consumer_key_here"
CONSUMER_SECRET = "your_consumer_secret_here"
ACCESS_TOKEN = "your_access_token_here"
ACCESS_TOKEN_SECRET = "your_access_token_secret_here"


def initialize_twitter_api():
    """Initializes and returns the Twitter API client."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


class TwitterAPIHandler:
    def __init__(self):
        self.api = initialize_twitter_api()

    def tweet(self, message):
        """Posts a tweet to Twitter."""
        try:
            self.api.update_status(message)
            print(f"Successfully tweeted: {message}")
        except tweepy.TweepError as e:
            print(f"Error while tweeting: {e}")

    def follow_back(self):
        """Follows back any followers."""
        try:
            for follower in tweepy.Cursor(self.api.followers).items():
                follower.follow()
                print(f"Followed back: {follower.screen_name}")
        except tweepy.TweepError as e:
            print(f"Error while following back: {e}")

    def like_recent_tweets(self, hashtag, count=5):
        """Likes recent tweets in a specified hashtag."""
        try:
            for tweet in tweepy.Cursor(self.api.search, q=hashtag, result_type="recent").items(count):
                tweet.favorite()
                print(f"Liked tweet: {tweet.text}")
        except tweepy.TweepError as e:
            print(f"Error while liking tweets: {e}")

    def retweet_recent_tweets(self, hashtag, count=5):
        """Retweets recent tweets in a specified hashtag."""
        try:
            for tweet in tweepy.Cursor(self.api.search, q=hashtag, result_type="recent").items(count):
                tweet.retweet()
                print(f"Retweeted: {tweet.text}")
        except tweepy.TweepError as e:
            print(f"Error while retweeting: {e}")
