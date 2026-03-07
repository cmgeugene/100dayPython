from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.movement_speed = STARTING_MOVE_DISTANCE
        self.turtlesize(1,2)
        self.setheading(180)
        self.is_on_lane = False

    def accelerate(self):
        if self.is_on_lane:
            self.goto(self.xcor() - self.movement_speed, self.ycor())

    def level_up(self):
        self.movement_speed += MOVE_INCREMENT
