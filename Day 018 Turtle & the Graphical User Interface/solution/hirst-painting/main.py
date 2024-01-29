import colorgram
import turtle
import random

timy = turtle.Turtle()
timy.speed(0)
turtle.colormode(255)
num_dot_per_row = 10

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
color_list = [(201, 10, 34), (244, 234, 53), (240, 234, 2), (240, 36, 137), (214, 161, 79), (41, 81, 176), (35, 216, 72), (31, 39, 157), (203, 72, 22), (20, 150, 22), (204, 31, 109), (219, 162, 8), (69, 10, 27), (179, 18, 11), (57, 15, 10), (220, 139, 198), (70, 70, 228), (18, 19, 46), (12, 96, 62), (83, 193, 219), (78, 210, 145), (96, 234, 195), (238, 157, 218), (227, 73, 41), (0, 249, 227), (253, 5, 45)]

timy.penup()
timy.hideturtle()
timy.setheading(225)
timy.forward(300)
timy.setheading(0)

for _ in range(num_dot_per_row):
    for _ in range(num_dot_per_row):
        color = random.choice(color_list)
        timy.dot(20, color)
        timy.forward(50)
    timy.left(90)
    timy.forward(50)
    timy.left(90)
    timy.forward(500)
    timy.left(180)

screen = turtle.Screen()
screen.exitonclick()
