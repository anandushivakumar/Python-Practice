import turtle as t
import random

# drawing dashed line
# for _ in range(50):
#     forward(10)
#     pencolor("white")
#     forward(10)
#     pencolor("black")

#####################################################################################

# drawing triangle, square, pentagon, hexagon, heptagon, octagon, nonago, decagon 
# for i in range(3, 11):
#     angle = 360/i
#     for _ in range(i):
#         forward(100)
#         right(angle)

#####################################################################################

# drawing a random walk
# t.colormode(255)
# turt = t.Turtle()
# turt.shape("turtle")

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b)

# directions = [0, 90, 180, 270]
# turt.pensize(10)
# turt.speed("fastest")

# for _ in range(200):
#     turt.forward(20)
#     turt.setheading(random.choice(directions))
#     turt.pencolor(random_color())

#####################################################################################

# drawing a spirograph
t.colormode(255)
turt = t.Turtle()
turt.shape("turtle")
turt.speed("fastest")
radius = 100

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(int(360/1)):
    turt.pencolor(random_color())
    turt.circle(radius)
    turt.setheading(turt.heading() + 1)

t.done()