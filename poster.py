# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

os.chdir('models')

# get timeline
timeline = api.home_timeline()

# get fortnite search
search = api.search("Fortnite", lang="en", count=1)

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    try:
        timeline[0].favorite()
        timeline[0].retweet()
        search[0].favorite()
        search[0].retweet()
    except:
        pass
    time.sleep(900)
