import os
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery

app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jina environment
app.jinja_env.globals.update(**all_definitions)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

GALLERY_PATH = os.path.join(app.root_path, 'static', 'images', 'gallery')
gallery.define(app, "Main Gallery", "/gallery", GALLERY_PATH)

testz = ['h','y']
#with app.test_request_context('/testz',method='POST'):
#	assert request.path == '/test'
#	assert request.method == 'POST'
#	testz.append(request.form['sam'])


@app.route("/test")
def test():
#	with app.test_request_context('/test',method='POST'):
#		testz.append(request.data)
	tez = ['4', '22']
	return 'test' + 'n' + string(tez)


@app.route("/")
def main():
	return render_template("main.html")

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)
