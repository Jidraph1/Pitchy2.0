from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    username = StringField('Username', validators= [InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember')

    

