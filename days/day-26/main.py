import pandas

student_dict ={
    "student" : ["Angela", "James", "Lily"],
    "score" : [56 ,67, 78]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (key, value) in student_df.items():
    print(value)

# pandas 에서 반복문을 돌리면 컬럼을 순회함
# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: str
# 0    56
# 1    67
# 2    78
# Name: score, dtype: int64

#row-by-row 로 순회 방법 : iterrows()
for (index,row) in student_df.iterrows():
    print(row)

# 행을 출력(인덱스 기준 조회)
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         67
# Name: 1, dtype: object
# student    Lily
# score        78
# Name: 2, dtype: object

# 판다스 특) 멤버에 접근하듯 접근할 수 있음
for (index,row) in student_df.iterrows():
    print(row.student)
# Angela
# James
# Lily

for (index,row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
        # 56