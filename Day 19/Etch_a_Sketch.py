from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
# tim.pensize(5)

colormode(255)
def forward():
    tim.forward(10)

def backward():
    tim.back(10)

def turn_left():
    tim.setheading(tim.heading()+10)
def turn_right():
    tim.setheading(tim.heading()-10)
def clear_all():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def curve_right():
    for i in range(100):
        turn_right()
        forward()

def curve_left():
    for i in range(100):
        turn_left()
        forward()

while True:
    screen.listen()
    screen.onkey(key="w", fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear_all)

    screen.exitonclick()