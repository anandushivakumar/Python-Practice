from tkinter import *
import pandas
import random
import json
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# --------------- CREATE FLASH CARD -------------- #
try:
    data = pandas.read_csv(r"py_bootcamp\d31_flash_card\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"py_bootcamp\d31_flash_card\data\french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
    pandas.DataFrame(to_learn).to_csv(r"py_bootcamp\d31_flash_card\data\words_to_learn.csv", index=False)
else:
    to_learn = data.to_dict(orient = "records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(canvas_img, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(canvas_img, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"py_bootcamp\d31_flash_card\data\words_to_learn.csv", index = False)

    next_card()

# ------------ UI SETUP -------------- # 
# create and config window
window = Tk()
window.title("Flash Card program")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

# load images
right_img = PhotoImage(file = r"py_bootcamp\d31_flash_card\images\right.png")
wrong_img = PhotoImage(file = r"py_bootcamp\d31_flash_card\images\wrong.png")
card_front_img = PhotoImage(file = r"py_bootcamp\d31_flash_card\images\card_front.png")
card_back_img = PhotoImage(file = r"py_bootcamp\d31_flash_card\images\card_back.png")

# create and config canvas
canvas = Canvas(height = 526, width= 800, highlightthickness=0, background= BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 263, image = card_front_img)
canvas.grid(row = 0, column = 0, columnspan=2)
card_title = canvas.create_text(400, 150, text = "", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"))

# config buttons
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()