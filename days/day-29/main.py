import tkinter
from tkinter import messagebox
from password import generate_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    if len(password_etr.get()) != 0:
        password_etr.delete(0, "end")
    password = generate_password()
    password_etr.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    input_website = website_etr.get()
    input_username = username_etr.get()
    input_password = password_etr.get()
    combined = f"{input_website} | {input_username} | {input_password}\n"

    if len(input_password) == 0 or len(input_username) == 0 or len(input_website) == 0:
        messagebox.showwarning(title="Verify your input", message="Please don't leave any fields empty!")
        return

    is_correct = messagebox.askyesno(title="Verify your input", icon="question", message=f"Website : {input_website}\nEmail/Username : {input_username}\nPassword : {input_password}\n\nIs it Correct?")

    if is_correct:
        with open("data.txt", mode="a") as file:
            file.write(combined)

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
website_etr = tkinter.Entry(width=50,bg="gray99")
website_etr.grid(row=1,column=1,columnspan=2,sticky="W")
website_etr.focus()

username_lb = tkinter.Label(text="Email/Username :",font=("Arial",12),bg="white")
username_lb.grid(row=2,column=0,sticky="E")
username_etr = tkinter.Entry(width=50,bg="gray99")
username_etr.grid(row=2,column=1,columnspan=2,sticky="W")

password_lb = tkinter.Label(text="Password :", font=("Arial",12), bg="white")
password_lb.grid(row=3,column=0,sticky="E",pady=10)
password_etr = tkinter.Entry(width=27,bg="gray99")
password_etr.grid(row=3,column=1,sticky="W")
gen_pw_btn = tkinter.Button(text="Generate Password", font=("Arial",12), bg="gray99", command=get_password)
gen_pw_btn.grid(row=3,column=2,sticky="E")

add_btn = tkinter.Button(text="Add", font=("Arial",12), bg="gray99",width=38, command=save_password)
add_btn.grid(row=4,column=1,columnspan=2,sticky="W",pady=10)


window.mainloop()