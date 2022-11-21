import tweepy

consumer_secret = 'bYOLrnkvJdCJeF3iYBAamLQY5HXwla5hz5mzWJiyAP9K0i9jul'
consumer_key = 'v3SoyRIi7d5xzjDiPUMgU5qS3'
access_token = '1497787515088035840-glE4iazjAbFDsVp7MiGyvJVHbR9wZp'
access_secret = 'ge0ntMRn9yZ95xmeaDHCeSbKRJ9Nbtqjj3zuPOwr8BFsf'

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_secret
)

api = tweepy.API(auth)

public_tweets = api.search_tweets('guitar')
for tweet in public_tweets:
    print(tweet.text)