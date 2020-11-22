from flask import Flask
from flask import Flask, url_for
from flask import request
from flask import Flask, Response
from flask import render_template
from markupsafe import escape

####
## Team Echo
## Project - Travel Recommender
## Becca Meares
## Bryan Arment
## Bryant Hicks
## Jeff Dank
## CSPB 3308
####

app = Flask(__name__)



@app.route('/best_airports/')
def sfile():
    return render_template("best_airports.html")

@app.route('/itinerary/')
def itin():
    return render_template("itinerary.html")



@app.route('/travel_recommender/')
def tr():
    return render_template("travel_recommender.html")
