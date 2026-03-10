
# *args 가변인수
def add(*args:int):
    return sum(args)
# 가변 인수 args는 튜플 <class 'tuple'>
# 따라서 인덱스 접근도 가능 args[1]
print(add(1,3))


def calculate(**kwargs):
    print(kwargs)

print(calculate(add=5,mul=3))
# **kwargs 키워드 가변인수
# kwargs 키워드 가변인수는 딕셔너리로 전달된다.
# {'add': 5, 'mul': 3}

# 클래스에서 kwargs 사용 예시
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(model="Ionic", make="Hyundai")
print(my_car.make) #Hyndai

# 다만 키 접근의 경우 인수가 존재하지 않으면 컴파일 에러가 발생함
# get()을 쓰면 이런 상황을 방지할 수 있다.

class Animal:
    def __init__(self, **kw):
        self.species = kw.get("species")
        self.legs = kw.get("legs")
        self.horns = kw.get("horns")

animal = Animal() # 아무것도 입력 안함
print(animal.species) # None 출력
