from turtle import Screen
from slider import Slider
import time


my_screen=Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title(titlestring="Pong Game")

right_slider=Slider(val_left_or_right="right")
left_slider=Slider(val_left_or_right="left")
my_screen.listen()
my_screen.onkey(fun=right_slider.move_up, key="Up")
my_screen.onkey(fun=right_slider.move_down,key="Down")
# my_screen.onkey(fun=left_slider.r_slider, key="r")

print(my_screen.onkey(fun=right_slider.move_up, key="Up"))

game_status=True
while game_status:
    my_screen.update()
    time.sleep(0.1)

    # game_status=False


my_screen.exitonclick()