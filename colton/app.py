from flask import Flask, render_template, send_from_directory, request,url_for, redirect
import os, gallery, todo, complain, neato, comic, logo, cool, mario
app = Flask(__name__)

#HACK 
APP_ROOT_PATH = app.root_path

# DEFINITIONS
# To make definitions available in the templates,
# we need to add them to the jinja environment
neato.define_globals(app)

# ROUTING
# Those slow loading galleries we like so much.
gallery.define(app, "sketches", "/sketches", "sketches")
gallery.define(app, "my pixels", "/pixels", "pixels")

# Each day is something new
todo.define(app)

#Phil Fish 2 Simulator
complain.define(app)

# Comic
comic.define(app)

# I am a designer
logo.define(app)

# Who is cooler?
cool.define(app)

# Colton is cooler because Brandon wears glasses
mario.define(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')


def nl2br(value): 
	return value.replace('\n','<br>\n')
app.jinja_env.filters['nl2br'] = nl2br

# progress
@app.route("/progress")
def progress():
  return render_template("progress.html")     
	
# part time job app
@app.route("/parttime")
def parttime():
	full_path = os.path.join(app.root_path, "static", "parttimead.txt")
	with open(full_path,'r') as adFile:
		text = adFile.read()
	return render_template("parttime.html",text=text)


# This is my boilerplate code I will start with
@app.route("/boiler")
def boiler():
	return render_template("boiler.html")

# Now a word from our sponsors
@app.route("/coolfolk")
def coolfolk():
	return render_template("coolfolk.html")

@app.route("/resume")
@app.route("/resume/")
def resume():
	return redirect(url_for('static', filename='resume.pdf'))

@app.route("/transcript")
@app.route("/transcript/")
def transcript():
	return redirect(url_for('static', filename='transcript.pdf'))

@app.route("/gear")
def gear():
	return render_template("gear.html")

@app.route("/indiewishlist")
def indiewishlist():
	return render_template("indiewishlist.html")

@app.route("/verbthenoun")
def verbthenoun():
	return render_template("verbthenoun.html")

@app.route("/")
def main():
	return render_template("main.html")
# ERROR
@app.errorhandler(404)
def page_not_found(e):
	return render_template("pagenotfound.html"), 404

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	# TODO: Get logging to work
	app.run(debug=True)

