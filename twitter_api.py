import requests
import requests_oauthlib
import json
import os

url = "https://api.twitter.com/1.1/search/tweets.json?q=pudding%20dessert&tweet_mode=extended"

key = os.getenv("TWI_API_Key")
secret = os.getenv("TWI_API_Secret_Key")
token = os.getenv("TWI_Access_Token")
token_secret = os.getenv("TWI_Access_Token_Secret")

oauth = requests_oauthlib.OAuth1(
    key,
    secret,
    token,
    token_secret
    )


response = requests.get(url, auth=oauth)
json_body = response.json()
