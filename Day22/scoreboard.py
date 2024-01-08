from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))

    def score_increment(self):
        self.score += 1
        self.clear()
        self.score_update()
