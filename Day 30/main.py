from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    #Password Generator Project
    password_ntry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    
    random.shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    password_ntry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    #Insert Functionality to see if password has already been added - Can reuse and modify Search_cred
    website = website_ntry.get()
    user = user_ntry.get()
    password = password_ntry.get()
    new_data = {website: {
        "email":user,
        "password":password         
    }}
    
    if len(password) == 0 or len(user) ==0 or len(website) == 0:
        messagebox.showwarning(title="Caution", message="Everything is mandatory, just fill it up ok?")
    else:
        oktosave = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Username:{user} \nPassword: {password} \n IS it ok to save?")
        if oktosave:
            with open(file=".\\100-days-of-code\Day 30\data.json", mode="w") as file:                
                json.dump(new_data, file,indent=4)  

            messagebox.showinfo(title="", message="Credentials successfully saved")
            website_ntry.delete(0,END)
            #user_ntry.delete(0,END)
            password_ntry.delete(0,END)
# ----------------------- SEARCH CREDENTIALS -------------------------- #
def search_cred():
    #Insert Try FileNotFoundError Except Clause
    with open(file=".\\100-days-of-code\Day 30\data.json", mode="r") as file:
        data = json.load(file)
        website = website_ntry.get()
        if  website in data:
            user_ntry.delete(0,END)
            password_ntry.delete(0,END)
            user_ntry.insert(0,f"{data[website]['email']}")
            password_ntry.insert(0,f"{data[website]['password']}")            
        else:
            messagebox.showinfo(title="Search", message="The website you've search has not been found.")       
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=50)

logo_pi = PhotoImage(file=".\\100-days-of-code\Day 30\logo.png")

logo_img = Canvas()
logo_img.config(height=200, width=200)
logo_img.create_image(100,100,image=logo_pi)
logo_img.grid(column=1,row=0)

#Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0,row=1)
user_lbl = Label(text="Email/Username:")
user_lbl.grid(column=0,row=2)
password_lbl = Label(text="Password:")
password_lbl.grid(column=0,row=3)

#Entries
website_ntry = Entry(width=31)
website_ntry.grid(column=1, row=1, columnspan=1)
website_ntry.focus()
user_ntry =Entry(width=50)
user_ntry.grid(column=1, row=2, columnspan=2)
user_ntry.insert(0,"default-email@gmail.com")
password_ntry =Entry(width=31)
password_ntry.grid(column=1, row=3)

#Buttons
generate_pwd_btn = Button(text="Generate Password", command=generate_pwd)
generate_pwd_btn.grid(column=2,row=3)
search_btn = Button(text = "Search", width=15, command=search_cred)
search_btn.grid(column=2, row=1)
add_btn = Button(text="Add", width=42, command=save_pwd)
add_btn.grid(column=1,row=4, columnspan=2)



window.mainloop()