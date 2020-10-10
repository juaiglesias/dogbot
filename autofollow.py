import tweepy
import os

import twitter
import testenv

def main():
    #testenv.set_variables()
    api = twitter.twitter_access()
    print('Automatic Following starting...')
    for item in tweepy.Cursor(api.search, "#dogs").items(int(os.environ['FOLLOWING_USERS_PER_HOUR'])):
        try:
            api.create_friendship(item.user.id)
            print('Following: '+item.user.name)
        except tweepy.TweepError:
            print('Hubo un problema ...')
            break

if __name__ == "__main__":
    main()