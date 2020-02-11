import flask
import os
import requests
import spoon_api
import twitter_api
import random


app = flask.Flask(__name__)


@app.route('/')
def index():
    randomize = random.randint(0, 9)

    current_tweet = twitter_api.json_body["statuses"][randomize]
    current_cell = spoon_api.json_body["results"][randomize]
    
    tw = current_tweet["full_text"]
    sn = current_tweet["user"]["screen_name"]
    t = current_cell["title"]
    p = current_cell["readyInMinutes"]
    i = current_cell["image"]
    l = current_cell["sourceUrl"]
    
   
    return flask.render_template("index.html", title=t, prep_time=p, image=i, link=l, tweet=tw, screen_name=sn)
    
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
    )