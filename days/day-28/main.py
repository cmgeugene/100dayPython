import tkinter, math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
timer = None
remain = 0
last_state = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def cancel_timer():
    global reps, remain
    if timer:
        window.after_cancel(id=timer)
        canvas.itemconfig(timer_text, text="00:00")
        status_label.config(text="Waiting..")
        check_label.config(text="")
        start_button.config(text="Start", command=start_timer)
        reps = 0
        remain = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, mark, remain

    start_button.config(text="Stop", command=stop_timer)

    reps += 1

    # 체크 표시 추가 로직
    if reps % 2 == 0:
        mark = "✔" * (reps // 2)
        check_label.config(text=mark)

    if reps == 8:
        # 긴 휴식
        status_label.config(text="Take a LONG break")
        reps = 0

        remain = LONG_BREAK_MIN*60
        count_down(remain)

    elif reps % 2 == 1:
        # 집중 시간
        status_label.config(text="Running")

        remain = WORK_MIN*60
        count_down(remain)

    elif reps % 2 == 0:
        # 휴식 시간
        status_label.config(text="Take a short break")

        remain = SHORT_BREAK_MIN*60
        count_down(remain)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# mainloop() 안에서 지속 실행하기 위해서 재귀 호출 필요
def count_down(count):
    global reps, mark, timer, remain
    remain = count

    count_min = math.floor(count/60)
    count_min_text = str(count_min) if count_min > 9 else f"0{count_min}"
    count_sec = count % 60
    count_sec_text = str(count_sec) if count_sec > 9 else f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min_text}:{count_sec_text}")
    if remain > 0:
        remain -= 1
        timer = window.after(1000, count_down, remain)
    else:
        notify_user()
        start_timer()

# ---------------------------- STOP & RESUME MECHANISM ------------------------------- #
def stop_timer():
    global last_state, timer
    window.after_cancel(id=timer)
    timer = None
    last_state = status_label.cget("text")
    status_label.config(text="STOP")
    start_button.config(text="Resume", command=resume_timer)

def resume_timer():
    global remain
    start_button.config(text="Stop", command=stop_timer)
    status_label.config(text=last_state)
    count_down(remain)

# ---------------------------- USER NOTIFYING MECHANISM ------------------------------- #
def notify_user():
    # 맨 앞으로 고정 잠깐 활성화
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)
    # 최소화되어 있을 경우를 대비
    window.deiconify()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

timer_label = tkinter.Label(text="Pomodoro\nTimer",font=("Arial",45,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

status_label = tkinter.Label(text="Waiting..", font=("Arial",15),fg=PINK,bg=YELLOW)
status_label.grid(row=1,column=1)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(102,132, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(row=2,column=1)

start_button = tkinter.Button(text="Start",font=("Arial",15),bg="white",highlightthickness=0, command=start_timer)
start_button.grid(row=3,column=0)
reset_button = tkinter.Button(text="Reset",font=("Arial",15),bg="white",highlightthickness=0, command=cancel_timer)
reset_button.grid(row=3,column=2)

check_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=("Arial",20))
check_label.grid(row=4,column=1)

window.mainloop()