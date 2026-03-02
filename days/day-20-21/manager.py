from turtle import Turtle
from snake import Snake
from food import Food

class Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.show_score()
        self.food = None
        self.snake = None
        self.is_game_on = True

    def initialize(self,snake:Snake,food:Food):
        self.snake = snake
        self.food = food

    def show_score(self):
        self.write(arg=f"Score: {self.score}",align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_game_over(self):
        self.is_game_on = False
        self.penup()
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial", 24, "normal"))

    def detect_collision(self):
        if self.snake and self.food:
            self.detect_food()
            self.detect_tail()
            self.detect_wall()

    def detect_food(self):
        # 먹이 감지
        if self.snake.head.distance(self.food) < 15:
            self.snake.get_food()
            self.food.refresh()
            self.add_score()

    def detect_tail(self):
        # 꼬리 충돌 감지
        # 파이썬 특성상 슬라이싱으로는 빈 리스트를 반환하고 IndexError 발생하지 않음
        for body in self.snake.bodies[4:]:
            if self.snake.head.distance(body) < 10:
                self.show_game_over()

    def detect_wall(self):
        # 벽 충돌 감지
        if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
            self.show_game_over()