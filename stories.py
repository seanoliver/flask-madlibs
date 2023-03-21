import os
import re
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


def create_ai_story():

    content = fetch_gpt_story()
    terms = extract_terms(content)

    return Story(terms, content)

def fetch_gpt_story():

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": """You are a helpful assistant that generates funny
                        stories with blanked-out words indicated by curly
                        braces. The blanked words should be mad-libs style
                        descriptors of the type of word, such as noun,
                        adjective, adverb, person name, place, country, action
                        verb, etc.

                        Please respond with the mad-libs story only without any
                        chat-style conversation before or after the story
                        content. In other words, don't feel a need to say things
                        like: 'Sure thing! Here you go:' Instead, just respond
                        with the desired story itself."""},
            {"role": "user",
             "content": """Create a funny story for me with mad-libs style blank
                        words in curly braces."""}
        ]
    )

    return response['choices'][0]['message']['content']

def extract_terms(text):

    pattern = r'\{([^}]+)\}'
    terms = re.findall(pattern, text, flags=re.IGNORECASE)
    return terms


# Here's a story to get you started

silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

ai_story = create_ai_story()