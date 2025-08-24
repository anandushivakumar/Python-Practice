# drawing the dots
import turtle as t
import random
from extract_colours import color_list

t.colormode(255)
turt = t.Turtle()
turt.speed("fastest")
turt.pensize(20)
turt.hideturtle()

turt.penup()
turt.setheading(225)
turt.forward(350)
turt.setheading(0)
turt.pendown()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.penup()
    turt.forward(50)
    turt.pendown()
    if dot_count % 10 == 0:
        turt.setheading(90)
        turt.penup()
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)
        turt.pendown()

t.done()