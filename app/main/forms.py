from flask_wtf import FlaskFofrm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    dnasjn