from game.word_generator import WordGenenator
from game.game_logic import GameLogic
import tkinter as tk
import sys

class Game():

    wg = WordGenenator()
    window = tk.Tk()
    window2 = tk.Tk()
    window2.withdraw()
    gl = GameLogic()
    button_list = []
    word_display = tk.Label(window, font = ("Arial", 25))
    photo = tk.PhotoImage(file = "")
    photo_lbl = tk.Label()
    image_str = "images/image"
    image_num = 1

    '''
    Button actions
    '''

    def reset_button(self, button):
        button["state"] = tk.NORMAL
        button["relief"] = tk.RAISED

    def disable_button(self, button):
        button["state"] = tk.DISABLED
        button["relief"] = tk.FLAT

    def disable_all_letter_buttons(self):
        for button in self.button_list: 
            self.disable_button(button)

    def restart_game(self):
        self.gl.set_word(self.wg.generate_word())

        for button in self.button_list:
            self.reset_button(button)
        self.gl.start_game()
        self.photo = tk.PhotoImage(file = "")
        self.photo_lbl["image"] = self.photo
        new_str = self.text_display_format(self.gl.get_display())
        self.word_display["text"] = new_str
        self.window2.withdraw()
        self.image_num = 1


    #Letter button inputs
    def button_input(self, button):
        user_input = button.cget("text")
        self.disable_button(button)
        if user_input != "":
            if self.gl.is_in_list(user_input):
                if self.gl.word_contains_letter(user_input):
                    self.gl.correct_guess(user_input)
                    self.gl.win_check()
                    temp = self.text_display_format(self.gl.get_display())
                    self.word_display["text"] = temp
                else:
                    self.gl.incorrect_guess()
                    self.gl.lose_check()
                    temp = self.image_str + str(self.image_num) + ".png"
                    self.image_num += 1
                    self.photo = tk.PhotoImage(file = temp)
                    self.photo_lbl["image"] = self.photo

                self.gl.remove_from_list(user_input)
        game_status = self.gl.get_game_status()
        if game_status == "Win":
            self.disable_all_letter_buttons()
            self.open_end_screen("Congradulations")
        elif game_status == "Lose":
            self.disable_all_letter_buttons() 
            self.word_display["text"] = self.gl.get_word()
            self.open_end_screen("Game Over")

    #Open game window
    def open_window(self):

        self.gl.set_word(self.wg.generate_word())
        self.gl.start_game()

        self.photo_lbl.configure(image = self.photo)
        self.photo_lbl = tk.Label(image = self.photo, height = 500)
        self.photo_lbl.grid(row = 0, column = 0, columnspan = 26)

        str = self.gl.get_display()
        self.word_display["text"] = self.text_display_format(str)
        self.word_display.grid(columnspan = 26, row = 1, column = 0)

        spacer_lbl = tk.Label(height = 5)
        spacer_lbl.grid(row = 2, column = 0, columnspan = 26)

        i = 0
        for letter in self.gl.get_letters():
            button = tk.Button(self.window, text = letter, width = 5 ,disabledforeground = "white", relief = tk.RAISED)
            button["command"] = lambda button = button: self.button_input(button)
            self.button_list.append(button)
            button.grid(row = 3, column = i)
            i += 1

        self.window_settings(self.window)
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def open_end_screen(self, str):
        self.window2 = tk.Tk()
        self.window2.geometry("500x500")
        self.window_settings(self.window2)

        status_lbl = tk.Label(self.window2, text = str, font = ("Arial", 25))
        status_lbl.pack(pady = 80)
        play_again_btn = tk.Button(self.window2, text = "Play Again", command = lambda : self.restart_game())
        play_again_btn.pack(pady = 50)
        exit_button = tk.Button(self.window2, text = "Exit", command = lambda : self.exit())
        exit_button.pack(pady = 50)

    def text_display_format(self, str):
        new_str = str[0]
        for i in range(1, len(str)):
            new_str = new_str + " " + str[i]
        return new_str

    def window_settings(self, win):
        win.wm_attributes("-toolwindow", "True")
        win.overrideredirect(True)

    def exit(self):
        self.window.destroy()
        self.window2.destroy()
        sys.exit()


g = Game()
g.open_window()