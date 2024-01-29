from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# While true game continues
game_on = True

# Set the screen size
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
# Create objects from Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Create an object from Ball
ball = Ball()
# Create scoreboard
scoreboard = Scoreboard()

# set keyboards key to control the paddles
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
