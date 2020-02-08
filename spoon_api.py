import requests
import json

# add free parameter?
url = "https://api.spoonacular.com/recipes/complexSearch?query=red-velvet&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="

# get red velvet spoonacular endpoint + secret api key

# Heroku secrets
# url = 

# "API_Key"


# for parsing
response = requests.get(url)
json_body = response.json()

title = json_body["results"][0]["title"]
prep_time = json_body["results"][2]["readyInMinutes"]
#print(json.dumps(json_body, indent=2))
