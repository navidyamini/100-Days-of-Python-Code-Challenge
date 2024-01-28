from turtle import Turtle
import random

SHAPE = "circle"
SHAPE_SIZE = 0.5
COLOR = "blue"
SPEED = 0
COORDINATE = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=SHAPE_SIZE, stretch_wid=SHAPE_SIZE)
        self.color(COLOR)
        self.speed(SPEED)
        random_x = random.randint(COORDINATE * -1, COORDINATE)
        random_y = random.randint(COORDINATE * -1, COORDINATE)
        self.goto(random_x, random_y)

    def refresh(self):
        """Refresh the food's coordinate"""
        random_x = random.randint(COORDINATE * -1, COORDINATE)
        random_y = random.randint(COORDINATE * -1, COORDINATE)
        self.goto(random_x, random_y)
