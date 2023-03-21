import sys
print(sys.executable)

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# from stories import silly_story as story
from stories import silly_story, excited_story, ai_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

stories = {
        "Silly Story" : silly_story,
        "Excited Story" : excited_story,
        "AI-Generated Story" : ai_story,
    }

@app.get('/')
def create_silly_story():
    """ renders a form that accepts words for the story's prompt """

    return render_template(
        "story_selector.html",
        templates=stories.keys()
    )


@app.get('/questions')
def story_questions():
    """ renders the list of questions for the user to populate the story"""

    story = stories[request.args['template']]
    return render_template(
        "questions.html",
        template=request.args['template'],
        prompts=story.prompts)

@app.get('/results/<template>')
def show_results(template):
    """ renders the content with the user's provided madlib inputs """
    story = stories[template]

    return render_template(
        "results.html",
        content=story.generate(request.args)
    )