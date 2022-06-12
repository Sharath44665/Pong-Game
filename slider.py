from turtle import Turtle

UP = 90
DOWN = 270
DISTANCE = 10


class Slider(Turtle):
    def __init__(self):
        super().__init__()
        self.slider = self.create_right_slider()

    def create_right_slider(self):
        slider = Turtle()
        slider.shape(name="square")
        slider.width = 20
        slider.penup()
        slider.color("white")
        slider.goto(x=350, y=0)
        return slider

    def move(self):
        self.slider.forward(DISTANCE)

    def move_up(self):
        self.slider.setheading(UP)
        self.move()

    def move_down(self):
        self.slider.setheading(DOWN)
        self.move()
