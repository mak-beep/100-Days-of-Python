from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x, current_y + MOVE_DISTANCE)
    def down(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x, current_y - MOVE_DISTANCE)
    def left(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x - MOVE_DISTANCE, current_y)
    def right(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + MOVE_DISTANCE, current_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.go_to_start()
            return True
        else:
            return False