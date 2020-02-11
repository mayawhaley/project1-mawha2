import requests
import requests_oauthlib
import json

url = "https://api.twitter.com/1.1/search/tweets.json?q=pudding%20dessert&tweet_mode=extended"

oauth = requests_oauthlib.OAuth1(
    "TWI_API_Key"
    "TWI_API_Secret_Key"
    "TWI_Access_Toke"
    "TWI_Access_Token_Secret"
    )

response = requests.get(url,auth=oauth)
json_body = response.json()
print(json.dumps(json_body))
