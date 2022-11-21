import tweepy
from tweepy import OAuthHandler, Stream
import socket
import json

consumer_secret = 'bYOLrnkvJdCJeF3iYBAamLQY5HXwla5hz5mzWJiyAP9K0i9jul'
consumer_key = 'v3SoyRIi7d5xzjDiPUMgU5qS3'
access_token = '1497787515088035840-glE4iazjAbFDsVp7MiGyvJVHbR9wZp'
access_secret = 'ge0ntMRn9yZ95xmeaDHCeSbKRJ9Nbtqjj3zuPOwr8BFsf'

class TweetListener(Stream):
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print('ERROR', e)
        return True
    
    def on_error(self, status):
        print(status)
        return True

def send_data(csocket):
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_secret)
    
    #twitter_stream = Stream(consumer_key, consumer_secret,
    #                        access_token, access_secret)
    #twitter_stream.filter(track=['guitar'])
    auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_secret)

    api = tweepy.API(auth)

    public_tweets = api.search_tweets('guitar')


if __name__ == '__main__':
    s = socket.socket()

    host = '127.0.0.1'
    port = 9999
    s.bind((host, port))

    print('listening on port', port)

    s.listen(5)
    c, addr = s.accept()

    send_data(c)