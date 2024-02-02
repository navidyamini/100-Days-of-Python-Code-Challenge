from turtle import Turtle

FONT = ("Courier", 6, "normal")


class StateCapital(Turtle):
    def __init__(self, name, xcor, ycor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(xcor, ycor)
        self.write(f"{name}", align="center", font=FONT)