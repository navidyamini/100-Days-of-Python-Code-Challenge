from turtle import Screen
from snake import Snake
import time

# While true game continues
game_on = True
# Set the screen size
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create 3 segments with square shape in horizontal position with white color
snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
while game_on:
    screen.update()
    time.sleep(0.1)
    # Move the snake
    snake.move()

screen.exitonclick()
