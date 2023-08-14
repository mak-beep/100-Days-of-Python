import turtle
from turtle import Turtle, Screen
from time import sleep
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.screensize(400,400)
screen.bgcolor("black")
screen.title("My Snake Game")

turtle.tracer(0)
speed = 0.1
game_is_on = True
# Snake Body
snake = Snake()

scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")


food = Food()
while game_is_on:

    snake.move()
    sleep(0.1)
    turtle.update()
    # Check collision of snake and food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()

    if (snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300):
        scoreboard.reset()
        snake.reset()
    for segment in snake.body[1:]:
        if segment == snake.head:
            pass
        elif (snake.head.distance(segment) < 10):
            snake.reset()
            scoreboard.reset()
screen.exitonclick()