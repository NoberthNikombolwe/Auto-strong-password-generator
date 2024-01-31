import random
import string
import tkinter as tk
from tkinter import ttk

def is_valid_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def is_valid_word(word):
    return word.isalpha()

def generate_custom_password(word, number, other_word):
    word = word.capitalize()
    word = word[:-1] + word[-1].upper()

    special_symbol = random.choice("!@#$%^&*()_-+=<>?")

    password = f"{word}{special_symbol}{number}{random.choice(string.punctuation)}{other_word}"
    return password

def generate_credentials():
    entered_word = word_entry.get()
    entered_number = number_entry.get()
    entered_other_word = other_word_entry.get()

    # Validation
    if not is_valid_word(entered_word):
        result_text.set("\nPlease enter a valid word in the Word field.")
        return
    
    if not is_valid_number(entered_number):
        result_text.set("\nPlease enter a valid number in the Number field.")
        return
    
    if not is_valid_word(entered_other_word):
        result_text.set("\nPlease enter a valid word in Other word fields.")
        return
    
    if not entered_other_word:
        result_text.set("\nPlease fill in Other word fields.")
        return

    password = generate_custom_password(entered_word, entered_number, entered_other_word)
    if len(password) <= 8:
        result_text.set("\nGenerated password must have more than 8 characters.")
        return

    result_text.set(f"\nGenerated Custom Password: {password}")



root = tk.Tk()
root.title("Password Generator")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter a Word:").grid(column=0, row=0, sticky=tk.W)
word_entry = ttk.Entry(frame)
word_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)

ttk.Label(frame, text="Enter a Number:").grid(column=0, row=1, sticky=tk.W)
number_entry = ttk.Entry(frame)
number_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

ttk.Label(frame, text="Enter Another Word:").grid(column=0, row=2, sticky=tk.W)
other_word_entry = ttk.Entry(frame)
other_word_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_credentials)
generate_button.grid(column=0, row=3, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text)
result_label.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
