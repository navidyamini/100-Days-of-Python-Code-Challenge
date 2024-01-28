from turtle import Turtle

X = 0
Y = 280
COLOR = "white"
STARTING_SCORE = 0
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(X, Y)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the user score by one"""
        self.score += 1

    def update_scoreboard(self):
        """Update the scoreboard and refresh it"""
        self.increase_score()
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Show the game over sign"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
