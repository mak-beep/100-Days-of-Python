import turtle
from turtle import Turtle
from time import sleep
STARTING_POSIIONS = [0,20,-20]

HERO = -270
ENEMY = 270

MOVE_DISTANCE = 20

UP = 90
DOWN = 270

turtle.tracer(0)
class Player(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.create_player(pos)

        # self.head = self.body

    def create_player(self,pos):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(pos)
        # sleep(5)

    def move(self,heading):
        self.setheading(heading)

        self.forward(MOVE_DISTANCE)
        self.x = self.xcor()
        self.y = self.ycor()
        self.pos = (self.x, self.y)
        turtle.update()

    def up(self):
        if self.y <290:
            self.move(UP)
    def down(self):
        if self.y > -290:
            self.move(DOWN)