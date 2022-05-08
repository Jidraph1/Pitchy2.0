from flask import render_template
from flask_wtf import FlaskForm
from ..models import Users


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