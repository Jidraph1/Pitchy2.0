from flask import render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from ..models import Users, Pitch, Comment
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from .. import main
from . import db

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home page"
    return render_template('index.html', title = title)

@app.route('/signup')
def signup():
    """
    View sign up page
    """
    return render_template('signup.html')