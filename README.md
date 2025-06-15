**Hangman Game**
A Python-based Hangman game with a graphical user interface (GUI) built using Tkinter. Guess letters to uncover a hidden word before running out of lives, with a visual hangman figure updating as you play.
Features

Random word selection from a predefined list.
Tkinter GUI displaying:
Hangman figure (text-based).
Word with guessed letters revealed.
Lives remaining and guessed letters.
Input field and button for letter guesses.


Input validation for single letters and repeat guesses.
Win/lose message boxes with game end.
Press Enter or click "Guess" to submit letters.

Installation

**Prerequisites:**

Python 3.x installed (Tkinter is included in standard Python installations).
No additional libraries required.


**Clone the Repository:**
git clone https://github.com/ARUNAGIRINATHAN-K/hangman-game.git
cd hangman-game



**Usage**

Run the Game:
python hangman_gui.py


**How to Play:**

The game starts with a hidden word (e.g., _ _ _ _ _ _).
Enter a single letter in the input field.
Click "Guess" or press Enter to submit.
Correct guesses reveal letters in the word.
Incorrect guesses reduce lives and update the hangman figure.
Win by guessing the word before losing all 6 lives.
A message box shows the result, and the game closes.



**File Structure**

hangman_gui.py: Main game script with Tkinter GUI and game logic.
README.md: This file.

Built with Python and Tkinter.
Inspired by classic Hangman games.

