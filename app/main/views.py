from flask import render_template
from app import app

#main view
@app.route('/')
def index():

    """
    View root page function that returns the index page and its data
    
    """
    title = 'Home Page'
    return render_template('index.html', title = title)