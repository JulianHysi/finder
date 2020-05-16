from os import environ
from flask import Flask
from flask import render_template
from forms import SignUpForm, LogInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

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
	return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LogInForm()
	return render_template('login.html', form=form)
 
if __name__ == '__main__':
	app.run(debug=True)
