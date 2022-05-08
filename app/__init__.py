from flask import Flask
from config import config_options

app = Flask(__name__)

#setting up configuratin
app.config.from_object(DevConfig)
