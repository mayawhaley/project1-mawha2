import requests, requests_oauthlib
import json

url = "https://api.twitter.com/1.1/search/tweets.json?q=pudding%20dessert"

oauth = requests_oauthlib.OAuth1(
   
    )

response = requests.get(url, auth=oauth)
json_body = response.json()






# Heroku secrets
# TWI_Access_Token

# TWI_Access_Token_Secret

# TWI_API_Key

# TWI_API_Secret_Key