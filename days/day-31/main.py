BACKGROUND_COLOR = "#B1DDC6"
DATA_PATH = "./data/french_words.csv"
SAVED_DATA = "./data/words_to_learn.csv"

import tkinter, pandas
from random import choice

#--------------------------- DATA PROCESSING -------------------------------#
data = None
data_list:list[dict] = None
current_card:dict = None
timer = None

def load_data():
    global data, data_list
    try:
        previous_data = pandas.read_csv(SAVED_DATA)
    except FileNotFoundError:
        original_data = pandas.read_csv(DATA_PATH)
        data_list = original_data.to_dict(orient="records")
    else:
        data_list = previous_data.to_dict(orient="records")
    finally:
        print(f"{len(data_list)} data loaded")

def save_data():
    global data, data_list
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv(SAVED_DATA,index=False)

def remove_card():
    data_list.remove(current_card)

def show_next_card():
    global current_card, timer

    window.after_cancel(timer)

    if len(data_list) == 0:
        canvas.itemconfig(card_text_title, text="Congratulations!", fill="black")
        canvas.itemconfig(card_text_word, text="You learned all words!", fill="black")
        return

    next_card = choice(data_list)
    current_card = next_card
    next_french = next_card["French"]
    next_english = next_card["English"]
    canvas.itemconfig(card_img,image=card_front_img)
    canvas.itemconfig(card_text_title,text="French",fill="black")
    canvas.itemconfig(card_text_word,text=next_french,fill="black")

    timer = window.after(3000,flip_card)

def right_marking():
    global timer
    if timer:
        window.after_cancel(timer)

    remove_card()
    save_data()

    show_next_card()

def wrong_marking():
    global timer
    if timer:
        window.after_cancel(timer)
    show_next_card()

def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_text_title, text="English",fill="white")
    canvas.itemconfig(card_text_word, text=current_card["English"],fill="white")

#--------------------------- UI -------------------------------#
window = tkinter.Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
#--------------------------- Card(Canvas) -------------------------------#
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")

canvas = tkinter.Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = canvas.create_image(400,263,image=card_front_img)
card_text_title = canvas.create_text(400,150,text="title",font=("Arial",40,"italic"),fill="black")
card_text_word = canvas.create_text(400,283,text="word",font=("Arial",60,"bold"),fill="black")
canvas.grid(row=0, column=0,columnspan=2)

#--------------------------- Buttons -------------------------------#
btn_right_img = tkinter.PhotoImage(file="./images/right.png")
btn_wrong_img = tkinter.PhotoImage(file="./images/wrong.png")

# 버튼 자체의 테두리도 지우려면 bd=0
right_btn = tkinter.Button(image=btn_right_img,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,bd=0,activebackground=BACKGROUND_COLOR, command=right_marking)
wrong_btn = tkinter.Button(image=btn_wrong_img,highlightthickness=0,highlightcolor=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,bd=0,activebackground=BACKGROUND_COLOR, command=wrong_marking)
right_btn.grid(row=1, column=1)
wrong_btn.grid(row=1, column=0)

load_data()
show_next_card()

window.mainloop()