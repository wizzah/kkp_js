from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

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
	app.run()