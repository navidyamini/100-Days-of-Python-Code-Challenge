from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# While true game continues
game_on = True
speed = 0.5
# Set the screen size
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create 3 segments with square shape in horizontal position with white color
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_on:
    screen.update()
    time.sleep(speed)
    # Move the snake
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()
        if len(snake.segments) % 5 == 0 and speed > 0.1:
            speed -= 0.1

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        speed = 0.5

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # If the head collides with any segment in the tail the game will be over.
        if snake.head.distance(segment) < 10:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            speed = 0.5


screen.exitonclick()
