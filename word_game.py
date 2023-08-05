import tkinter as tk
import random

# List of words for each level
word_list = {
    "easy": ["apple", "banana", "cherry", "orange", "grape"],
    "medium": ["elephant", "giraffe", "zebra", "kangaroo", "ostrich"],
    "hard": ["python", "javascript", "java", "cplusplus", "ruby"],
}

# Initialize variables
player_name = ""
level = ""
score = 0
current_word_index = 0
current_word = ""

# Function to start the game
def start_game():
    global player_name, level
    player_name = name_entry.get().strip()
    level = level_var.get()
    if player_name == "":
        tk.messagebox.showwarning("Error", "Please enter your name!")
    else:
        start_button.destroy()
        name_entry.destroy()
        level_label.destroy()
        level_menu.destroy()
        welcome_label.config(text=f"Welcome, {player_name}!")
        display_word()

# Function to display a misspelled word for the user to correct
def display_word():
    global current_word_index, current_word
    if current_word_index < len(word_list[level]):
        current_word = word_list[level][current_word_index]
        mixed_word = list(current_word)
        random.shuffle(mixed_word)
        misspelled_word.set("".join(mixed_word))
        current_word_index += 1
    else:
        finish_game()

# Function to submit the corrected word
def submit_word():
    global score
    if corrected_word.get().strip() == current_word:
        score += 1
    display_word()
    update_score()

# Function to update the score label
def update_score():
    score_label.config(text=f"Score: {score}/{len(word_list[level])}")

# Function to finish the game
def finish_game():
    word_label.destroy()
    corrected_word_entry.destroy()
    submit_button.destroy()
    score_label.config(text=f"Final Score: {score}/{len(word_list[level])}")

# Create the main window
root = tk.Tk()
root.title("Word Game")
root.geometry("400x300")

# Welcome label
welcome_label = tk.Label(root, text="Enter your name and select a level to start the game.")
welcome_label.pack(pady=10)

# Player name entry
name_entry = tk.Entry(root)
name_entry.pack()

# Level selection menu
level_var = tk.StringVar()
level_var.set("easy")
level_label = tk.Label(root, text="Select Level:")
level_label.pack()
level_menu = tk.OptionMenu(root, level_var, "easy", "medium", "hard")
level_menu.pack()

# Start button
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack(pady=10)

# Misspelled word display
misspelled_word = tk.StringVar()
word_label = tk.Label(root, textvariable=misspelled_word, font=("Arial", 24))
word_label.pack(pady=20)

# Entry for corrected word
corrected_word = tk.StringVar()
corrected_word_entry = tk.Entry(root, textvariable=corrected_word, font=("Arial", 16))
corrected_word_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_word)
submit_button.pack(pady=10)

# Score label
score_label = tk.Label(root, text="")
score_label.pack()

# Run the main loop
root.mainloop()
