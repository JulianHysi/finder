"""Set up the imports, variables and configuration for the package.

Import the necessary third party packages.
Create an instance of the Flask application.
Configurate the secret key and database URI of the application.
Create the variables needed to be shared throughout the package.

Modules:

    models
    routes
    forms

Variables:
    
    app
    db
    bcrypt
    login_manager
"""


from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

import finder.routes
