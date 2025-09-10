from tkinter import *

THEME_COLOR = "#375362"

# py_bootcamp\d34_api_quiz_app\images\false.png
# py_bootcamp\d34_api_quiz_app\images\true.png

class QuizInterface: 
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(self.window, width = 300, height = 250, bg = "white")
        self.canvas.grid(row = 1, column= 0, columnspan = 2)

        self.score_label = Label()

        self.window.mainloop()
