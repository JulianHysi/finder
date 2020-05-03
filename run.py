from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return '<h2>Hello Web</h2>'

@app.route('/about')
def about():
	return '<center>This is the about page</center>'
 
if __name__ == '__main__':
	app.run(debug=True)
