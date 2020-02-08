import flask
import os
import requests
import spoon_api

app = flask.Flask(__name__)

@app.route('/')
def index():
    t = spoon_api.title
    p = spoon_api.prep_time
    return flask.render_template("index.html", title=t, prep_time=p)
    
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
    )