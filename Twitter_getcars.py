# Import the necessary methods from tweepy library
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


# Variables that contain the user credentials to access Twitter API
# (Note: replace with your own values from https://apps.twitter.com/)
consumer_key = "Consumer Key (API Key)"
consumer_secret = "Consumer Secret (API Secret)"
author_token = "Access Token"
author_secret = "Access Token Secret"


class listener(StreamListener):
    def on_data(self, data):
        try:
            
            # We only want the tweet (text) and time
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            # I used three colons here to be safe. Two will suffice.
            saveAs = str(time.time()) + ':::' + tweet
            
            # writing data to file            
            saveFile = open('tweet_cars2.csv', 'a')
            saveFile.write(saveAs)
            saveFile.write('\n')
            saveFile.close()
            return (True)
        except BaseException as e:
            print
            'failed ondata,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print
        status


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(author_token, author_secret)
twitterStream = Stream(auth, listener())
# This retrieves tweets that contain any of these carmakers
twitterStream.filter(track=['car'
                            'chevy', 'ford', 'toyota',
                            'acura', 'kia', 'audi',
                            'chrysler', 'dodge', 'ferrari'
                            'fiat', 'buick', 'cadillac', 'chevrolet',
                            'bmw', 'honda', 'jeep', 'lexus', 'mazda',
                            'mini', 'nissan', 'tesla''volvo', 'saab',
                            'porsche', 'lamborghini', 'mclaren'])
