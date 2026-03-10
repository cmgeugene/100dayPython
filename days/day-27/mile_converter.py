import tkinter

from numpy.ma.extras import row_stack

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.maxsize(width=500, height=150)
window.config(padx=30, pady=25)

entry = tkinter.Entry(width=10)
entry.grid(row=0,column=1)
entry.insert(0,string="0")

miles_label = tkinter.Label(text=" Miles")
miles_label.grid(row=0,column=2)

equal_label = tkinter.Label(text=" is equal to")
equal_label.grid(row=1,column=0)

converted_label = tkinter.Label(text="0")
converted_label.grid(row=1, column=1)

km_label = tkinter.Label(text="km")
km_label.grid(row=1,column=2)

def convert():
    miles = int(entry.get())
    converted_label["text"] = round(miles * 1.609344,2)

calc_button = tkinter.Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)



window.mainloop()