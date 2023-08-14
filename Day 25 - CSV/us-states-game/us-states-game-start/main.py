import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "D:/100 Days of Python/Day 25 - CSV/us-states-game/us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# ## To get location of the Mouse (i.e., Arrow)

# def mouse_screen_click_coor(x, y):
#     print(x,y)

# turtle.onscreenclick(mouse_screen_click_coor)
# turtle.mainloop()

# ## Importing all_states from the CSV
data = pandas.read_csv("D:/100 Days of Python/Day 25 - CSV/us-states-game/us-states-game-start/50_states.csv")
all_states = data.state.to_list()
# print(states_names)

guessed_states = []
while len(guessed_states) < 50:
    # # POP-UP Box
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guess the State.", "What's another state's name?").title()
    print(answer_state)
    if answer_state in all_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        x_cor = state_data.x
        y_cor = state_data.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cor),int(y_cor))
        # t.write(answer_state)
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # exit()
        break

# States to learn.csv
data_dict = {
    "Missed States": missing_states
}
data = pandas.DataFrame(data_dict)
data.to_csv("D:/100 Days of Python/Day 25 - CSV/us-states-game/us-states-game-start/learn.csv")