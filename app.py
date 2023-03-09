from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/silly-story')
def create_silly_story():

    return render_template("questions.html",
                           prompts = silly_story.prompts)

@app.get('/excited-story')
def create_excited_story():

    return render_template("questions.html",
                           prompts = excited_story.prompts)

@app.get('/results')
def show_results():

    print(request)

    return render_template("results.html")