from tkinter import *
import pandas
import random

FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 40, "bold")

BACKGROUND_COLOR = "#B1DDC6"
current_card_id = None


def knows_word():
    global current_card_id
    new_dict = data_dict["English"].pop(current_card_id)
    new_dict = data_dict["French"].pop(current_card_id)
    dict_df = pandas.DataFrame(new_dict)
    dict_df.to_csv("..\\100-days-of-code\Day 31\data\\words_to_learn.csv")
    new_card()
    

def new_card():
    global current_card_id
    current_card_id = random.randint(0,100)
    card_french = (data_dict['French'].get(current_card_id)).title()
    canvas_card.itemconfig(card_word, text=f"{card_french}")
    canvas_card.itemconfig(canvas_img, image=card_front_img)
    window.after(3000,func=change_to_english)

def change_to_english():
    global current_card_id
    card_english = (data_dict['English'].get(current_card_id)).title()
    canvas_card.itemconfig(card_word, text=f"{card_english}")
    canvas_card.itemconfig(canvas_img, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50, pady=50, height=626, width=900)


Data = pandas.read_csv("..\\100-days-of-code\Day 31\data\\french_words.csv")

data_dict = pandas.DataFrame(Data).to_dict()

print(data_dict)


card_front_img  = PhotoImage(file="..\\100-days-of-code\Day 31\images\card_front.png")
card_back_img   = PhotoImage(file="..\\100-days-of-code\Day 31\images\card_back.png")
checkmark_img   = PhotoImage(file="..\\100-days-of-code\Day 31\images\\right.png")
cross_img       = PhotoImage(file="..\\100-days-of-code\Day 31\images\wrong.png")

canvas_card = Canvas(width=800, height=526, border=0, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas_card.create_image(400,263,image=card_front_img)

canvas_card.grid(row=0, column=0, columnspan=2)
card_lang = canvas_card.create_text(400,150, text="Language", font=FONT_LANG)
card_word =canvas_card.create_text(400,263, font=FONT_WORD)
new_card()

checkmark_btn = Button(image=checkmark_img, border=0, highlightthickness=0,command=knows_word)
checkmark_btn.grid(row=1,column=1)
cross_btn = Button(image=cross_img, border=0, highlightthickness=0,command=new_card)
cross_btn.grid(row=1,column=0)



window.mainloop()