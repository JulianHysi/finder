"""Create the route functions needed for navigating the application.

Use the route decorator of the Flask class on every function.
Use the render_template function of the flask package to render html pages.

Functions:

    index() -> string
    about() -> string
    signup() -> string
    login() -> string
    logout() -> string
    profile() -> string
    update_profile(form -> UpdateProfileForm, profile -> Profile)
    update_profile_pic(profile -> Profile, picture_file -> file object)
    prefill_profile_form(form -> UpdateProfileForm, profile -> Profile)
"""


import os
import secrets

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image

from finder import app, db, bcrypt
from finder.forms import SignUpForm, LogInForm, UpdateProfileForm
from finder.models import User, Profile


@app.route('/')
@app.route('/home')
def index():
    """Return the route for the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Return the route for the about page."""
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle the signup process.

    If the user is already authenticated, redirect them to the home page.
    Render the signup template.
    If the form validates, create the user and log them in.
    Create also the (empty) profile for that user.
    After that, redirect them home.
    If the form doesn't validate, re-render the signup template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_pwd)
        db.session.add(user)
        user_id = User.query.filter_by(username=user.username).first().id
        profile = Profile(user_id=user_id)
        db.session.add(profile)
        db.session.commit()
        flash(f'The account {username} was created successfully', 'success')
        login_user(user)
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle the login process.

    If the user is already authenticated, redirect them to the home page.
    Render the login template.
    If the form validates, and a user with such credentials exists:
        Log them in and redirect them to the home page.
        But if they were trying to access a login-required page, redirect to it.
    If the form doesn't validate, re-render the login template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle the logout process."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Handle loading and updating profile information.

    Update the profile if the form is posted correctly.
    Load the prefilled profile form on a GET request.
    """
    profile = current_user.profile
    form = UpdateProfileForm()
    if form.validate_on_submit():
        update_profile(form, profile)
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        prefill_profile_form(form, profile)
    return render_template('profile.html', profile=profile, form=form)

def update_profile(form, profile):
    """Update the profile with the posted data.

    Use this function for POST requests on the profile route.
    Update the profile of the current user,
    with the data posted on the profile form.
    Commit the changes to the db, and display a message.
    """
    profile.full_name = form.full_name.data
    profile.nick_name = form.nick_name.data
    profile.email = form.email.data
    profile.phone_number = form.phone_num.data
    profile.address = form.address.data
    profile.birth_date = form.birth_date.data
    profile.birth_place = form.birth_place.data
    profile.website = form.website.data

    if form.profile_pic.data:
        update_profile_pic(profile, form.profile_pic.data)

    db.session.commit()
    flash('Profile information has been updated', 'info')

def update_profile_pic(profile, picture_file):
    """Update the profile picture with the form posted file.

    Generate a random 128 bit hex.
    Get the extension of the uploaded file.
    Combine the 2 above to create a new and unique filename.
    Resize the uploaded picture to the wanted dimensions.
    Save the resized picture in the file system proper path.
    Update the profile_pic field on the db record.
    """
    random_hex = secrets.token_hex(16)
    _, file_ext = os.path.splitext(picture_file.filename)
    file_name = random_hex + file_ext
    file_path = os.path.join(
        app.root_path,'static/pictures/profile_pics', file_name)

    size = (120, 120)
    resized_pic = Image.open(picture_file)
    resized_pic.thumbnail(size)  # resize the pic
    resized_pic.save(file_path)

    old_file_name = profile.profile_pic
    if old_file_name != 'default.png':
        os.remove(os.path.join(
            app.root_path, 'static/pictures/profile_pics', old_file_name))

    profile.profile_pic = file_name

def prefill_profile_form(form, profile):
    """Prefill the profile form with the existing data.
    
    Use this function for GET requests on the profile route.
    Fill the profile form fields with existing data,
    so that when the form loads, it is already completed.
    """
    form.full_name.data = profile.full_name
    form.nick_name.data = profile.nick_name
    form.email.data = profile.email
    form.phone_num.data = profile.phone_number
    form.address.data = profile.address
    form.birth_date.data = profile.birth_date
    form.birth_place.data = profile.birth_place
    form.website.data = profile.website
