# reuired libraries
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
WAIT_SECOND = 5
button_pressed = False
word = 0
length = 0
TIMER_POS = (400,50)
TITLE_POS = (400,150)
WORD_POS = (400,300)

# 

def change_card(word, title):
    card.itemconfig(title_text, text = f"{title}")
    card.itemconfig(word_text, text = f"{word}")

def start_timer():    
    count_down(WAIT_SECOND)
    # return True

def count_down(count):
    card.itemconfig(timer_text, text = f"{count}")
    timer = window.after(1000, count_down, count-1)
    global word, button_pressed, english_word
    if count < 1:
        window.after_cancel(timer)
        image = PhotoImage(file = "./Day 31 - Flash Card Capstone/images/card_back.png")
        card.itemconfig(background_img ,image = image)
        button_pressed = False
        english_word = english_words[word]
        title = "English"
        change_card(english_word, title)

def new_word():
    image = PhotoImage(file = "./Day 31 - Flash Card Capstone/images/card_front.png")
    card.itemconfig(background_img, image = image)
    global length, english_words, french_words, french_word, word
    length -= 1
    word = random.randint(0,length)
    french_word = french_words[word]
    title = "French"
    # Change the card
    change_card(french_word, title)
    start_timer()

def right_option():
    global button_pressed, english_words, french_words, english_word, french_word
    if (not button_pressed):
        english_words.remove(english_word)
        french_words.remove(french_word)
        button_pressed = True
        new_word()

def wrong_option():
    global button_pressed
    if (not button_pressed):
        button_pressed = True
        new_word()


# Text
data = pandas.read_csv("./Day 31 - Flash Card Capstone/data/french_words.csv")
length = len(data)
french_words = data["French"].to_list()
english_words = data["English"].to_list()

# Window
window = Tk()
window.title("Flash Card App")
window.minsize(width=850, height=700)
window.config(padx=30, pady=50, bg=BACKGROUND_COLOR)

# Canvas - Image
card = Canvas(width = 800, height=520, highlightthickness=0, background=BACKGROUND_COLOR)
image = PhotoImage(file = "./Day 31 - Flash Card Capstone/images/card_front.png")
background_img = card.create_image(400,260,image = image)
# card.place(x= 0, y = 0)
card.grid(column=0,row=0, columnspan=2)

timer_text = card.create_text(TIMER_POS,text="", fill = "black", font = (FONT_NAME,35,"bold"))
title_text = card.create_text(TITLE_POS,text="Title", fill = "black", font = (FONT_NAME,35,"italic"))
word_text = card.create_text(WORD_POS,text="Word", fill = "black", font = (FONT_NAME,35,"bold"))

# Buttons
photo_right = PhotoImage(file="./Day 31 - Flash Card Capstone/images/right.png")
right_btn = Button(image = photo_right, highlightthickness=0, border=0, command=right_option)
right_btn.place(x = 500, y = 550)
right_btn.grid(column=1,row=1)
photo_wrong = PhotoImage(file="./Day 31 - Flash Card Capstone/images/wrong.png")
wrong_btn = Button(image = photo_wrong, highlightthickness=0,border=0, command=wrong_option)
# wrong_btn.place(x = 200, y = 550)
wrong_btn.grid(column=0,row=1)

# Initial Word
try:
    word = random.randint(1,length)
except Exception as e:
    print(e)
    exit()
french_word = french_words[word]
title = "French"
change_card(french_word, title)
start_timer()



window.mainloop()