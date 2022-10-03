from tkinter import *
import pandas
import random

FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 40, "bold")

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

def known_word():
    global current_card
    data_dict.remove(current_card)
    dict_df = pandas.DataFrame(data_dict)
    dict_df.to_csv("..\\100-days-of-code\Day 31\data\\words_to_learn.csv", index=False)
    new_card()
    

def new_card():
    global current_card, flip_timer    
    window.after_cancel(flip_timer)
    if(len(data_dict) == 0):
        print("No more cards to learn")
        exit
    current_card = random.choice(data_dict)
    word_french = current_card["French"].title()
    canvas_card.itemconfig(card_word, text=f"{word_french}")
    canvas_card.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000,func=change_to_english)

def change_to_english():
    global current_card
    canvas_card.itemconfig(card_word, text=f"{current_card['English'].title()}")
    canvas_card.itemconfig(canvas_img, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50, pady=50, height=626, width=900)
flip_timer = window.after(3000,func=change_to_english)
try:
    data = pandas.read_csv("..\\100-days-of-code\Day 31\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("..\\100-days-of-code\Day 31\data\\french_words.csv")
finally:
    data_dict = pandas.DataFrame(data).to_dict(orient="records") #Records prints it out as a list


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

checkmark_btn = Button(image=checkmark_img, border=0, highlightthickness=0,command=known_word)
checkmark_btn.grid(row=1,column=1)
cross_btn = Button(image=cross_img, border=0, highlightthickness=0,command=new_card)
cross_btn.grid(row=1,column=0)



window.mainloop()