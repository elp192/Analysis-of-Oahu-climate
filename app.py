# Import depandency
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Create flask route
@app.route('/')
def hello_world():
    return 'Hello world'

# Set the FLASK_APP environment variable to the name of our Flask file, app.py
# go to the directory app.py is saved run following code in terminal
# export FLASK_APP=app.py
