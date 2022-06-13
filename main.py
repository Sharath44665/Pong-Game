from turtle import Screen
from slider import Slider
from ball import Ball
from score_board import ScoreBoard
import time,random

speed_list=[6,10,0]
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title(titlestring="Pong Game")
my_screen.tracer(0)  # tracer is off meaning animation off

right_slider = Slider(x_val=350, y_val=0)
left_slider = Slider(x_val=-350, y_val=0)
ball = Ball()
score_card=ScoreBoard()
my_screen.listen()

my_screen.onkey(fun=right_slider.move_up, key="Up")
my_screen.onkey(fun=right_slider.move_down, key="Down")
my_screen.onkey(fun=left_slider.move_up, key="w")
my_screen.onkey(fun=left_slider.move_down, key="s")

game_status = True
while game_status:
    my_screen.update()
    time.sleep(0.1)

    ball.move()
    if ball.ycor() >= 298 or ball.ycor() <= -298:
        ball.detect_collision()
    if ball.distance(right_slider) < 50 and ball.xcor() > 335   or ball.distance(left_slider) < 50 and ball.xcor() < -335  :
        ball.detect_slider_collision()
    #if missed by right side player
    if ball.xcor() > 350:
        ball.reset_position()
        score_card.get_score_left_player()
    # if missed by left side player
    if ball.xcor() < -350:
        ball.reset_position()
        score_card.get_score_right_player()
    ball_sepped=random.choice(speed_list)
    ball.speed()
my_screen.exitonclick()
