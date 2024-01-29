import turtle
from turtle import Turtle, Screen
import random
timy = Turtle()
degrees = [0, 90, 180, 270]
timy.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Draw Spirograph
degree = 5
for _ in range(0, 360, degree):
    timy.color(random_color())
    timy.circle(100)
    timy.left(degree)

"""
# Draw Shapes
for i in range(3,11):
    timy.color(random_color())
    degree = 360 / i
    for j in range(i):
        timy.forward(100)
        timy.right(degree)

# Random Walk
timy.pensize(10)
for _ in range(200):
    timy.color(random_color())
    timy.forward(30)
    timy.setheading(random.choice(degrees))
"""

screen = Screen()
screen.exitonclick()



