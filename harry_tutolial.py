# import datetime
#
# try:
#     login_str = input("Please put your entered time (format: HH:MM): ")
#     login_time = datetime.datetime.strptime(login_str, "%H:%M")
#     login_hour = login_time.hour
#
#     if login_hour >=9 and login_hour== 9:
#         print("Good morning")
#     elif login_hour >=4 and login_hour== 4:
#         print("Good afternoon")
#     else:
#         print("You are late")
# except ValueError:
#     print("Invalid time Format. Please enter time in the format HH:MM.")

# print(5**3)
import tkinter as tk
import random
import requests


def get_random_word():
    # Use the Datamuse API to get a random English word
    url = 'https://api.datamuse.com/words?random=true'
    response = requests.get(url)
    if response.status_code == 200:
        word_data = response.json()
        return word_data[0]['word']
    else:
        return None


def check_answer(word):
    # Use the Datamuse API to check if the input word is a valid English word
    url = f'https://api.datamuse.com/words?sp={word}&max=1'
    response = requests.get(url)
    return response.status_code == 200 and len(response.json()) > 0


def check_answer_and_update(result_label, word_entry):
    word = get_random_word()
    user_input = word_entry.get().lower()

    if check_answer(user_input):
        result_label.config(text="Correct! You guessed a valid English word.")
    else:
        result_label.config(text="Incorrect. Try again with a valid English word.")


def setup_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Word Game App")

    # Create labels and entry fields
    word_label = tk.Label(window, text="Guess the word:")
    word_label.pack()

    word_entry = tk.Entry(window)
    word_entry.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    # Create a button for submitting the answer
    submit_button = tk.Button(window, text="Submit", command=lambda: check_answer_and_update(result_label, word_entry))
    submit_button.pack()

    return window, word_entry


def main():
    window, word_entry = setup_gui()
    window.mainloop()


if __name__ == "__main__":
    main()

