import flask
import os
import requests
import spoon_api
import random


app = flask.Flask(__name__)



@app.route('/')
def index():
    
    randomize = random.randint(0, 9)

    current_cell = spoon_api.json_body["results"][randomize]
    
    t = current_cell["title"]
    p = current_cell["readyInMinutes"]
    
    return flask.render_template("index.html", title=t, prep_time=p)
    
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
    )