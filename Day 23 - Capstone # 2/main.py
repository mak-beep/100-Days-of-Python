import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=turtle.up)
screen.onkeypress(key="Down", fun=turtle.down)
screen.onkeypress(key="Left", fun=turtle.left)
screen.onkeypress(key="Right", fun=turtle.right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with Car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finishline():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()


screen.exitonclick()