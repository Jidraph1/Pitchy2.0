from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .config import DevConfig

def create_app(config_name):
# Initializing application
    app = Flask(__name__)

# Setting up configuration
    app.config.from_object(DevConfig)

    #initialising flask extensions
    db.init_app(app)
    bootstrap = Bootsrap

    return app