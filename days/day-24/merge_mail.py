# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# readlines() : 파일의 모든 줄을 리스트로 반환, 인자로 전달하는 정수는 줄이 몇 바이트인지 검사.
# string.replace() : 단어 바꾸는 함수. count를 통해 앞에서 부터 변환할 단어의 수를 결정
# string.strip() : 빈칸, 혹은 문자열을 제거하는 함수. 인자 전달이 없으면 space 제거(개행문자, 탭 문자 같은 \n, \t 등 제거), 인자로 문자열을 전달하면
# 해당 문자열의 char들을 모두 제거
# 예시 :
# txt = ",,,,,rrttgg.....banana....rrr"
#
# x = txt.strip(",.grt")
#
# print(x)
# banana

template_path = "Input/Letters/starting_letter.txt"
names_path = "Input/Names/invited_names.txt"
output_path = "Output/ReadyToSend/"

with open(names_path) as name_data:
    names = name_data.readlines()
names=[name.strip() for name in names]

with open(template_path) as template_data:
    letter_string = template_data.readlines()

for name in names:
    with open(f"{output_path}MailTo{name}", mode="w") as new_letter:
        _letter = letter_string.copy()
        _letter[0] = _letter[0].replace("[name]",name.strip())
        new_letter.writelines(_letter)

