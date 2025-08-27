# turtle etch a sketch
from turtle import Screen, Turtle
import random

turt = Turtle()
screen = Screen()
turt.pensize(5)
turt.color("black")

def move_forward():
    turt.forward(10)

def move_backward():
    turt.backward(10)

def left():
    turt.left(10)

def right():
    turt.right(10)

def clear():
    turt.clear()
    turt.penup()
    turt.reset()
    turt.pendown()

screen.listen()
screen.onkey(key="w", fun = move_forward)
screen.onkey(key="s", fun = move_backward)
screen.onkey(key="a", fun = left)
screen.onkey(key="d", fun = right)
screen.onkey(key="c", fun = clear)
screen.exitonclick()