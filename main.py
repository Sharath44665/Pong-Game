from turtle import Screen
from slider import Slider
import time


my_screen=Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title(titlestring="Pong Game")
my_screen.tracer(0) #tracer is off meaning animation off

right_slider=Slider()
my_screen.listen()

my_screen.onkey(fun=right_slider.move_up, key="Up")
my_screen.onkey(fun=right_slider.move_down, key="Down")

game_status=True
while game_status:
    my_screen.update()
    time.sleep(0.1)

    # game_status=False


my_screen.exitonclick()