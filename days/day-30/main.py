# 다양한 에러들

"""with open("a.text") as data:
    data.read()
"""
# FileNotFoundError: [Errno 2] No such file or directory: 'a.text'


"""a_dict = {
    "key":"value"
}
value = a_dict["keeey"]"""
# KeyError: 'keeey'


"""my_list = [1, 2, 5, 7]
value = my_list[7]"""
# IndexError: list index out of range

"""text = "abc"
print(text+7)"""
# TypeError: can only concatenate str (not "int") to str


# 에러 핸들링
# try
# except
# else
# finally

"""try:
    with open("a.txt", mode="r") as file:
        file.read()
except:
    print("created target file")
    with open("a.txt", mode="w") as file:
        file.write("abc")"""

# except 블록은 구체적으로 지정하는 것이 좋다. 또한 여러 개를 지정할 수있다.

try:
    file = open("a.txt", mode="r")
    my_dict = {"key":3335}
    #print(my_dict["errorkey"])
except FileNotFoundError:
    print("created target file")
    with open("a.txt", mode="w") as file:
        file.write("abc")
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
    print(content)
    file.close()
finally:
    # 커스텀 에러 : raise
    raise TypeError("my custom error~")


