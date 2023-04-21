from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog
from PIL import ImageTk, Image
import random
import pyperclip
import json
from ui_class import LABEL, BUTTON
from constants import COLOR, SYMBOL, NUMBERS, LETTERS


# Generating Password
def generate_password(l, n, s):
    password_letters = [random.choice(LETTERS) for _ in range(0, l)]
    password_symbols = [random.choice(SYMBOL) for _ in range(0, s)]
    password_numbers = [random.choice(NUMBERS) for _ in range(0, n)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)


def pop_up():
    root = tk.Tk()
    root.option_add('*background', COLOR)
    root.withdraw()
    root.geometry("240x100")

    # the input dialog
    number = simpledialog.askinteger(title="Password Generator",
                                     prompt="How many numbers do you want?:")
    letter = simpledialog.askinteger(title="Password Generator",
                                     prompt="How many letter do you want?:")
    symbol = simpledialog.askinteger(title="Password Generator",
                                     prompt="How many symbol do you want?:")

    generate_password(letter, number, symbol)


# Saving Password
def clear_text():
    """
         It clears the text that the user entered.
    """
    input_website.delete(0, 'end')
    input_pass.delete(0, 'end')


def save_entries():
    """
       It saves the texts that the user entered to txt file.
    """
    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(message=" Please don't leave any files empty!")

    else:
        try:
            with open("password_data.json", "r") as file:
                # read the data
                data = json.load(file)

        except FileNotFoundError:
            with open("password_data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # update the data
            data.update(new_data)

            with open("password_data.json", "w") as file:
                # save the data
                json.dump(data, file, indent=4)

        finally:
            clear_text()


def find_password():
    website = input_website.get()
    try:
        with open("password_data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def caps(event):
    v.set(v.get().upper())


# User Interface
window = Tk()
window.title("My Password Generator")
window.config(padx=50, pady=50, bg=COLOR)

canvas = Canvas(width=400, height=220, bg=COLOR, highlightthickness=0)
image = Image.open('pass_logo.png')
image = image.resize((320, 300), Image.ANTIALIAS)
pass_image = ImageTk.PhotoImage(image)
canvas.create_image(240, 100, image=pass_image)
canvas.grid(column=1, row=0)

# LABELS
labels = LABEL()

# ENTRIES
v = StringVar()
input_website = Entry(width=64, font=("Ariel", 10), textvariable=v)
input_website.grid(column=1, row=1)
input_email = Entry(width=80, font=("Ariel", 10))
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "name_surname@gmail.com")
input_pass = Entry(width=64, font=("Ariel", 10))
input_pass.grid(column=1, row=3)

input_website.bind("<KeyRelease>", caps)

# BUTTONS
generator_button = BUTTON("Generate Password", 2, 3, 1, pop_up, 14)
search_button = BUTTON("Search", 2, 1, 1, find_password, 14)
add_button = BUTTON("Add Password", 1, 4, 2, save_entries, 79)

window.mainloop()
