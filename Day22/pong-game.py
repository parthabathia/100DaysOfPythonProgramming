import turtle
from turtle import Screen
from center_line import CenterLine
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

paddle_left = Paddle(-470, 0)
paddle_right = Paddle(470, 0)
ball = Ball()
center_line = CenterLine()
score_right = Scoreboard(70, 220)
score_left = Scoreboard(-70, 220)

screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if (ball.xcor() >= 450 and ball.distance(paddle_right) <= 50) or (
            ball.xcor() <= -450 and ball.distance(paddle_left) <= 50):
        ball.bounce_x()
    if ball.xcor() >= 500:
        score_left.score_increment()
        if score_left.score == 5:
            turtle.color("white")
            turtle.write("Left Wins!", align="center", font=("Courier", 50, "normal"))
            is_game_on = False
        ball.reset_position()
    if ball.xcor() <= -500:
        score_right.score_increment()
        if score_right.score == 5:
            turtle.color("white")
            turtle.write("Right Wins!", align="center", font=("Courier", 50, "normal"))
            is_game_on = False
        ball.reset_position()

screen.exitonclick()
