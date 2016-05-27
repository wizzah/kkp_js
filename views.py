from flask import Flask, render_template, send_from_directory
import os
from flask_flatpages import FlatPages
from flask_frozen import Freezer
app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index(gifs=None):
	gifs = []
	print os.getcwd()
	for i in os.listdir(os.getcwd()+'/gifs'):
		if i.endswith(".gif"):
			print i
			gifs.append(i)

	return render_template('ktwd.html', gifs=gifs)

@app.route('/gifs/<path:path>')
def send_gif(path):
	return send_from_directory('gifs', path)

if __name__ == "__main__":
	app.debug = True
	# app.run()
	 main.freezer.freeze()