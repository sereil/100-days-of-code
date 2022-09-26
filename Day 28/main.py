
from ctypes.wintypes import SHORT
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BTN_WIDTH = 10
reps = 0
timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    global marks
    reps = 0
    marks = ""
    timer_lbl.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_lbl.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60        
    
    
    if reps == 8:
        countdown_timer(long_break_sec)
        timer_lbl.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(short_break_sec)
        timer_lbl.config(text="Break", fg=PINK)
    else:
        countdown_timer(work_sec)
        timer_lbl.config(text="Work", fg=GREEN)
    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_timer(count):
    global timer
    global reps
    global marks
    count_min = math.floor(count / 60)
    count_sec = count % 60    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1, countdown_timer, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"                    
            checkmark_lbl.config(text=marks)
           

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file="..\\100-days-of-code\Day 28\\tomato.png")
canvas.create_image(102,112, image=tomato_img)
canvas.grid(column=1,row=1)
timer_text = canvas.create_text(102,130, text="00:00",fill="white", font=(FONT_NAME, 20,"bold"))


timer_lbl = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME,30,"bold"))
timer_lbl.grid(column=1,row=0)
checkmark_lbl = Label(text="",fg=GREEN, bg=YELLOW, font=(FONT_NAME,30))
checkmark_lbl.grid(column=1,row=3)

start_btn = Button(text="Start",width=BTN_WIDTH, command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset", width=BTN_WIDTH, command=reset_timer)
reset_btn.grid(column=2,row=2)


window.mainloop()