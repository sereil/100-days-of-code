from tkinter import *

window = Tk()
window.title("Mile to Km Converter")


def btn_convert():
    miles = float(input.get())
    km = miles * 1.609344
    lbl_milestokm.config(text=f"{km}")

input = Entry()

input.grid(column=1, row=0)

lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2,row=0)

lbl_km = Label(text="Km")
lbl_km.grid(column=4,row=1)

lbl_equalto = Label(text="is equal to")
lbl_equalto.grid(column=0,row=1)

lbl_milestokm = Label(text="0")
lbl_milestokm.grid(column=1,row=1)

btn_calc = Button(text="Calculate", command=btn_convert)
btn_calc.grid(column=1,row=2)

window.mainloop()

# from tkinter import *


# def button_clicked():
#     print("I got clicked!")
#     print(type(input.get())) #Returns a string even if input is empty
#     inputtext = input.get() if input.get() != "" else "Button got clicked"
#     my_label.config(text=inputtext)

# window = Tk()
# window.title("My First Python GUI")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)


# #Label
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.grid(column=0,row=0)

# my_label["text"] = "new text"
# my_label.config(text="New Text") 


# button = Button()
# button.config(text="Click me!")
# button.grid(column=1,row=1)
# button["command"] = button_clicked

# new_button = Button(text="New Button")
# new_button.grid(column=2,row=0)

# input = Entry(width="10")
# input.grid(column=3,row=2)



# window.mainloop()