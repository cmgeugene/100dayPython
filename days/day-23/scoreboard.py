FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.teleport(-280, 250)
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",False,font=FONT)

    def show_gameover(self):
        self.teleport(0,0)
        self.write("GAME OVER",align="center",font=FONT)
