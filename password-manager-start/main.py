from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

from param.ipython import message

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    # This block of code does the same thing as the one below it, however it is not conventional.
    # Using list comprehension like this is not their intended use, since they're intended to produce something,
    # rather than to do something. If the sole objective is to operate on something, a for loop should be used instead.
    # password_list = []
    # [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    # [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    # [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    # shuffle(password_list)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website and password:
        try:
            with open("cred_storage.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("cred_storage.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("cred_storage.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="One or more fields emtpy", message="Please don't leave any fields empty silly!")
# ---------------------------- CRED RETRIEVAL ------------------------------- #
def search_creds():
    website = website_entry.get()
    try:
        with open("cred_storage.json", mode="r") as cred_storage:
            # Reading old data
            data = json.load(cred_storage)
    except FileNotFoundError:
        print("You don't have anything saved")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="No website info", message=f"No details for {website} exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
lock_canvas = canvas.create_image(100,112, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "sample@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

#Buttons
password_gen_button = Button(text="Generate Password", command=generate_password)
password_gen_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

search_button = Button(text="Search", command=search_creds)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()
