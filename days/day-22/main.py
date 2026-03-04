from turtle import Screen
import paddle
from ball import Ball
import time
from manager import Manager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Day-22 Pong")
screen.tracer()
user = paddle.Paddle((350,0))
comp = paddle.Paddle((-350,0))

screen.listen()

# **반복문으로 매핑하기**
#
# controls = {
#     "Up" : (user, "up"),
#     "Down" : (user, "down"),
#     "w" : (comp, "up"),
#     "s" : (comp, "down")
# }
# for key, value in controls.items():
#     screen.onkey(lambda:value[0].move(value[1]),key)
#
# 위 처럼 작성하게 되면 어떤 키를 누르든지 마지막 루프인 "s"에 해당하는 동작만 실행하게 된다.
# 이유 :
# - 반복문을 통해 람다 함수 객체 4개가 생성된다. 람다 함수들은 변수명 value를 참조하고 있다
# - 반복문은 main.py 모듈에 전역으로 선언되었으므로 key, value는 반복이 끝난 뒤에도 전역 심볼 테이블에 남아있다
# - 문제는 key, value가 마지막 값(key="s", value=(comp,"down"))을 유지한 채로 남아있다는 것이다
# - 즉 어떤 람다를 실행하든 "s"와 (comp, "down")을 참조하게 되는 문제가 발생하게 되는 것
#
# 이를 해결하기 위해 람다를 선언할 때 기본값을 지정해주어야 한다
# for key, value in controls.items():
#     # p와 d라는 로컬 변수에 현재 루프의 value[0], value[1]을 기본값으로 할당
#     screen.onkey(lambda p=value[0], d=value[1]: p.move(d), key)
# 생성되는 람다 함수 객체의 지역 변수에 반복 당시의 value[0]과 value[1]이 할당되기 때문에
# 람다 함수가 실행될 때 전역 심볼 테이블에서 value를 찾는 대신 내부의 value를 참조할 수 있어
# 의도한 대로 동작하게 된다.

controls = {
    "Up" : (user, "up"),
    "Down" : (user, "down"),
    "w" : (comp, "up"),
    "s" : (comp, "down")
}

for key, value in controls.items():
    screen.onkeypress(lambda target_obj=value[0], arg=value[1]:target_obj.move(arg),key)

manager= Manager()
ball = Ball(user,comp,manager)

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.movement()
    screen.update()


screen.exitonclick()