"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """Machine to select and return a random word from a given file.
    File must contain only one word per line. 
    """

    def __init__(self, dictionary_file_path):
        self.file = open(dictionary_file_path, 'r')
        self.word_list = self.make_word_list()
        print(f'{len(self.word_list)} words read')


    def make_word_list(self):
        """Creates list of all words contained in file"""
        word_list = []
        for line in self.file:
            word_list.append(line)
        return word_list

    def random(self):
        """Chooses and returns random word"""
        random_word = choice(self.word_list)
        return random_word[:-1]

class SpecialWordFinder(WordFinder):
    """A subset of WordFinder, this filters empty lines and lines that begin
    with a '#' for files that contain those"""

    def __init__(self, dictionary_file_path):
        super().__init__(dictionary_file_path)
        self.filtered_word_list = self.filter()

    def filter(self):
        """filters word list to remove empty lines and lines that begin with a '#'"""
        return [word for word in self.word_list if word != '' and word[:1] != '#']

    def random(self):
        """Chooses and returns random word from filtered list"""
        random_word = choice(self.filtered_word_list)
        return random_word[:-1]
