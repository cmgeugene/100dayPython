import tkinter

window = tkinter.Tk()
# 제목
window.title("GUI Program")

# 창 크기
window.minsize(500, 300)
# 내부 패딩
window.config(padx=20, pady=20)

# 컴포넌트 만들기
# pack() 을 해야 윈도우에 나타남
text_label = tkinter.Label(text="텍스트 라벨", font=("Arial",15,"bold"))
text_label.grid(row=0, column=0)

# 버튼 만들기

def button_clicked():
    text_label["text"] = entry.get()

button1 = tkinter.Button(text="click me", command=button_clicked)
button1.grid(row=0, column=2)

button2 = tkinter.Button(text="click me", command=button_clicked)
button2.grid(row=1, column=1)

# Entry 컴포넌트 (입력 프롬프트)

entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)

window.mainloop()