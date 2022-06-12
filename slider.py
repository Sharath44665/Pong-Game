from turtle import Turtle

UP = 90
DOWN = 270
DISTANCE = 10


class Slider(Turtle):
    def __init__(self):
        super().__init__()
        self.slider = self.create_right_slider()
        self.new_y=0

    def create_right_slider(self):
        slider = Turtle()
        slider.shape(name="square")
        slider.width = 20
        slider.penup()
        slider.color("white")
        slider.shapesize(stretch_wid=5, stretch_len=1)
        slider.goto(x=350, y=0)
        return slider

    # def move(self):
    #     self.slider.forward(DISTANCE)

    def move_up(self):
        self.new_y+=20
        self.slider.goto(x=350,y=self.new_y)

    def move_down(self):
        self.new_y -= 20
        self.slider.goto(x=350, y=self.new_y)