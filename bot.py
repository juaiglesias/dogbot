import datetime 
import os
import requests
import tweepy 

filename = 'temp'

def main():
    tweet_message, url_image = generate_tweet()
    twitter_api_connection = twitter_access()
    publish_tweet_api(tweet_message, url_image, twitter_api_connection)

def twitter_access(): 
    print('Authenticating at Twitter API...')
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET']) 
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    api_twitter = tweepy.API(auth)
    print('Successful authentication...')
    return api_twitter

def generate_tweet():
    print('Obtaining information for DOG API...')
    response = requests.get(os.environ['URL_GET_DOG'], headers={"x-api-key": os.environ['DOG_API_KEY']}).json()
    tweet_message = 'Hello world'
    return tweet_message, response[0]['url']

# Saves the image as filename variable name's
def get_image_and_save(url):
    request_image = requests.get(url, stream=True)
    if request_image.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request_image:
                image.write(chunk)
        print('Obtained image..')
    else:
        print('There was an error obtaining the image')
        return -1

def delete_image():
    os.remove(filename)

def publish_tweet_api(tweet_message, url_image, api):
    get_image_and_save(url_image)
    print('Sending tweet...')
    api.update_with_media(filename, status=tweet_message)
    print('The tweet was sent successfully')
    delete_image()

if __name__ == "__main__":
    main()