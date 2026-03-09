import pandas

df = pandas.read_csv("Squirrel_Data.csv")

# 새로운 데이터 테이블 만들기
# 다람쥐의 털 색상 별로 개체수 파악하기

# 털 색상 종류 파악하기 -> 이것만으로도 목적 달성이긴 함
data = df[["Primary Fur Color"]].value_counts()
print(data)

# value_counts() 는 series 객체를 반환
# 시리즈 객체는 딕셔너리의 특성과 리스트의 특성을 가지고 있다
# iloc[0] 으로 첫 번째 위치에 접근
# df["인덱스명"] 으로 해당 인덱스 값에 접근

# 각 색상별 컬럼 필터링 후 count()
# 방법 2가지
# 1.데이터프레임의 행x열 을 튜플로 반환하는 shape[0]
# 2.len() -> dataframe/series 객체 모두 __len__ 메서드가 있어서 행 갯수 확인 가능
num_gray = df[df["Primary Fur Color"] == "Gray"].shape[0]

num_cinnamon = df[df["Primary Fur Color"] == "Cinnamon"].shape[0]

num_black = len(df[df["Primary Fur Color"] == "Black"])


# 딕셔너리 생성
squirrels = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Counts" : [num_gray, num_cinnamon, num_black]
}

# 시리즈의 딕셔너리 특성으로 바로 접근 가능
# squirrels = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Counts" : [data["Gray"], data["Cinnamon"], data["Black"]]
# }

sq_df = pandas.DataFrame(squirrels)
sq_df.to_csv("squirrels_counts.csv")
print(sq_df)