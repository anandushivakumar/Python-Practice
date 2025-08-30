# creating the scoreboard class
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score1} : {self.score2}", align = "center", font = ("Arial", 24, "normal"))

    def increase_score1(self):
        self.score1 += 1
        self.update_scoreboard()
    
    def increase_score2(self):
        self.score2 += 1
        self.update_scoreboard()