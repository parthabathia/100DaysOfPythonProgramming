"""
Move the turtle in random direction from the starting for a predetermined number of steps.
"""

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move(angle):
    timmy.setheading(angle)
    timmy.forward(20)


for _ in range(200):
    timmy.pensize(5)
    timmy.color(random_color())
    move(random.choice(direction))


screen = turtle.Screen()
screen.exitonclick()