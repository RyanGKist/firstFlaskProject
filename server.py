from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index ():
	return render_template("index.html")

@app.route('/about_me')
def about_me():
	return render_template("about.html")

@app.route('/projects_by_me')
def projects():
	return render_template("projects.html")

app.run(debug=True)