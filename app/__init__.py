from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app(confg_name):
    app = Flask(__name__)

#setting up configuratin
app.config.from_object(config_options[config_name])


#initialising flask extensions
db.init_app(app)