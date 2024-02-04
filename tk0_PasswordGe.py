import tkinter as tk
from tkinter import ttk
from random import choice, shuffle
import string
from datetime import datetime
import os

passwords = []

def generate_password():
    def get_random_word():
        word_list = ["ripple", "banana", "berry", "fog", "trout", "giraffe", "happy", "jazz", "kangaroo", "monday", "mango", "zebra"]
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

    save_passwords()

def add_to_table(password, date_time):
    timestamp = int(datetime.strptime(date_time, "%d-%m-%Y %I:%M:%S %p").timestamp())
    passwords.append((password, date_time, timestamp))

    passwords.sort(key=lambda x: x[2], reverse=True)

    update_table()

    if len(passwords) > 10:
        passwords.pop()

def update_table():
    for item in table.get_children():
        table.delete(item)

    for password, date_time, _ in passwords:
        table.insert("", "end", values=(password, date_time))

def load_passwords():
    try:
        with open(os.path.join(os.path.expanduser("~"), ".my_passwords.txt"), "r") as file:
            entries = [line.strip().split(",") for line in file]

            for entry in entries:
                if len(entry) == 3:  
                    password, date_time, timestamp = entry
                    passwords.append((password, date_time, int(timestamp)))

            passwords.sort(key=lambda x: x[2], reverse=True)

            update_table()
    except FileNotFoundError:
        pass

def save_passwords():
    password_file_path = os.path.join(os.path.expanduser("~"), ".my_passwords.txt")
    with open(password_file_path, "w") as file:
        for password, date_time, timestamp in passwords:
            file.write(f"{password},{date_time},{timestamp}\n")

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

load_passwords()

generate_button.pack(pady=10)
password_label.pack()
message_label.pack()

window.mainloop()
