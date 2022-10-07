from tkinter import *
import requests

KANYE_API = "https://api.kanye.rest"
def get_quote():
    response = requests.get(url=KANYE_API)
    data = response.json()
    response.raise_for_status()    
    quote = data["quote"]    
    canvas.itemconfig(quote_text, text=quote)
    quote_text
    
    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="..\\100-days-of-code\Day 33\\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

get_quote()

kanye_img = PhotoImage(file="..\\100-days-of-code\Day 33\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()