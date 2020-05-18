from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from finder import app
from finder.forms import SignUpForm, LogInForm


static_data = [{'name':'Genci', 'email':'genci@mail.com'},
               {'name':'Mondi', 'email':'mondi@mail.com'},
               {'name':'Berti', 'email':'berti@mail.com'}
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('users.html', data=static_data)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'The account {form.username.data} was created successfully', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.username.data == 'user1' and form.password.data == '123456':
            flash('You have been logged in!', 'info')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)