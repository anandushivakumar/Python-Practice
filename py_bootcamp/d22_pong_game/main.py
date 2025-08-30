from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setting up the screen
screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
paddle.go_to((350, 0))
paddle2 = Paddle()
paddle2.go_to((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

# moving the paddle
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= -1
    
    # detect collision with paddle
    if (ball.distance(paddle) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.x_move *= -1
        ball.move_speed *= 0.9
    
    # keeping score
    if ball.xcor() > 380:
        scoreboard.increase_score1()
        ball.goto(0, 0)
        ball.x_move *= -1
        ball.move_speed = 0.1

    elif ball.xcor() < -380:
        scoreboard.increase_score2()
        ball.goto(0, 0)
        ball.x_move *= -1
        ball.move_speed = 0.1

screen.exitonclick()