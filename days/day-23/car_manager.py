from turtle import Turtle
from car import Car
from random import randint

MAX_CAR_LIMIT = 30

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars = []

    def deploy_cars(self):
        can_spawn = randint(1,6) == 6
        if can_spawn:
            if len(self.cars) != MAX_CAR_LIMIT:
                new_car = Car()
                new_car.is_on_lane = True
                new_car.goto(300,randint(-12,12)*20)
                self.cars.append(new_car)
            else:
                for car in self.cars:
                    if not car.is_on_lane:
                        car.is_on_lane = True
                        break

    def move_cars(self):
        if len(self.cars) != 0:
            for car in self.cars:
                car.accelerate()
                if car.xcor() < -300:
                    car.is_on_lane = False
                    car.goto(300, randint(-12, 12) * 20)

    def gear_up_cars(self):
        for car in self.cars:
            car.level_up()



