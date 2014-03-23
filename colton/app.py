import os 
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery

app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jinja environment
app.jinja_env.globals.update(**all_definitions)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

GALLERY_PATH = os.path.join(app.root_path, 'static', 'images', 'gallery')
gallery.define(app, "Main Gallery", "/gallery", GALLERY_PATH)

ADIPOSE_SCORE_PATH = os.path.join(app.root_path, 'static','scores','adipose.score')
@app.route("/static/scores/adipose_check_is_highest_score", methods=["GET", "POST"])
def adipose_check_is_highest_score():
	if request.method == "POST":
		high_score = 9999999990
		with open(ADIPOSE_SCORE_PATH,'r') as _f:
			high_score = _f.readline()#name
			high_score = int(_f.readline().strip('\n'))
		return request.data
		if score  > high_score:
			return 'true'
		else:
			return 'false'
		
	elif request.method == "GET":
		return 'fuck off'	

@app.route("/")
def main():
	return render_template("main.html")

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)
