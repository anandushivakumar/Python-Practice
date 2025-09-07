from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# save info into data.txt

def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open(file=r"py_bootcamp\d29_password_manager\data.txt", mode = "a") as file:
        file.write(f"{website} | {email} | {password}")
        file.write("\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tkinter Password Manager")
window.config(padx=50, pady = 50)

logo = PhotoImage(file=r"py_bootcamp\d29_password_manager\logo.png")
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
website_entry = Entry(width = 50)
website_entry.focus()
website_label.grid(row = 1, column = 0)
website_entry.grid(row = 1, column = 1, columnspan = 2)

# password label, entry, generate password
password_label = Label(text="Password:")
password_entry = Entry(width=32)
password_button = Button(text = "Generate Password", width=14)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_button.grid(row=3, column=2)

# Add button
add_button = Button(text = "Add", width = 36, command=save_info)
add_button.grid(row = 4, column = 1, columnspan=2)

window.mainloop()