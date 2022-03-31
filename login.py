import tweepy 
from tweet_analyzer import config

def authrize():
    """3 legged OAuth to be completed"""
    CONSUMER_KEY = config.CONSUMER_KEY
    CONSUMER_SECRET = config.CONSUMER_SECRET

    BEARER_TOKEN = config.BEARER_TOKEN

    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET,callback="oob")

    print(auth.get_authorization_url())

    verifier = input("Input PIN: ")
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET = auth.get_access_token(verifier)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    print(ACCESS_TOKEN,"******",ACCESS_TOKEN_SECRET)
    config.ACCESS_TOKEN = ACCESS_TOKEN
    config.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
    return True
