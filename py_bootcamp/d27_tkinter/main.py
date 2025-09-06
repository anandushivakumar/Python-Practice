# miles to kilometers converter project

from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)

# entry widget for miles input
miles = Entry(window, width = 10)

# label widget for miles, "is equal to", result and "kilometers"
miles_label = Label(window, text = "Miles")
is_equal_to = Label(window, text = "is equal to")
km_result_label = Label(window, text = "0")
km_label = Label(window, text = "Kilometers")

# button for conversion
calculate = Button(window, text = "calculate")

# place the widgets according to grid
miles.grid(row = 0, column = 1)
miles_label.grid(row = 0, column = 2)
is_equal_to.grid(row = 1, column = 0)
km_result_label.grid(row = 1, column = 1)
km_label.grid(row = 1, column = 2)
calculate.grid(row = 3, column = 1)

# config
window.config(padx = 20, pady = 20)

# function for conversion
def conversion():
    mi = float(miles.get())
    km = mi * 1.609 
    km_result_label.config(text = f"{km:.2f}")

# bind button
calculate.config(command=conversion)

window.mainloop()