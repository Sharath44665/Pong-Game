from turtle import Turtle

DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Slider(Turtle):
    def __init__(self,val_left_or_right):
        super().__init__()
        self.r_slider = []

        if val_left_or_right=="right":
            self.create_slider(380)
        elif val_left_or_right=="left":
            self.create_slider(-380)

        self.r_slider_head = self.r_slider[0]

    def create_slider(self,x_val):
        for _ in range(3):
            slider = Turtle()
            slider.shape(name="square")
            slider.penup()
            slider.color("white")
            self.r_slider.append(slider)

        y_val = 0

        for l in self.r_slider:
            l.goto(x=x_val, y=y_val)
            y_val += 20

    def move(self):
        for index_of_slider in range(len(self.r_slider) - 1, 0, -1):
            x_val = self.r_slider[index_of_slider - 1].xcor()
            y_val = self.r_slider[index_of_slider - 1].ycor()
            self.r_slider[index_of_slider].goto(x=x_val, y=y_val)
        self.r_slider_head.forward(DISTANCE)

    def move_up(self):
        self.r_slider_head.setheading(UP)
        self.move()

    def move_down(self):
        self.r_slider_head.setheading(DOWN)
        self.move()

    def right_slider(self):
        pass
