from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def l_point(self):
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Amazon ember", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Amazon ember", 60, "normal"))

    def declare_winner(self):
        if self.l_score >= 11:
            self.goto(0, 100)
            self.write("Left Side Won!!", align="center", font=("Amazon ember", 60, "normal"))

        if self.r_score >= 11:
            self.goto(0, 100)
            self.write("Right Side Won!!", align="center", font=("Amazon ember", 60, "normal"))