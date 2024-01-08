import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
user = Player()
car_manager = CarManager()
score = Scoreboard()
screen.onkey(user.move, "Up")
count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if count % 6 == 0:
        car_manager.create_car()
    count += 1
    screen.update()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(user) <= 20:
            turtle.write(f"Game Over!", align="center", font=("courier", 24, "normal"))
            game_is_on = False

    if user.check_win():
        score.score_increment()
        car_manager.level_up()

screen.exitonclick()
