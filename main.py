# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter= [random.choice(letters) for _ in range(nr_letters)]
    password_symbol=[random.choice(symbols) for _ in range (nr_symbols)]
    password_number=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letter+password_symbol+password_number


    random.shuffle(password_list)


    password = "".join(password_list)
    password_Entry.insert(0,password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_command():

    web=Website_Entry.get()
    email=Email_Entry.get()
    password=password_Entry.get()
    new_data= {
        web:{
            "email": str(email),
            "password": str(password),

        }
    }

    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="Please don't leave any fields empty")
    else :

        is_ok=messagebox.askokcancel(title=f"{web}",message=f"these are the details you've entered : \nEmail:{email}\nPasseword:{password}\nis it ok to save it ?")
        if is_ok:

            try:

                with open ("Password.json","r") as record:
                    data2= json.load(record)


            except FileNotFoundError:

                with open ("Password.json","w") as record :
                    json.dump(new_data,record,indent=4)

            else :
                data2.update(new_data)
                with open("Password.json","w") as record:
                    json.dump(data2,record,indent=4)
            finally :

                    Website_Entry.delete(0,END)
                    Email_Entry.delete(0,END)
                    password_Entry.delete(0,END)
#---------------------------------search command ------------------------#

def search_command():
    web = Website_Entry.get()
    try :
        with open ("Password.json","r") as record:
            elements=json.load(record)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found")
    else:

        if web in elements:
            email=elements[web]["email"]
            password=elements[web]["password"]
            messagebox.showinfo(title=f"{web}",message=f" email= {email} , password={password}")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
password_logo=PhotoImage(file="logo.png")

canvas.create_image( 100,100,image=password_logo)
canvas.grid(row=0,column=1)

# canvas.create_text(50,200,text="Website",fill="black",font=("Courier","12","bold"))
# canvas.grid(row=1,column=0)

website=Label(text="Website")
website.grid(row=1,column=0)

Website_Entry=Entry(width=35)
Website_Entry.grid(row=1,column=1,columnspan=2)
Website_Entry.focus()
# canvas.create_text(80,240,text="Email/Username:",fill="black",font=("Courier","12","bold"))
# canvas.grid(row=2,column=0)

Email=Label(text="Email/UserName")
Email.grid(row=2,column=0)

Email_Entry=Entry(width=35)
Email_Entry.grid(row=2,column=1,columnspan=2)
Email_Entry.insert(0,"@gmail.com")

# canvas.create_text(50,280,text="Password:",fill="black",font=("Courier","12","bold"))
# canvas.grid(row=3,column=0)

password=Label(text="Password")
password.grid(row=3,column=0)

password_Entry=Entry(width=21)
password_Entry.grid(row=3,column=1)



generate_password=Button(text="Generate password",command=generate_password)
generate_password.grid(row=3,column=2)


Add_button=Button(text="Add",command=save_command)
Add_button.grid(row=4,column=1,columnspan=2)

Search_Button=Button(text="search",command=search_command)
Search_Button.grid(row=1,column=3,columnspan=2)

window.mainloop()