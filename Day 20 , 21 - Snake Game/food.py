import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()


    def create_food(self):
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)