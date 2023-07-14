from petfax import create_app
app = create_app()
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index(): 
    return 'Hello, PetFax!'


@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
from petfax import create_app
app = create_app()