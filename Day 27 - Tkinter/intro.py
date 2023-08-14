from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
# Padding - empty space
window.config(padx=20,pady=20)


# Tkinter has three layout managers
# pack - strat from the extreme
# place - position (x=0,y=0)
# grid - divides the screen into sub sections

# Components #

### Label

label = Label(text = "I am a Label.", background="yellow", font=("Arial", 24, "bold"))
# To display it on screen - Pack start from top
# label.pack()
label.grid(column=0,row=0)
label.config(padx=20,pady=20)

# Updating Properties
label["text"] = "NEW LABEL"
# OR
label.config(text="NEW TEXT.")

### Button

def button_clicked():
    new_text = entry.get()
    label.config(text=new_text)


button = Button(text="Press" , command=button_clicked)
# button.pack()
button.grid(column=1, row=1 )


button2 = Button(text="Press - 2" , command=button_clicked)
# button.pack()
button2.grid(column=2,row=0)

### Entry
entry = Entry(width=10)
entry.insert(END, string="Data")
# entry.pack()
entry.grid(column=3,row=2)
print(entry.get())

# ### Text Block
# text = Text(height=5, width=10)
# # Puts cursor in the textbox
# text.focus()
# # Add some starting text to help with
# text.insert(END, "Multi-line Text Input")
# # Get text from line 1 to the END
# print(text.get("1.0", END))
# text.pack()


# ### Spinbox

# def spinbox_used():
#     print(spinbox.get())

# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# ### Scale

# def scale_used(value):
#     print(value)

# scale = Scale(from_=0, to=10, command=scale_used)
# scale.pack()


# ### CheckBox
# def checkbutton_used():
#     # 1 for ON, and 0 for OFF
#     print(checked_state.get())

# checked_state = IntVar()
# checkbutton = Checkbutton(text = "Is ON?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()

# ### RadioButton
# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# radiobutton_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton_1.pack()
# radiobutton_2.pack()


# ### List Box
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Mango", "Orange", "Bnana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)

# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()









# To keep window open and keep listening
window.mainloop()