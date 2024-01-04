import random
import colorgram
import turtle


def extract_color():
    colors = colorgram.extract("image.jpeg", 30)
    rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    return rgb_colors


def move(colour):
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    x, y = timmy.pos()
    vertical = 0
    while vertical < 10:
        horizontal = 0
        while horizontal < 10:
            timmy.setposition(x, y)
            timmy.dot(20, random.choice(colour))
            horizontal += 1
            x += 50
        vertical += 1
        y += 50
        x -= 500
    timmy.hideturtle()


turtle.colormode(255)
timmy = turtle.Turtle()
colours = extract_color()
move(colours)

screen = turtle.Screen()
screen.screensize(300, 300)
screen.exitonclick()
