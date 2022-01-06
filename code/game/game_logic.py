from game.word_generator import WordGenenator

word = ""
letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
alist = []
incorrect_guesses = []
max_incorrect_guesses = 8
count = 0
game_status = "Stop"
display = ""


class GameLogic:
    def start_game(self):
        wg = WordGenenator()
        self.word = wg.generate_word()
        self.alist = list(letters)
        self.count = 0
        self.game_status = "Running"
        self.incorrect_guesses = []
        str = ""
        for i in range(0, len(self.word) - 1):
            str = str +  "_"
        self.display = str

    '''
    Checks
    '''

    def word_contains_letter(self, char):
        for i in range(0, len(self.word) - 1):
            if char == self.word[i]:
                return True
        return False

    def list_contains_letter(self, char):
        if char in alist:
            return True
        return False

    def win_check(self):
        i = 0
        while i in range(0, len(self.display)):
            if self.display[i] == "_":
                return
            i += 1
        self.game_status = "Win"

    def lose_check(self):
        if count == max_incorrect_guesses:
            self.game_status = "Lose"


    '''
    Add
    '''

    def add_incorrect_list(self, char):
        incorrect_guesses.append(char)

    '''
    Remove
    '''

    def remove_from_list(self, char):
        if char in self.alist:
            self.alist.remove(char)

    '''
    Player Guesses
    '''

    def incorrect_guess(self):
        self.count += 1

    def correct_guess(self, char):
        new_word = ""
        for i in range(0, len(self.word) - 1):
            if char == self.word[i]:
                new_word += char
            elif self.display[i] != "_":
                new_word += self.display[i]
            else:
                new_word += "_"
        self.display = new_word

    '''
    Getters
    '''

    def get_display(self):
        return self.display

    def get_word(self):
        return word

    def is_in_list(self, char: str):
        return char in self.alist

    def get_game_status(self):
        return self.game_status

    def get_letters(self):
        return list(self.letters)