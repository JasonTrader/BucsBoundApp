
import tweepy
from tweepy import OAuthHandler

import config

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print status_code

auth = OAuthHandler(config.cons_key, config.cons_sec)
auth.set_access_token(config.access_token, config.access_sec)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#chinesegp'], async=True)

while True:
    inp = raw_input()
    if inp == 'q':
        myStream.disconnect()
        break
