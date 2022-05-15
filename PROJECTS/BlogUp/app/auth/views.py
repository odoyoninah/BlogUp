from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from . import auth

# Registration Route
@auth.route('/register', methods = ['GET', 'POST'])
def register():
     
    registration_form = RegistrationForm()

    title = 'App Sign Up'

    if registration_form.validate_on_submit():

        user = User(email = registration_form.email.data, username = registration_form.username.data, password = registration_form.password.data )
         
        user.save_user()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title = title, registration_form = registration_form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():

    login_form = LoginForm()

    title = 'Post Login'

    if login_form.validate_on_submit():

        user = User.query.filter_by(email = login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('invalid Username or Password')

         

    return render_template('auth/login.html', login_form = login_form, title = title)

    
@auth.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('main.index'))

    
