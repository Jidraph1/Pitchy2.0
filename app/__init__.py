from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flas_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

#setting up configuratin
app.config.from_object(config_options[config_name])


#initialising flask extensions
db.init_app(app)
bootstrap = Bootstrap(app)