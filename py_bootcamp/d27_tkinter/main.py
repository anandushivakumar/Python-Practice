from tkinter import *

window = Tk()
window.title("Test program")
window.minsize(width=500, height=300)

# label
label = Label(text = "I am a label", font=("Arial", 24))
label.pack() # to show the label on the screen

# button
def button_click():
    print("I got clicked")
    new_text = input.get()
    label.config(text = new_text)

button = Button(text = "Click me", command=button_click)
button.pack()

# entry
input = Entry(width=10)
input.pack()

window.mainloop()