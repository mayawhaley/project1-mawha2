import requests
import json
import os

url = "https://api.spoonacular.com/recipes/complexSearch?query=pudding&addRecipeInformation=true&instructionsRequired=true%20free&apiKey="


response = requests.get(url + os.getenv("API_Key"))
json_body = response.json()