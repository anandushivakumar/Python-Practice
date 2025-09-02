from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

    # saving high score in a file
    def save_highscore(self):
        with open("data.txt", mode = "w") as file:
            file.write(f"{self.highscore}")
    
    # loading high score from a file
    def load_highscore(self):
        with open("data.txt", mode = "r") as file:
            self.highscore = int(file.read())
    
    def update_scoreboard(self):
        self.clear()
        self.load_highscore()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
    
    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()