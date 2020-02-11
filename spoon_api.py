import requests
import requests_oauthlib
import json
import os

url = "https://api.spoonacular.com/recipes/complexSearch?query=pudding&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="
# 541651421a774a08bbadc9089fe32d78"



response = requests.get(url + os.getenv("API_Key"))
json_body = response.json()
# print(json.dumps(json_body))





