from tkinter import *
from tkinter import messagebox
from turtle import update


from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT= ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:        
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)    
        
        
        self.lbl_score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", padx=10, pady=5,font=FONT)
        self.lbl_score.grid(row=0,column=1)
        
        
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        
        
        
        true_image = PhotoImage("..\\100-days-of-code\Day 34\images\\true.png") #Can't be found for some reason.
        self.btn_true = Button(text="True", highlightthickness=0,width=10,height=10,command = self.press_true)
        self.btn_true.grid(row=2,column=0)
        
        false_image = PhotoImage("..\\100-days-of-code\Day 34\images\\false.png")
        self.btn_false = Button(text="False",highlightthickness=0, width=10,height=10,command=self.press_false)
        self.btn_false.grid(row=2,column=1)
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():            
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            messagebox.showinfo(title="You've completed the quiz!", message=f"Your final score was: {self.quiz.score}/10")
            self.btn_false.config(state="disabled")
            self.btn_true.config(state="disabled")
        
    def press_true(self):
        response = self.quiz.check_answer("False")
        self.give_feedback(response)    
        

    
    def press_false(self):
        response = self.quiz.check_answer("False")
        self.give_feedback(response)    
        
        
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.update_score()
        else:
            self.canvas.config(bg="red")            
        self.window.after(1000,func=self.get_next_question)
            
    def update_score(self):
        self.lbl_score.config(text=f"Score: {self.quiz.score}")