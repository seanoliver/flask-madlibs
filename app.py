from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def create_silly_story():
    """ renders a form that accepts words for the story's prompt """

    return render_template(
        "questions.html",
        prompts=story.prompts)

@app.get('/results')
def show_results():
    """ renders the content with the user's provided madlib inputs """

    return render_template(
        "results.html",
        content=story.generate(request.args)
    )