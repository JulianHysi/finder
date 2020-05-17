from os import environ
from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

import finder.routes