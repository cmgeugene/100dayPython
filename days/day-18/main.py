# /// script
# dependencies = [
#     "colorgram-py"
# ]
# ///
from turtle import Turtle, Screen, colormode
from random import randint, choice
import colorgram

extract_colors = colorgram.extract('hirst-painting.jpg', 20)
print(extract_colors[0].rgb) #returns namedtuple : Rgb(r=226, g=225, b=222)

# colorgram.extract 는 Color 클래스 오브젝트의 리스트를 반환
# 컬러클래스 rgb 속성을 통해 rgb 네임드튜플에 접근할 수 있음
# 리스트 컴프리헨션으로 바로 추출
hirst_colors=[(i.rgb.r,i.rgb.g,i.rgb.b) for i in extract_colors]
filtered_colors = [color for color in hirst_colors if sum(color)/len(color) <= 220]

timmy = Turtle()
timmy.shape("turtle")

def draw_line():
    # 길이 200 점선 그리기
    for _ in range(10):
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)
        timmy.down()

def get_random_rgb():
    # turtle.pencolor는 rgb로 전달하려면 튜플 형식이 필요
    random_rgb = (randint(1,255),randint(1,255),randint(1,255))
    return random_rgb

def draw_shapes(start:int, end:int):
    # start각형부터 end각형까지 겹쳐 그리기
    for i in range(start, end+1):
        angle = 360 / i
        count = i
        timmy.pencolor(get_random_rgb())
        for _ in range(i):
            timmy.forward(100)
            timmy.right(angle)

def random_walk(turtle:Turtle,steps:int):
    turtle.pensize(10)
    turtle.speed(10)
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.pencolor(get_random_rgb())
        turtle.setheading(choice(directions))
        turtle.forward(30)

def draw_spirograph(turtle:Turtle,radius:int,gap:int):
    turtle.speed(0)
    for _ in range(int(360/gap)):
        turtle.pencolor(get_random_rgb())
        turtle.circle(radius)
        turtle.left(gap)


def draw_hirst(turtle:Turtle, width:int, height:int, gap:int):
    turtle.hideturtle()
    turtle.teleport(x=-(width*gap/2),y=-(height*gap/2))
    for h in range(height):
        home = turtle.pos()
        for w in range(width):
            turtle.dot(20,choice(filtered_colors))
            turtle.teleport(x=turtle.pos()[0]+gap)
        turtle.teleport(x=home[0], y=home[1]+gap) #vec2d = 튜플 상속




colormode(255) #1~255 까지 쓰려면 컬러모드 지정 필요

draw_hirst(timmy,10,10,50)

screen = Screen()
screen.exitonclick()