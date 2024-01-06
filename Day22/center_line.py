from turtle import Turtle


class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() != -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
