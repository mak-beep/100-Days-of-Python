import random
import turtle
from turtle import Turtle, Screen
from players import Player
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

screen = Screen()
screen.screensize(600,600,"black")
screen.title("Pong")
DIFFICULTY = 0.1
turtle.tracer(0)
l_player = Player((-350,0))
r_player = Player((350,0))
ball = Ball()



l_scoreboard = Scoreboard((-100,200))
r_scoreboard = Scoreboard((100,200))

# y = 0
# def add_segment(pos):
#     segment = Turtle("square")
#     segment.color("white")
#     segment.shapesize(2)
#     segment.penup()
#     segment.goto(0, pos)
#
# add_segment(0)
# for i in range(5):
#     y += 60
#     add_segment(y)
#     add_segment(-y)
#     turtle.update()

game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=r_player.up)
screen.onkeypress(key="Down",fun=r_player.down)
screen.onkeypress(key="w", fun=l_player.up)
screen.onkeypress(key="s",fun=l_player.down)

while game_is_on:
    sleep(ball.speed)
    ball.move()
    screen.update()
    # Detects Collision with the Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Hit with Paddle
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # r_player misses
    if ball.xcor()>380:
        game_is_on = l_scoreboard.point()
        if (not game_is_on):
            l_scoreboard.winner("Left Player")
        ball.reset_position()
        ball.bounce_x()


    # l_player misses
    if ball.xcor()<-380:
        game_is_on = r_scoreboard.point()
        if (not game_is_on):
            r_scoreboard.winner("Right Player")
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()