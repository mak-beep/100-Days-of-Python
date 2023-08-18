# reuired libraries
from tkinter import *
import pandas
import random
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
WAIT_SECOND = 5
current_card = {}
TIMER_POS = (400,50)
TITLE_POS = (400,150)
WORD_POS = (400,300)

def flip():
    card.itemconfig(background_img ,image = Card_Back)
    card.itemconfig(title_text, text = "English")
    card.itemconfig(word_text, text = current_card["English"])

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    card.itemconfig(background_img, image = Card_Front)
    current_card = random.choice(words)
    card.itemconfig(title_text, text = "French")
    card.itemconfig(word_text, text = current_card["French"])
    flip_timer = window.after(5000, flip)
        
def right_option():
    words.remove(current_card)
    print(len(words))
    data = pandas.DataFrame(words)
    data.to_csv("./Day 31 - Flash Card Capstone/V2/data/words_to_learn.csv", index=False)

    new_card()

# Data Files
try:
    data = pandas.read_csv("./Day 31 - Flash Card Capstone/V2/data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./Day 31 - Flash Card Capstone/V2/data/french_words.csv")
    words = original_file.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

# Window
window = Tk()
window.title("Flash Card App")
window.minsize(width=850, height=700)
window.config(padx=30, pady=50, bg=BACKGROUND_COLOR)

# Timer for Flipping the Card
flip_timer = window.after(5000, flip)

# Canvas - Image
card = Canvas(width = 800, height=520, highlightthickness=0, background=BACKGROUND_COLOR)
Card_Front = PhotoImage(file = "./Day 31 - Flash Card Capstone/V2/images/card_front.png")
Card_Back = PhotoImage(file = "./Day 31 - Flash Card Capstone/V2/images/card_back.png")
background_img = card.create_image(400,260,image = Card_Front)
# card.place(x= 0, y = 0)
card.grid(column=0,row=0, columnspan=2)

timer_text = card.create_text(TIMER_POS,text="", fill = "black", font = (FONT_NAME,35,"bold"))
title_text = card.create_text(TITLE_POS,text="Title", fill = "black", font = (FONT_NAME,35,"italic"))
word_text = card.create_text(WORD_POS,text="Word", fill = "black", font = (FONT_NAME,35,"bold"))

# Buttons
photo_right = PhotoImage(file="./Day 31 - Flash Card Capstone/V2/images/right.png")
right_btn = Button(image = photo_right, highlightthickness=0, border=0, command=right_option)
right_btn.place(x = 500, y = 550)
right_btn.grid(column=1,row=1)
photo_wrong = PhotoImage(file="./Day 31 - Flash Card Capstone/V2/images/wrong.png")
wrong_btn = Button(image = photo_wrong, highlightthickness=0,border=0, command=new_card)
# wrong_btn.place(x = 200, y = 550)
wrong_btn.grid(column=0,row=1)


new_card()



window.mainloop()