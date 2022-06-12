from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=0, y=-280)
        self.shape("circle")

    def move(self):
        ball_angle = random.randint(10, 70)
        self.setheading(ball_angle)
        for _ in range(100):
            self.forward(1)
