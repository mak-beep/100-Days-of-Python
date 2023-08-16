from tkinter import *
from tkinter import messagebox
import random

# To copy something automatically i.e., password
import pyperclip

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','~']

password_list = []
password = ''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_Password():
    global password
    global password_list
    password_field.delete(0,END)
    password_list = []
    for i in range(0,random.randint(3,7)):
        random_letter = random.choice(letters)
        password_list.append(random_letter)
    for i in range(0,random.randint(3,7)):
        random_number = random.choice(numbers)
        password_list += random_number
    for i in range(0,random.randint(3,7)):
        random_symbol = random.choice(symbols)
        password_list += random_symbol

    random.shuffle(password_list)
    password = "".join(password_list)
    password_field.insert(0,password)
    # Automatically copies the 'password'
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_List():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()
    if (website == "" or email == "" or password == ""):
        messagebox.askretrycancel(title = "Error", message = "You left one or more fields empty.")
    
    # Pop Up message
    else:
        confirmation = messagebox.askokcancel(title = f"{website}", message = f"These are the details entered:\nEmail: {email}\n"
                                          f"Password: {password}\n Is it ok to save?")
        if (confirmation):
            with open("Day 29 - Password Generator App/password.txt", mode = 'a') as txt_file:
                txt_file.write(f"{website} | {email} | {password}\n")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width = 500, height = 500)
window.title("Password Generator")
window.config(padx = 20, pady = 20)


# Logo
canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "Day 29 - Password Generator App/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row = 0, column = 1)

# Labels

website_label = Label(text = "Website")
website_label.grid(row = 1, column = 0, padx = 20)

email_label = Label(text = "Username/Email")
email_label.grid(row = 2, column = 0, padx = 20)

password_label = Label(text = "Password")
password_label.grid(row = 3, column = 0)

#  Text Fields

website_field = Entry(width = 50)
website_field.focus()
website_field.grid(row = 1, column = 1, columnspan= 2, pady= 2)

email_field = Entry(width = 50)
email_field.grid(row = 2, column = 1, columnspan= 2, pady= 2)

password_field = Entry(width = 25)
password_field.grid(row = 3, column = 1, sticky = W, padx = 5, pady= 2)

# Buttons

password_generator = Button(text="Generate Password", command = generate_Password)
password_generator.grid(column = 2, row = 3, sticky = W, pady= 2)

add_button = Button(text="Add", width = 40, command = add_to_List)
add_button.grid(row = 4, column = 1, columnspan= 2, pady= 2)





window.mainloop()