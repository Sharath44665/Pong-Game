from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")

        self.hideturtle()

        self.left_score=0
        self.right_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Arial", 12, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Arial", 12, "normal"))

    def get_score_left_player(self):
        self.left_score+=1
        self.update_score()
    def get_score_right_player(self):
        self.right_score += 1
        self.update_score()

