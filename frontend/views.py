from frontend import app
from flask import render_template

@app.route('/')
def home():
	return render_template('base.html')


@app.route('/route')
def route():
	return render_template('route.html')