from turtle import Turtle, Screen, colormode
import random
all_turtles = []
turtle_colors = ["red","blue","green","pink","yellow","orange"]
y_pos = [-50, -30, -10 , 10 , 30, 50]
screen = Screen()
screen.setup(300,300)
# tim.pensize(5)
is_race_started = False
user_bet = screen.textinput("Make a bet", "Which turtle will will the race? Enter a color : ")
for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x =-250,y = y_pos[turtle])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_started = True

while is_race_started:
    for turtle in all_turtles:
        if turtle.xcor()>=230:
            winning_color = turtle.pencolor()
            is_race_started = False
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the winner.")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner.")

        distance = random.randint(10,20)

        turtle.forward(distance)
screen.exitonclick()