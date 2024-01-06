from turtle import Turtle
import time

STARTING_POSITIONS_1 = [(-470, 30), (-470, 10), (-470, -10), (-470, -30), (-470, -50)]
STARTING_POSITIONS_2 = [(470, 30), (470, 10), (470, -10), (470, -30), (470, -50)]
UP = 90
DOWN = 270
MOVE_DISTANCE = 10


class Paddle:

    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]

    def create_paddle(self):
        if not self.segments:
            for position in STARTING_POSITIONS_1:
                self.add_segment(position)
        else:
            for position in STARTING_POSITIONS_2:
                self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        pass
