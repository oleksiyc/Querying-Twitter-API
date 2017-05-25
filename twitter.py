import absolute_import , print_function import tweepy
from tweepy import OAuthHandler

consumer_key = ""
consumer_secret = ""

access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.secure = True
auth.set_access_token(access_token , access_secret)

api = tweepy.API(auth) print(api.me())

for timeline in tweepy.Cursor(api.home_timeline).items(10): print(timeline._json)

for friends in tweepy.Cursor(api.friends).items(10): print(friends._json)

for followers in tweepy.Cursor(api.followers).items(10): print(followers._json)