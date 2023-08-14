from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)

# Challenge 1 - Square
def square():
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.forward(100)
    tim.left(90)

square()

screen.exitonclick()