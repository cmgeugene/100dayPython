# /// script
# dependencies = [
#     "pandas"
# ]
# ///

DATA_PATH = "weather_data.csv"

with open(DATA_PATH,mode="r") as weather_data:
    data = [data.strip() for data in weather_data]
print(data)

#  strip()으로 개행문자가 제거된 순수한 데이터를 가지고 올 수 있지만 행이 합쳐져있다.
# ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', 'Wednesday,15,Rain', 'Thursday,14,Cloudy', 'Friday,21,Sunny', 'Saturday,22,Sunny', 'Sunday,24,Sunny']

import csv

with open(DATA_PATH) as weather_data:
    data = csv.reader(weather_data)

    # csv 모듈의 reader()로 가져오게 되면 csv.reader 오브젝트가 생성. 이 객체는 iterable임
    # 따라서 반복문으로 순회 가능하고 이를 살펴보면:
    for row in data:
        print(row)
        # 헤더(컬럼)를 포함한 각 행이 리스트 안에 구분되어서 담겨 나온다
        # ['day', 'temp', 'condition']
        # ['Monday', '12', 'Sunny']
        # ['Tuesday', '14', 'Rain']
        # ...(생략)...

    # csv.reader 객체에서 원하는 컬럼만 가져오기
    temperature = []
    # 참고 : 말이 iterable이지, 시퀀스 오브젝트가 아니므로 공용 len() 불가. -> line_num 속성을 이용하면 행 개수를 가져올 수 있음
    # csv.reader 객체 안의 각 행은 리스트로 이루어져 있다.

    # 리스트이므로 row[{index}]로 직접 접근할 수 있으나, 지금은 빈 리스트를 반환하게 된다.
    # 원인 : 이터레이터가 소모되었기 때문
    # 이 위치는 weather_data 변수의 스코프 안에 있다.
    # 그런데 위에서 for row in data를 시도해서 weather_data의 이터레이터 포인터가 파일 끝까지 갔다.
    # 따라서 아래에서 다시 data == weather_data 의 이터레이터 순회를 시작해도 이미 끝에 있어서 빈 결과만 나옴.
    # 두 가지 방법으로 해결 가능 :
    # weather_data.seek(0) 으로 파일 객체의 이터레이터를 0번으로 초기화
    # 새로운 open으로 초기화
    # c++ 에선 반복문에서 항상 이터레이터를 초기화하기 때문에 for(auto it=v.begin(); ...) 이런 문제가 드물다.
    for row in data:
        temperature.append(row[1])
    print(temperature)

# 새로 가져와서 초기화 후 행만 가져오기
with open(DATA_PATH) as weather_data:
    data = csv.reader(weather_data)

    temperature:list[int] = []
    for row in data:
        # 첫 행은 헤더가 들어가있으므로 조건문으로 거르기
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)

# csv.DictReader 객체로 가져올 수도 있다. DictReader 객체는 각 행이 컬럼:값 으로 매핑된 딕셔너리로 이루어져있다
# (iterable일 뿐 리스트 아님)
with open(DATA_PATH) as weather_data:
    data_dict = csv.DictReader(weather_data)
    temp:list[int] = []
    for row_dict in data_dict:
        temp.append(int(row_dict["temp"]))
    print(temp)

# 내장 csv 모듈은 하나의 컬럼도 위처럼 여러 줄 코드를 짜야한다.
# pandas 라이브러리를 사용해 간편하게 작업 가능

import pandas

pd_data = pandas.read_csv(DATA_PATH)
print(type(pd_data))

# 전체 tabular 출력
print(pd_data)
# 특정 컬럼만 출력
print(pd_data['temp'])
print(pd_data.temp)

pd_dict = pd_data.to_dict()
print(pd_dict)
# 데이터프레임을 딕셔너리로 변환 결과를 볼 수 있음.
# 컬렴명이 키가 된다. 값은 딕셔너리이며, 내부 딕셔너리의 키가 인덱스.

# 각 컬럼(리스트)는 시리즈이므로 시리즈의 메소드인 to_list() 사용 가능
print(pd_data["temp"].to_list())

# 평균 온도 구하기
average_temp = pd_data["temp"].mean()
print(round(average_temp,1))

# 최고 온도 구하기
max_temp = pd_data["temp"].max()
print(max_temp)

# 컬럼에서 데이터 가져오기
# row[index] 처럼 직접 접근으로 가져올 수도 있고
# 컬럼명을 인자로 해도 가능
print(pd_data["condition"])
print(pd_data.condition)


# 행에서 데이터 가져오기
# day 컬럼이 Monday 인 행을 가져온다.
print(pd_data[pd_data["day"] == "Monday"])
print(pd_data[pd_data.day == "Monday"])

# temp 컬럼 값이 가장 높은 행 가져오기
print(pd_data[pd_data["temp"] == pd_data["temp"].max()])
print(pd_data[pd_data.temp == pd_data.temp.max()])



# condition 이 Monday 인 행에서 온도를 가져와 화씨로 변환하기

# 1.monday 인 행만 가져오기
monday_data = pd_data[pd_data["day"] == "Monday"]

# 2.행에서 temp 컬럼만 가져오기 -> 시리즈 객체임
monday_temp = monday_data["temp"]
print(type(monday_temp)) # <class 'pandas.Series'>

# 3. 시리즈 객체의 값에 접근하기 - 하나만 있다는 확신 하에
monday_temp_value = monday_data["temp"].item()
# 3-1. 시리즈 객체의 값에 접근하기 - iloc(인덱스 기반 직접 접근)
monday_temp_value = monday_data["temp"].iloc[0]

# 4. 화씨 변환식 적용
print(monday_temp_value * (9/5) +32)


# loc을 이용한 필터링으로 한 줄로도 가능
# dataframe.loc[행조건, 열조건]
monday_temp_value = pd_data.loc[pd_data["day"]=="Monday","temp"].item() * 9/5 + 32
print(monday_temp_value)



# 데이터프레임 직접 만들기
# 위에서 봤던 것처럼 딕셔너리 기반임
# 딕셔너리의 value는 꼭 딕셔너리일 필요는 없음 -> 리스트여도 DataFrame 변환 과정에서 알아서 인덱싱 해줌
source = {
    "students" : ["Amy" , "James", "Michael"],
    "score" : [50, 60, 80]
}

df = pandas.DataFrame(source)
print(df)
#   students  score
# 0      Amy     50
# 1    James     60
# 2  Michael     80

# 데이터프레임을 csv로 저장
df.to_csv("student.csv")