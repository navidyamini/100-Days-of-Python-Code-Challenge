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
        self.high_score = self.read_high_score()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(X, Y)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the user score by one"""
        self.score += 1

    def update_scoreboard(self):
        """Update the scoreboard and refresh it"""
        self.increase_score()
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update_scoreboard()

    def save_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    @staticmethod
    def read_high_score():
        with open("data.txt", mode="r") as file:
            return int(file.read())

    # def game_over(self):
    #     """Show the game over sign"""
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
