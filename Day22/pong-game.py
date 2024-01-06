from turtle import Screen
from center_line import CenterLine
# from ball import Ball
# from scoreboard import Scoreboard
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
is_game_on = True

center_line = CenterLine()
paddle_1 = Paddle()
# paddle_2 = Paddle()
while is_game_on:
    screen.update()
    time.sleep(1)
    paddle_1.move()

screen.exitonclick()
