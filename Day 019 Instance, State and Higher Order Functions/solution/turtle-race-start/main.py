from turtle import Turtle, Screen
import random

game_on = True
X = -240
y = -55
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")

for index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=X, y=y)
    new_turtle.speed(0)
    y += 30
    turtles.append(new_turtle)

while game_on:
    distance = random.randint(0, 10)
    turtle = random.choice(turtles)
    turtle.forward(distance)
    if turtle.xcor() > 225.0:
        game_on = False
        if user_bet == turtle.pencolor():
            print(f"You've won! Turtle {turtle.pencolor()} is the winner.")
        else:
            print(f"You've Lost! Turtle {turtle.pencolor()} is the winner.")

screen.exitonclick()
