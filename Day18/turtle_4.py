"""
Draw spirograph using different colors for each circle using the turtle package.
"""

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.fillcolor("coral")
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
