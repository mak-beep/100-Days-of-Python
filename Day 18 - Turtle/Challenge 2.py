from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)

# Challenge 2 - Dashed Line
def dashed_line(paces):
    for i in range(paces):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)

    tim.hideturtle()

dashed_line(10)

screen.exitonclick()