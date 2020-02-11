import requests
import requests_oauthlib
import json

url = "https://api.twitter.com/1.1/search/tweets.json?q=pudding%20dessert&tweet_mode=extended"

oauth = requests_oauthlib.OAuth1(
    "gnyHPeOlmdYuU4ecionYCPjOt",
    "clBi6W7KgQ9hoIQ9sZ3DbQAxOkp2k8ZGsUSe0F8ifQR7esp5Vs",
    
    
    "258103267-FCvy1NDM1wXGVmHzYnEPtL6k25ThFGs2PlHJI9YW",
    "w202ArZEDrQNSrY546wDCaPUtDed3R4So3s9yYhjgBhjL"
    )

response = requests.get(url,auth=oauth)
json_body = response.json()
print(json.dumps(json_body))
