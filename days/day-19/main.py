# /// script
#  dependencies = [
#      ""
#  ]
# ///
from turtle import Turtle, Screen
from random import randint
colors = ["red","blue","orange","yellow","green","purple","navy"]
turtles= []

def init_turtles():
    for c in colors:
        tt = Turtle(shape="turtle")
        tt.color(c)
        tt.penup()
        tt.goto(x=-230,y=(-120)+(30*colors.index(c)))
        turtles.append(tt)

def forward_rand():
    for turtle in turtles:
        turtle.forward(randint(1,10))

def check_finishline():
    global winner
    for turtle in turtles:
        if turtle.pos()[0] >= 230:
            winner = turtle.pencolor()
            return True
    return False

is_race_over = False
timmy = Turtle()
screen = Screen()
winner = ""
screen.setup(width=500,height=400)
user_input = screen.textinput(title="우승 거북이 선택",prompt="우승 예상되는 거북이의 색상 입력").lower()
init_turtles()
while not is_race_over:
    forward_rand()
    is_race_over = check_finishline()
if user_input == winner :
    print("you win")
else :
    print("you lose")

screen.exitonclick()