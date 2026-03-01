from turtle import Turtle

DIRECTIONS = {
    "d" : 0,
    "w" : 90,
    "a" : 180,
    "s" : 270
}

class Snake:
    def __init__(self):
        self.bodies = []
        self.new_snake()
        self.head = self.bodies[0]

    def add_body(self):
        current_length = len(self.bodies)
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.goto(self.bodies[current_length-1])
        self.bodies.append(new_turtle)

    def new_snake(self):
        for i in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            pos = new_turtle.pos()
            new_turtle.penup()
            new_turtle.teleport(x=pos[0] - (i * 20))
            self.bodies.append(new_turtle)

    def move_forward(self):
        for i in range(len(self.bodies)-1, -1, -1):
            if i > 0:
                next_pos = self.bodies[i-1].pos()
                self.bodies[i].goto(next_pos)
            elif i == 0:
                self.bodies[i].forward(20)

    def turn_head(self, direction:str):
        new_heading = DIRECTIONS[direction]
        if abs(self.head.heading() - DIRECTIONS[direction]) != 180:
            if direction == "w":
                self.head.setheading(new_heading)
            elif direction == "s":
                self.head.setheading(new_heading)
            elif direction == "a":
                self.head.setheading(new_heading)
            elif direction == "d":
                self.head.setheading(new_heading)