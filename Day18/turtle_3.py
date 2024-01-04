"""
Draw polygons from triangle to decagons starting from the same point using different colors for each polygon using
the turtle package.
"""

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "SeaGreen", "wheat", "SlateGrey", "Orchid",
          "Coral", "Violet"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for _ in range(3, 11):
    color = random.choice(colors)
    timmy.pencolor(color)
    colors.remove(color)
    draw_shape(_)

screen = Screen()
screen.exitonclick()

