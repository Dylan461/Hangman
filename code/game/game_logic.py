from word_generator import WordGenerator

word = ""
letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
alist = []

def start_game(self):
    wg = WordGenerator()
    self.word = wg.generate_word()
    self.alist = list(letters)

def get_word(self):
    return self.word

def word_contains_letter(self, char):
    if char in self.word:
        return True
    return False

def remove_from_list(self, char):
    if char in self.alist:
        alist.remove(char)

def list_contains_letter(self, char):
    if char in self.alist:
        return True
    return False