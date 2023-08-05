import tkinter as tk
import random
import string


# Function to generate a random word
def generate_random_word():
    word_length = random.randint(3, 8)  # Random word length between 3 and 8 characters
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(word_length))


# Generate a list of 1000 random words
word_list = [generate_random_word() for _ in range(1000)]


def get_random_word():
    return random.choice(word_list)


def check_answer(word):
    return word in word_list


def check_answer_and_update(result_label, word_entry):
    word = get_random_word()
    if word is None:
        result_label.config(text="Oops! Something went wrong. Please try again.")
        return

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
