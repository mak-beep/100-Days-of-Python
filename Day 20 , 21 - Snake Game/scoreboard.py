from turtle import Turtle

FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-0, 250)
        self.write(f"Score : {self.score} High Score = {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0 ,0)
    #     self.write(f"GAME OVER.", align="center", font=FONT)
