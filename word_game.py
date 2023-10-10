import http.client
import tkinter as tk
from tkinter import messagebox

def get_random_word():
    conn = http.client.HTTPSConnection("random-words5.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "d04a13536cmshb62d4597a725bcfp1d20cdjsne1f2b5ed852b",
        'X-RapidAPI-Host': "random-words5.p.rapidapi.com"
    }
    conn.request("GET", "/getRandom", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def display_word():
    global misspelled_word
    misspelled_word = get_random_word()
    word_label.config(text=f"Correct this word: {misspelled_word}")

def check_word():
    global score, misspelled_word
    user_input = entry.get()
    if user_input.lower() == misspelled_word.lower():
        misspelled_word = ""
    else:
        score += 1
    entry.delete(0, tk.END)
    update_score()
    display_word()

def update_score():
    score_label.config(text=f"Score: {score}")

def start_game():
    global player_name
    player_name = name_entry.get()
    if not player_name:
        messagebox.showwarning("Error", "Please enter your name!")
        return
    name_label.config(text=f"Welcome, {player_name}!")
    name_entry.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    display_word()

score = 0
misspelled_word = ""
player_name = ""

root = tk.Tk()
root.title("Word Game")
root.geometry("400x250")

welcome_label = tk.Label(root, text="Welcome to the Word Game!")
welcome_label.pack()

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

word_label = tk.Label(root, text="")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_word)
check_button.pack()

score_label = tk.Label(root, text="Score: 0")
score_label.pack()

root.mainloop()
