from turtle import Turtle

UP = 90
DOWN = 270
DISTANCE = 10


class Slider(Turtle):
    def __init__(self, x_val, y_val):
        super().__init__()
        self.slider_pos = (x_val, y_val)
        self.create_slider(self.slider_pos)
        self.new_y = 0


    def create_slider(self, slider_pos):
        self.shape(name="square")
        self.width = 20
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        posx = slider_pos[0]
        posy = slider_pos[1]
        self.goto(x=posx, y=posy)

    def move_up(self):
        self.new_y += 20
        self.goto(x=self.slider_pos[0], y=self.new_y)

    def move_down(self):
        self.new_y -= 20
        self.goto(x=self.slider_pos[0], y=self.new_y)
