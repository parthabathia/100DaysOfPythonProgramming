from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""

    for i in range(5):
        password += random.choice(letters)

    for i in range(5):
        password += random.choice(numbers)

    for i in range(5):
        password += random.choice(symbols)

    password = ''.join(random.sample(password, len(password)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH DETAILS ------------------------------- #
def search_details():
    website = website_entry.get().title()
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n")
        else:
            messagebox.showinfo(title="Error", message=f"Data for {website} does not exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Details missing", message="Some details are left empty.")
    else:
        try:
            with open("password_manager.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_data, file, indent=2)
        else:
            data.update(new_data)
            with open("password_manager.json", "w") as file:
                json.dump(data, file, indent=2)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

search_details = Button(text="Search", width=14, command=search_details)
search_details.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.insert(0, "abc@xyz.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
