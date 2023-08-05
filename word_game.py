import tkinter as tk
import random
import string

# List of words for the crossword puzzle
word_list = ['crossword', 'letter', 'grid', 'python', 'game', 'puzzle', 'word']

# Dictionary of clues for each word
clues = {
    'crossword': "Clue for 'crossword' goes here.",
    'letter': "Clue for 'letter' goes here.",
    'grid': "Clue for 'grid' goes here.",
    'python': "Clue for 'python' goes here.",
    'game': "Clue for 'game' goes here.",
    'puzzle': "Clue for 'puzzle' goes here.",
    'word': "Clue for 'word' goes here.",
}

# Function to scramble a word
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Create the main window
window = tk.Tk()
window.title("Word Game")
window.geometry("400x400")

# Function to start the game
def start_game():
    player_name = name_entry.get().strip()
    if not player_name:
        return

    # Remove the GUI elements related to name entry and level selection
    welcome_label.pack_forget()
    name_label.pack_forget()
    name_entry.pack_forget()
    start_button.pack_forget()

    # Create GUI elements for the game
    level_label = tk.Label(window, text="Select level:")
    level_label.pack(pady=10)

    level_var = tk.StringVar()
    level_var.set("Easy")
    level_menu = tk.OptionMenu(window, level_var, "Easy", "Medium", "Hard")
    level_menu.pack()

    word_label = tk.Label(window, text="", font=("Arial", 20))
    word_label.pack(pady=20)

    score = 0
    current_word_index = 0

    def display_word():
        nonlocal current_word_index
        word = word_list[current_word_index]
        misspelled_word = scramble_word(word)
        word_label.config(text=f"Correct this word: {misspelled_word}")

    def submit_word():
        nonlocal current_word_index, score
        entered_word = word_entry.get().strip().lower()
        correct_word = word_list[current_word_index].lower()
        if entered_word == correct_word:
            score += 1
        current_word_index += 1
        if current_word_index < len(word_list):
            display_word()
            update_score()

    def update_score():
        score_label.config(text=f"Score: {score}/{len(word_list)}")

    word_entry = tk.Entry(window, font=("Arial", 16))
    word_entry.pack(pady=10)

    submit_button = tk.Button(window, text="Submit", command=submit_word)
    submit_button.pack(pady=10)

    score_label = tk.Label(window, text=f"Score: {score}/{len(word_list)}", font=("Arial", 16))
    score_label.pack(pady=10)

    display_word()

# Create GUI elements for name input and level selection
welcome_label = tk.Label(window, text="Welcome to Word Game!", font=("Arial", 20))
welcome_label.pack(pady=20)

name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window, font=("Arial", 16))
name_entry.pack(pady=10)

start_button = tk.Button(window, text="Start", command=start_game)
start_button.pack(pady=10)

# Run the main loop
window.mainloop()
