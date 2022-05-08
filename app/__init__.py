from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

def create_app(config_name):
# Initializing application
    app = Flask(__name__)

# Setting up configuration
    app.config.from_object(DevConfig)

    #initialising flask extensions
    db.init_app(app)
    bootstrap = Bootsrap

    return app