import requests
import requests_oauthlib
import json
import os

url = "https://api.spoonacular.com/recipes/complexSearch?query=pudding&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="
api_key = os.getenv("API_Key")

# "541651421a774a08bbadc9089fe32d78"

# oauth = requests_oauthlib.OAuth1(
    
#     )

response = requests.get(url, api_key)
# ,auth=oauth)
json_body = response.json()






