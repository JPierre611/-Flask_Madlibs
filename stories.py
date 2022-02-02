"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a title, a list of prompts,
    and the text of the template.

        >>> s = Story("A simple tale", ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with title, words and template text."""

        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here are a few stories.

stories = [
    Story("A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    ),

    Story("A Simple Tale",
    ["plural_noun", "verb"],
    "I love to {verb} {plural_noun}."
    ),

    Story("A Friendly Tale",
    ["name", "noun"],
    "My name is {name}. would you please be my {noun}?"
    ),

    Story("A Current Event",
    ["plural_noun", "noun", "verb", "adjective", "proper_noun"],
    """Thousands of Canadian {plural_noun} traveled from all over the {noun} to
       Ottawa to {verb} against the government's quarantine requirements for {adjective}
       truckers returning to {proper_noun} after a trip to the USA.""" 
    )
]