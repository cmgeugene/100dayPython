from turtle import Screen, Turtle
from snake import Snake
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
screen.listen()

# 입력 매핑
screen.onkey(lambda: snake.turn_head('w'), "w")
screen.onkey(lambda: snake.turn_head('s'), "s")
screen.onkey(lambda: snake.turn_head('d'), "d")
screen.onkey(lambda: snake.turn_head('a'), "a")

game_is_on = True
while game_is_on:
    # tracer(0)과 합쳐서 모든 뱀이 이동하고 그리기. 반복문(이동) 시퀀스가 끝나고 업데이트
    # 후 0.5초 쉬고 다시 이동
    screen.update()
    time.sleep(0.1)
    snake.move_forward()



screen.exitonclick()