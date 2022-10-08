#! python 3

import json
import os


class MadLibs:
    path = '.\\templates'

    def __init__(self, word_description, template):
        self.template = template
        self.word_description = word_description
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_libs = cls(**data)
        return mad_libs

    def get_words_from_user(self):
        print('Please provide the following words:')
        for desc in self.word_description:
            ui = input(f'{desc}: ')
            self.user_input.append(ui)
        return self.user_input

    def build_story(self):
        story = self.template.format(*self.user_input)
        return story

    def display_story(self):
        print(story)


def select_template():
    print('Select a Mad Lib from the following list: ')
    templates = os.listdir(MadLibs.path)
    template = input(f'{templates} ')
    return template


temp_name = select_template()
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.display_story()
