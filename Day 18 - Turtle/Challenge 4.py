from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
tim.pensize(5)

colormode(255)

directions = [0,90,180,270]
def walk(steps,turn):
    tim.forward(steps)
    tim.left(turn)

for i in range(100):
    steps = 30
    turn = random.choice(directions)
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    tup = (r,g,b)
    tim.pencolor(tup)
    walk(steps,turn)


screen.exitonclick()