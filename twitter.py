# Twitter interaction scripts

import os
import tweepy

# Twitter access
def twitter_access(): 
    print('Authenticating at Twitter API...')
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET']) 
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    api_twitter = tweepy.API(auth)
    print('Successful authentication...')
    return api_twitter