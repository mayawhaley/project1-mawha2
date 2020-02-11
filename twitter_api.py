import requests
import requests_oauthlib
import json

url = "https://api.twitter.com/1.1/search/tweets.json?q=pudding%20dessert&tweet_mode=extended"

oauth = requests_oauthlib.OAuth1(
    "TWI_Access_Token",
    "TWI_Access_Token_Secret",
    "TWI_API_Key",
    "TWI_API_Secret_Key"
    )

response = requests.get(url, auth=oauth)
json_body = response.json()

