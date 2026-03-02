from turtle import Screen
from snake import Snake
from food import Food
from manager import Manager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# tracer(N, Nms)
# N번째 드로잉 마다 화면 렌더링
# 드로잉 간 간격 N millisecond
# 0 = 수동 렌더링
screen.tracer(0)

snake = Snake()
food = Food()
manager = Manager()
manager.initialize(snake,food)
screen.listen()


# 입력 매핑
screen.onkey(lambda: snake.turn_head('w'), "w")
screen.onkey(lambda: snake.turn_head('s'), "s")
screen.onkey(lambda: snake.turn_head('d'), "d")
screen.onkey(lambda: snake.turn_head('a'), "a")

while manager.is_game_on:
    # tracer(0)과 합쳐서 모든 뱀이 이동하고 그리기. 반복문(이동) 시퀀스가 끝나고 업데이트
    # 후 0.1초 쉬고 다시 이동
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    manager.detect_collision()


#TODO-1 : 먹이 먹을 때마다 이상한 곳에 잠깐 표시되는 몸통 처리
    #렌더링-대기-이동 사이클 조정으로 해결
#TODO-2 : refresh() 20 단위로
    # randint(-280,280) -> randint(-14,14) * 20
#TODO-3 : 충돌 로직 main.py에서 분리 -> Manager 관리

#TODO-4 : 꼬리 충돌 로직 수정 -> 머리와 몸통이 딱 붙어서 수평한 경우
    # 20크기:1그리드 단위로 이동하기 때문에 distance() < 10 이면 딱 붙는 정도로는 충돌 X

screen.exitonclick()