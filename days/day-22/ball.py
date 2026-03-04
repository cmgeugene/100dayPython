from turtle import Turtle
from random import uniform
from paddle import Paddle
from manager import Manager

class Ball(Turtle):
    def __init__(self,user:Paddle,comp:Paddle,manager:Manager):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction:list[float] = [0.0, 0.0]
        self.movement_multiplier = 5
        self.user_paddle = user
        self.comp_paddle = comp
        self.manager = manager
        self.initialize()


    def initialize(self):
        self.teleport(0,0)
        self.direction = [uniform(0.5,1.0), uniform(0.5,1.0)]
        self.movement_multiplier = 5

    def movement(self):
        self.detect_wall()
        self.detect_goal()
        self.detect_paddle()
        self.move()

    def move(self):
        new_x = self.xcor() + (self.direction[0] * self.movement_multiplier)
        new_y = self.ycor() + (self.direction[1] * self.movement_multiplier)
        self.goto(new_x,new_y)

    def detect_wall(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.bounce("y")

    def bounce(self, direction:str):
        if direction == "y":
            self.direction[1] *= -1
        else:
            self.direction[0] *= -1
        self.movement_multiplier = min(self.movement_multiplier * 1.1, 10)

    def detect_paddle(self):
        if self.distance(self.user_paddle) < 50 and self.xcor() > 320:
            if self.direction[0] > 0:
                self.bounce("x")
        elif self.distance(self.comp_paddle) < 50 and self.xcor() < -320:
            if self.direction[0] < 0 :
                self.bounce("x")

    def detect_goal(self):
        if self.xcor() > 390 :
            self.manager.add_score("comp")
            self.initialize()
            self.direction[0] = abs(self.direction[0])
        elif self.xcor() < -390 :
            self.manager.add_score("user")
            self.initialize()
            self.direction[0] = -abs(self.direction[0])
