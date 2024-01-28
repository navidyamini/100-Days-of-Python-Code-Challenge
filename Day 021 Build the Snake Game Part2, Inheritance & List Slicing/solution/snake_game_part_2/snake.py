from turtle import Turtle

X = -20
Y = 0
MOVE_DISTANCE = 20
SEGMENTS_NO = 3
SHAPE = "square"
SNAKE_COLOR = "white"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake"""
        # Create 3 segments with square shape in horizontal position with white color
        for index in range(0, SEGMENTS_NO):
            self.add_segment(index * X, Y)

    def add_segment(self, x, y):
        """Add segment to snake"""
        new_turtle = Turtle()
        new_turtle.shape(SHAPE)
        new_turtle.color(SNAKE_COLOR)
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        self.segments.append(new_turtle)

    def extend(self):
        """Add new segment to the end of snake"""
        x = self.segments[-1].position()[0]
        y = self.segments[-1].position()[1]
        self.add_segment(x, y)

    def move(self):
        """Moving the snake by MOVE_DISTANCE"""
        # starts from the last one and move it to the last-1 position
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Set the snake heading to north or up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set the snake heading to south or down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set the snake heading to west or left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set the snake heading to east or right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
