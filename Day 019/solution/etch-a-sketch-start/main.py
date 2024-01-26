from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def move_backward():
    tim.backward(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.exitonclick()
