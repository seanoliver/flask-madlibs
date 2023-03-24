import sys
print(sys.executable)

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

from stories import ai_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def create_silly_story():
    """ renders a form that accepts words for the story's prompt """

    return redirect('/questions')


@app.get('/questions')
def story_questions():
    """ renders the list of questions for the user to populate the story"""

    story = ai_story
    return render_template(
        "questions.html",
        prompts=story.uniques)

@app.get('/result')
def show_results():
    """ renders the content with the user's provided madlib inputs """
    story = ai_story

    return render_template(
        "results.html",
        content=story.generate(request.args)
    )