import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS_X = [-600,600]

# STARTING_POSITIONS_Y = []


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # To limit the number of cars
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            # Color of the Car
            new_car.color(random.choice(COLORS))
            # Size of the Car
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # starting position
            Y = random.randint(-200,200)
            new_car.goto(300,Y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
