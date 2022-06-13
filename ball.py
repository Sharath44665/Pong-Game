from turtle import Turtle
# from main import right_slider
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        # self.goto(x=0, y=-280)
        self.shape("circle")
        self.y_move = 10

    def move(self):
        xpos = self.xcor() + 10
        ypos = self.ycor() + self.y_move
        self.goto(x=xpos, y=ypos)

    def detect_collision(self):
        self.y_move *= -1
