from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# py_bootcamp\d34_api_quiz_app\images\false.png
# py_bootcamp\d34_api_quiz_app\images\true.png

class QuizInterface: 
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(self.window, width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text(150, 125, width = 280, text = "Question", font = ("Arial", 20, "italic"), fill = THEME_COLOR)
        self.canvas.grid(row = 1, column=0 , columnspan=2, pady=50)

        self.right_image = PhotoImage(file = r"py_bootcamp\d34_api_quiz_app\images\true.png")
        self.wrong_image = PhotoImage(file = r"py_bootcamp\d34_api_quiz_app\images\false.png")

        self.right_button = Button(image = self.right_image, highlightthickness = 0, command = self.right_button_pressed)
        self.right_button.grid(row = 2, column = 0)

        self.wrong_button = Button(image = self.wrong_image, highlightthickness = 0, command=self.wrong_button_pressed)
        self.wrong_button.grid(row = 2, column = 1)

        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.score_label = Label(text="Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)

            self.score_label.config(text = f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text = "Quiz Over!")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def right_button_pressed(self):
        self.feedback(self.quiz.check_answer("True"))
    
    def wrong_button_pressed(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def feedback(self, is_right):
        if is_right:
             self.canvas.config(bg = "green")
        else:
             self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)