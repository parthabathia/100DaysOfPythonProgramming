from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []


def set_players():
    x, y = -200, -90
    for colour in colours:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colour)
        new_turtle.penup()
        new_turtle.goto(x, y)
        y += 30
        all_turtles.append(new_turtle)


def start_race(user_bet):
    if user_bet:
        is_race_on = True
    else:
        is_race_on = False

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


set_players()
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color from 'VIBGYOR'")
start_race(user_bet)
screen.exitonclick()
