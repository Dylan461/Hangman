import random

class WordGenenator:
    words = []
    file_name = "text_files\words.txt"

    def __init__(self):
        f = open(self.file_name)

        for line in f:
            self.words.append(line)

        f.close()

    def generate_word(self):
        return random.choice(self.words)
