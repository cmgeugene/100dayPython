from turtle import Turtle

class State(Turtle):
    def __init__(self,name:str,pos:tuple[int,int]):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(6)
        self.goto(pos[0],pos[1])
        self.write(name,align="center")
