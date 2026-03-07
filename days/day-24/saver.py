# 기본적인 파일 시스템 입출력 예제

file = open("test_text.txt")
contents = file.read()
print(contents)
file.close()

#메모리 관리를 위해서 open() 과 close() 는 짝을 이루고 있어야 한다.


#with 키워드를 사용하면 파이썬의 컨텍스트 매니저가 작업을 끝내면
#자동으로 메모리에서 내린다. 위의 키워드 없이 사용하는 방식과 다르게 권장되는 방식
with open("test_text.txt") as with_file:
    contents = with_file.read()
    print(contents)

#write() 메소드를 이용하면 내용을 수정할 수 있지만 open() 옵션이 기본값인 읽기 전용이어서
#권한 문제로 불가. 따라서 편집 가능한 옵션인 "w"로 열면 편집이 가능함.
with open("test_text.txt",mode="w") as edit_file:
    edit_file.write("this method can edit source.")

#존재하지 않는 파일을 mode="w"로 열게 되면 해당 파일을 생성한다.
with open("save_data.txt", mode="w") as new_file:
    new_file.write("new file creation")

#사실 mode="w" 는 덮어쓰기 편집이다. 좀 더 일반적인 의미의 편집은 append를 뜻하는 mode="a"로 열어야함
#아래처럼 하면 뒷 내용에 추가
with open("test_text.txt", mode="a") as append_text:
    append_text.write("\nappend parameter test")

with open("../../README.md") as readme:
    print(readme.read())