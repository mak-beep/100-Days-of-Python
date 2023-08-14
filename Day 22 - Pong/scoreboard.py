from turtle import Turtle

FONT = ("Courier", 80, "normal")
ANNOUNCEMENT_FONT = ("Courier", 40, "normal")

# Points to Win
MAX_POINTS = 5
class Scoreboard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(pos)
        self.write(f"{self.score}", align="center", font=FONT)

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=FONT)
        if self.score == MAX_POINTS:
            self.game_over()
            return False
        else:
            return True

    def game_over(self):
        self.goto(0 ,50)
        self.write(f"GAME OVER.", align="center", font=ANNOUNCEMENT_FONT)

    def winner(self, Player):
        self.goto(0 ,-50)
        self.write(f"{Player} Won.", align="center", font=ANNOUNCEMENT_FONT)