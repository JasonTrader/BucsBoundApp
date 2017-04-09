import tweepy
from tweepy import OAuthHandler
import unicodedata

import config

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        f = open('in', 'a')
        s = unicodedata.normalize('NFKD', status.user.name).encode('ascii','ignore') + ',' + unicodedata.normalize('NFKD', status.user.screen_name).encode('ascii','ignore') + ',' + unicodedata.normalize('NFKD', status.text).encode('ascii','ignore') + ',' + str(status.user.followers_count)
        print status.text
        f.write(s)
        f.close()
        
    def on_error(self, status_code):
        print status_code





auth = OAuthHandler(config.cons_key, config.cons_sec)
auth.set_access_token(config.access_token, config.access_sec)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#BucsBound'], async=True)


inp = raw_input()
myStream.disconnect()

