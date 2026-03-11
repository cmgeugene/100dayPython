import tkinter, json
from tkinter import messagebox
from password import generate_password
import pyperclip

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    target_website = website_etr.get().title()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="No Data", message="There is no Password data file.")
    else:
        # 데이터 파일 불러오기 성공
        try:
            # 키가 있음
            target_info = data[target_website]
        except KeyError:
            # 키가 없음
            messagebox.showwarning(title="Website not found", message=f"There is no {target_website} login data. Try another website.")
        else:
            target_email = target_info["email/username"]
            target_password = target_info["password"]
            messagebox.showinfo(title="Found result", message=f"Your {target_website} Login data:\n\nEmail/Username : {target_email}\nPassword : {target_password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    if len(password_etr.get()) != 0:
        password_etr.delete(0, "end")
    password = generate_password()
    password_etr.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    input_website = website_etr.get().title()
    input_username = username_etr.get()
    input_password = password_etr.get()
    new_data = {
        input_website : {
            "email/username" : input_username,
            "password" : input_password
        }
    }

    if len(input_password) == 0 or len(input_username) == 0 or len(input_website) == 0:
        messagebox.showwarning(title="Verify your input", message="Please don't leave any fields empty!")
        return

    is_correct = messagebox.askyesno(title="Verify your input", icon="question", message=f"Website : {input_website}\nEmail/Username : {input_username}\nPassword : {input_password}\n\nIs it Correct?")

    if is_correct:
        # 처음부터 w 모드로 열게 되면 기존 내용을 전부 삭제하게 된다.
        # 또한 json은 통째로 읽고 써야 한다. txt처럼 맨 뒤에 붙이는 게 불가능
        # 즉 json을 수정하려면 로드->딕셔너리로 바꾼 후 내용 추가 ->json으로 바꾸기 를 해야 한다.
        try:
            with open("data.json", mode="r") as file:
                # 쓰기 - json.dump : 파이썬 딕셔너리를 json으로 변환
                # 읽기 - json.load() : json 을 파이썬 딕셔너리로 변환
                # 수정 - dict.update() : load() -> update() -> dump() 단계
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # 파일이 없음 = 첫 요소이므로 바로 덤프하고 끝
                json.dump(new_data, file, indent=4)
        else:
            # 파일이 있음 = 새로운 요소가 아님 -> update 후 dump
            with open("data.json", mode="w") as file:
                data.update(new_data)
                json.dump(data, file, indent=4)
        finally:
            #clear entry
            website_etr.delete(0,"end")
            username_etr.delete(0,"end")
            password_etr.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=30,bg="white")
window.title("Password Manager")

canvas = tkinter.Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1, sticky="E")

website_lb = tkinter.Label(text="Website :",font=("Arial",12),bg="white")
website_lb.grid(row=1,column=0,sticky="E",pady=10)
website_etr = tkinter.Entry(width=27,bg="gray99")
website_etr.grid(row=1,column=1,sticky="W")
website_etr.focus()
search_btn = tkinter.Button(text="Search", font=("Arial",12), bg="gray99", width=16,command=find_password)
search_btn.grid(row=1,column=2,sticky="W")

username_lb = tkinter.Label(text="Email/Username :",font=("Arial",12),bg="white")
username_lb.grid(row=2,column=0,sticky="E")
username_etr = tkinter.Entry(width=50,bg="gray99")
username_etr.grid(row=2,column=1,columnspan=2,sticky="W")

password_lb = tkinter.Label(text="Password :", font=("Arial",12), bg="white")
password_lb.grid(row=3,column=0,sticky="E",pady=10)
password_etr = tkinter.Entry(width=27,bg="gray99")
password_etr.grid(row=3,column=1,sticky="W")
gen_pw_btn = tkinter.Button(text="Generate Password", font=("Arial",12), bg="gray99", command=get_password)
gen_pw_btn.grid(row=3,column=2,sticky="W")

add_btn = tkinter.Button(text="Add", font=("Arial",12), bg="gray99",width=38, command=save_password)
add_btn.grid(row=4,column=1,columnspan=2,sticky="W",pady=10)


window.mainloop()