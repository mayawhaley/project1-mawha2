import requests
import json
import os
import random



url = "https://api.spoonacular.com/recipes/complexSearch?query=pudding&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="


# Heroku secrets
# api_key = os.getenv("API_Key")
# endpoint = "https://api.spoonacular.com/recipes/complexSearch?query=red-velvet&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="
# url = endpoint + str(api_key)


response = requests.get(url)
json_body = response.json()
# print(json.dumps(json_body))


