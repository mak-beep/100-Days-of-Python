from turtle import Turtle

STARTING_POSIIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.direction = "right"
        self.x = 0
        self.y = 0

    def create_snake(self):
        for position in STARTING_POSIIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            [new_x, new_y] = self.body[seg_num - 1].position()
            self.body[seg_num].goto(new_x, new_y)

        self.body[0].forward(MOVE_DISTANCE)
        self.x = self.head.xcor()
        self.y = self.head.ycor()

    def reset(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def left(self):
        if self.direction != "right":
            self.head.setheading(LEFT)
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.head.setheading(RIGHT)
            self.direction = "right"
    def up(self):
        if self.direction != "down":
            self.head.setheading(UP)
            self.direction = "up"
    def down(self):
        if self.direction != "up":
            self.head.setheading(DOWN)
            self.direction = "down"