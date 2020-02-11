import requests
import requests_oauthlib
import json
import os

url = "https://api.spoonacular.com/recipes/complexSearch?query=pudding&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="

oauth = requests_oauthlib.OAuth1(
    "API_Key"
    )

response = requests.get(url, auth=oauth)
sp_data = response.json()






