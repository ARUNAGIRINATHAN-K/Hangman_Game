import random
import tkinter as tk
from tkinter import messagebox

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x500")

        # Game variables
        self.words = ['python', 'programming', 'computer', 'algorithm', 'database', 'network']
        self.word = random.choice(self.words)
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.lives = 6

        # Hangman stages
        self.hangman_stages = [
            '''
             ------
             |    |
                  |
                  |
                  |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
                  |
                  |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
             |    |
                  |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
            /|    |
                  |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
            /|\\   |
                  |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
            /|\\   |
            /     |
                  |
            =========''',
            '''
             ------
             |    |
             O    |
            /|\\   |
            / \\   |
                  |
            ========='''
        ]

        # GUI elements
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack(pady=10)

        self.hangman_label = tk.Label(self.root, text=self.hangman_stages[0], font=("Courier", 12))
        self.hangman_label.pack()

        self.word_label = tk.Label(self.root, text=self.get_word_display(), font=("Arial", 20))
        self.word_label.pack(pady=10)

        self.lives_label = tk.Label(self.root, text=f"Lives: {self.lives}", font=("Arial", 12))
        self.lives_label.pack()

        self.guessed_label = tk.Label(self.root, text="Guessed: ", font=("Arial", 12))
        self.guessed_label.pack()

        self.input_entry = tk.Entry(self.root, width=5, font=("Arial", 12))
        self.input_entry.pack(pady=10)
        self.input_entry.focus()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.process_guess)
        self.guess_button.pack()

        # Bind Enter key to process guess
        self.root.bind('<Return>', lambda event: self.process_guess())

    def get_word_display(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def update_display(self):
        self.hangman_label.config(text=self.hangman_stages[6 - self.lives])
        self.word_label.config(text=self.get_word_display())
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.guessed_label.config(text=f"Guessed: {' '.join(sorted(self.guessed_letters))}")
        self.input_entry.delete(0, tk.END)

    def process_guess(self):
        guess = self.input_entry.get().lower()
        if not guess or len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            self.input_entry.delete(0, tk.END)
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            self.input_entry.delete(0, tk.END)
            return

        self.guessed_letters.add(guess)
        if guess in self.word_letters:
            self.word_letters.remove(guess)
        else:
            self.lives -= 1

        self.update_display()

        if self.lives == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {self.word}.")
            self.root.quit()
        elif not self.word_letters:
            messagebox.showinfo("Congratulations", f"You won! The word was {self.word}.")
            self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()