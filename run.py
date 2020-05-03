from flask import Flask
from flask import render_template

app = Flask(__name__)

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
 
if __name__ == '__main__':
	app.run(debug=True)
