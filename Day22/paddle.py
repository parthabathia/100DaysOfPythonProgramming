from turtle import Turtle
import time


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.goto(x_cor, y_cor)

    def move_up(self):
        if self.ycor() < 300:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -300:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
