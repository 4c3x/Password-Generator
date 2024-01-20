import tkinter as tk
from tkinter import ttk
from random import choice, shuffle
import string
from datetime import datetime

def generate_password():
    def get_random_word():
        word_list = ["brabus",
                     "banana",
                     "javelin",
                     "dog",
                     "carrots",
                     "spain",
                     "happy",
                     "jazz",
                     "kangaroo",
                     "lemon",
                     "mango",
                     "zebra"]
        return choice(word_list)

    
    password = get_random_word().capitalize() + get_random_word().capitalize()

    password += ''.join(choice(string.ascii_uppercase) for _ in range(2))

    password += str(choice(range(10))) + choice(string.punctuation)

    password_list = list(password)
    shuffle(password_list)
    shuffled_password = ''.join(password_list)

    generated_password.set(shuffled_password)

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    message_label.config(text=f"Password generated on {current_time}")

    add_to_table(shuffled_password, current_time)

def add_to_table(password, date_time):
    table.insert("", 0, values=(password, date_time))
    
    if table.get_children():
        if len(table.get_children()) > 10:
            table.delete(table.get_children()[-1])


window = tk.Tk()
window.title("Memorable Password Generator")

generate_button = tk.Button(window, text="Generate Memorable Password", command=generate_password)

generated_password = tk.StringVar()
password_label = tk.Label(window, textvariable=generated_password)

message_label = tk.Label(window, text="")

columns = ("Password", "Date and Time")
table = ttk.Treeview(window, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.pack()

generate_button.pack(pady=10)
password_label.pack()
message_label.pack()

window.mainloop()
