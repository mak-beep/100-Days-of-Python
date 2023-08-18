from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Search within file

def search():
    data_index = {}
    website = website_entry.get()
    with open("Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/Password-Manager-End-of-Day-29/data.json", "r") as data_file:
        try:
            data = json.load(data_file)
            data_index = data[website]
        except KeyError:
            messagebox.showinfo(title="Error", message="No Info Found for this Website")
            
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            messagebox.showinfo(title=f"{website}", message=f"Email : {data_index['Email']}\nPassword : {data_index['Password']}")


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:

            try:
                with open("Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/Password-Manager-End-of-Day-29/data.json", "r") as data_file:
                    
                    ### TO create new data

                    # json.dump(new_data, data_file, indent= 4)

                    ### To update existing data
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/Password-Manager-End-of-Day-29/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent= 4)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/Password-Manager-End-of-Day-29/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent= 4)

            finally:
                    website_entry.delete(0, END)
                    email_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/Password-Manager-End-of-Day-29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row = 1, column = 1, sticky = W, padx = 5, pady= 2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2, sticky = W, padx = 5)
password_entry = Entry(width=30)
password_entry.grid(row = 3, column = 1, sticky = W, padx = 5, pady= 2)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column = 2, row = 3, sticky = W, pady= 2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row = 4, column = 1, columnspan= 2, pady= 2)
search_button = Button(text="Search", command=search, width= 13)
search_button.grid(row = 1, column=2, sticky = W, pady= 2)
window.mainloop()