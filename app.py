# # Import depandency
# from flask import Flask

# # Create a new flask app instance
# app = Flask(__name__)

# # Create flask route
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# # Set the FLASK_APP environment variable to the name of our Flask file, app.py
# # go to the directory app.py is saved run following code in terminal
# """# export FLASK_APP=app.py
# #flask run"""
# #by running above code :Running on http://127.0.0.1:5000/ 
# # paste local host in web

#-----------------------------------------
# Add dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Add SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Add Flask dependencies
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session
session = Session(engine)

#Set up flask 
#Create flask application called app
app = Flask(__name__)

# import app
# print("example __name__ = %s", __name__)
# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")

# Set up welcome route
@app.route("/")


def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
    ## Write flask run in terminal