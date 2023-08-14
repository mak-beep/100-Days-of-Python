# docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

tis = Turtle()
tis.color("coral")
tis.shape("turtle")
print(tis)
my_screen = Screen()
my_screen.canvheight = 480
my_screen.canvwidth = 680
tis.forward(100)
my_screen.exitonclick()