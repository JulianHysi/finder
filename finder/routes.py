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
"""


from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from finder import app, db, bcrypt
from finder.forms import SignUpForm, LogInForm
from finder.models import User


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
    If the form doesn't validate, re-render the login template.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle the logout process."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    """Return the route for the profile page."""
    return render_template('profile.html')
