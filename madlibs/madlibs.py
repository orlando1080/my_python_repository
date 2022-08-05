import json
import os

class MadLibs:
    def __init__(self, word_description, template):
        self.template = template
        self.word_description = word_description

def get_words_from_user(word_description):
    print('Please provide the following words:')
    words = []
    for desc in word_description:
        user_input = input(f'A {desc}: ')
        words.append(user_input)
    return words

def build_story(template, words):
    story = template.format(*words)
    return story

def get_template(name, path='.\\templates'):
    fpath = os.path.join(path, name)
    with open(fpath, "r") as f:
        data = json.load(f)
    mad_libs = MadLibs(**data)
    print(mad_libs.word_description)

template_name = 'make me a video game.json'
get_template(template_name)

# template = 'Back when {} Walberg, was marky mark, this how we used to get the party {}!'
# words = get_words_from_user(['noun', 'verb'])
# story = build_story(template, words)
#
# print(story)