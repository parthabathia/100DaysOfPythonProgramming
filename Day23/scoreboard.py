from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def score_increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

