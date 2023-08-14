from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)

# Challenge 3 - Different Shapes
def draw_shape(paces, sides):
    angle = 360/sides
    for i in range(sides):
        tim.forward(paces)
        tim.right(angle)

# Triangle to Decagon
for i in range(3,10):
    draw_shape(100, i)

screen.exitonclick()