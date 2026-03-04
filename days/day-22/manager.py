from turtle import Turtle

class Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.comp_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(0,250)
        self.update_score()


    def add_score(self, target:str):
        if target == "user":
            self.user_score += 1
        else:
            self.comp_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.comp_score}  vs  {self.user_score}", align="center", font=("Courier", 25, "normal"))