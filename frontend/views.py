from frontend import app

@app.route('/')
def home():
	return render_template('base.html')