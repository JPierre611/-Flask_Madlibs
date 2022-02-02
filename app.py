from imaplib import Int2AP
from click import prompt
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def select_story():
	"""Displays a drop-down list to select a story title."""
	return render_template('select.html', stories_length=len(stories), stories=stories)

@app.route('/words')
def show_words_form():
	"""Shows form prompting for all the words in the story."""
	index = int(request.args["stories"])
	story = stories[index]
	return render_template('words.html', title=story.title, index=index, words=story.prompts)

@app.route('/story')
def show_story():
	"""Shows the resulting story."""
	index = int(request.args["index"])
	story = stories[index]
	text = story.generate(request.args)
	return render_template('story.html', title=story.title, text=text)
