from turtle import Turtle
LEVEL_FONT = ("Courier", 16, "normal")
ANNOUNCEMENT_FONT = ("Courier", 26, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"level = {self.level}", align = "left", font = LEVEL_FONT)

    def  update_scoreboard(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", align = "center", font = ANNOUNCEMENT_FONT)

