import datetime as dt
import time
import smtplib
import requests
import tweepy

with open('secrets.txt', 'r') as file:
    exec(file.read())


def tweet(h, m):
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_secret)
    auth = tweepy.OAuthHandler(access_secret, api_secret, api_key, access_token)
    api = tweepy.API(auth)

    client.create_tweet(text=f"Hello world it's {h}:{m}!")


while True:
    now = dt.datetime.now()
    time_now = (now.hour, now.minute)
    if time_now == (19, 45):
        print(f"Hello world it's {now.hour}:{now.minute}!")
        tweet(now.hour, now.minute)
    time.sleep(60)
