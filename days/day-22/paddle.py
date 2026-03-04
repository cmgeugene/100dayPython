from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, initial_pos:tuple[int,int]):
        """초기 위치는 튜플로 전달"""
        super().__init__()
        self.shape("square")

        # 모든 turtle 사이즈는 20 * 20 이므로 width를 5배 늘림
        # width인 이유는 기본값인 거북이 머리가 오른쪽을 보고 있기 때문에 width를 늘려야 세로로 길어짐
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)

        self.color("white")
        self.penup()
        self.speed(5)
        # 언패킹 전달
        # * : 이터러블 언패킹 (리스트, 튜플, 세트 등)
        # ** : 딕셔너리 언패킹
        self.teleport(*initial_pos)
        if initial_pos == (350, 0):
            self.is_right_paddle = True
        else: self.is_right_paddle = False

    def move(self, direction:str):
        if direction == "up":
            if self.ycor() < 250:
                self.goto(self.xcor(), self.ycor() + 20)
        elif direction == "down":
            if self.ycor() > -250:
                self.goto(self.xcor(), self.ycor() - 20)