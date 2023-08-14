from tkinter import *

window = Tk()
window.title("Miles To Km Converter")
# window.minsize(width=300,height=300)
window.config(padx=20,pady=20)

FONT =("Arial", 15)

checkValue = IntVar()

def calculate():
    input = float(miles_input.get())
    if checkValue.get():
        output = round(input * 1.609)
    else:
        output = round(input / 1.609)


    kilometer_result_label.config(text=f"{output}")


miles_label = Label(text="Miles", font = FONT)
miles_label.grid(column=2,row=0)
miles_label.config(padx = 25, pady = 10)

miles_input = Entry(width=10)
miles_input.focus()
miles_input.grid(column=1,row=0)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0,row=1)
is_equal_label.config(padx = 25, pady = 10)

kilometer_result_label = Label(text=0, font=FONT)
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km", font = FONT)
kilometer_label.grid(column=2,row=1)
kilometer_label.config(padx = 25, pady = 10)

calculate_button = Button(text="Calculate", font = FONT, command=calculate)
calculate_button.grid(column=1,row=2)

def miles_to_km():
    if (checkValue.get()):
        kilometer_label.config(text="Km")
        miles_label.config(text="Miles")
        print("Called1")
    else:
        kilometer_label.config(text="Miles")
        miles_label.config(text="Km")
        print("Called2")

miles_to_km_check = Checkbutton(text="Miles to Km?", variable=checkValue, command=miles_to_km)
# By default selection
miles_to_km_check.select()
miles_to_km_check.grid(column=2,row=2)

window.mainloop()