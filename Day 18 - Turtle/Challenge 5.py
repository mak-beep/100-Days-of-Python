from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
# tim.pensize(5)

colormode(255)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tup = (r, g, b)
    tim.pencolor(tup)

def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.circle(100)
        random_color()
        tim.setheading(tim.heading() + gap)
        # tim.left(gap)

draw_spirograph(10)

screen.exitonclick()