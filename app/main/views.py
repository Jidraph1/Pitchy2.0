from flask import render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from .forms import LoginForm, RegisterForm, PitchForm, CommentForm
from ..models import Users, Pitch, Comment
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from . import main
from .. import db

# Views
@main.route('/')
def index():
    title = "Home page"
    return render_template('index.html', title = title)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
       
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html', form=form)