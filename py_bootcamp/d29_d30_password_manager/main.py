from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)] 
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# save info into data.txt

def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title = "Error", message = "Please don't leave any fields empty!")
    else:
        if len(website) != 0 or len(password) != 0 or len(email) != 0:
            try:
                with open(file=r"py_bootcamp\d29_d30_password_manager\data.json", mode = "r") as file:
                    # read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(file=r"py_bootcamp\d29_d30_password_manager\data.json", mode = "w") as file:
                    json.dump(new_data, file, indent = 4)
            else:
                # update with new data
                data.update(new_data)

                with open(file=r"py_bootcamp\d29_d30_password_manager\data.json", mode = "w") as file:
                    # save new data
                    json.dump(data, file, indent = 4)
                    messagebox.showinfo(title = "Success", message = "Information saved successfully")
            finally:  
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get() # get user input for website name
    try:
        with open(file=r"py_bootcamp/d29_d30_password_manager/data.json", mode = "r") as file: # open file
            data = json.load(file) # load json data
            email = data[website]["email"] # get mail and password
            password = data[website]["password"]
            messagebox.showinfo(title = website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}") # display info
    except FileNotFoundError: # if file is not found
        messagebox.showinfo(title = "Error", message = "No data file found")
    except KeyError: # if the website is not found
        messagebox.showinfo(title = "Error", message = f"No details for {website} found")

# ---------------------------- UI SETUP ------------------------------- #
# creating window and window config
window = Tk()
window.title("Tkinter Password Manager")
window.config(padx=50, pady = 50)

logo = PhotoImage(file=r"py_bootcamp\d29_d30_password_manager\logo.png")
canvas = Canvas(window, width = 200, height = 200)
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

# email/username label and entry
email_label = Label(text = "Email/Username:")
email_entry = Entry(width = 50)
email_label.grid(row = 2, column = 0)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, "anandu.shivakumar@gmail.com")

# website label and entry
website_label = Label(text = "Website:")
website_entry = Entry(width = 32)
website_entry.focus()
website_label.grid(row = 1, column = 0)
website_entry.grid(row = 1, column = 1, columnspan = 1)

# password label, entry, generate password
password_label = Label(text="Password:")
password_entry = Entry(width=32)
password_button = Button(text = "Generate Password", width=14, command=generate_password)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_button.grid(row=3, column=2)

# add button
add_button = Button(text = "Add", width = 36, command=save_info)
add_button.grid(row = 4, column = 1, columnspan=2)

# search button
search_button = Button(text = "Search", width = 12, command = find_password)
search_button.grid(row = 1, column = 2)

window.mainloop()