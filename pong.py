from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
sleep_timer = 0.006
game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong')
scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkeypress(key='Up',fun=r_paddle.up)
screen.onkeypress(key='Down',fun=r_paddle.down)
screen.onkeypress(key='w',fun=l_paddle.up)
screen.onkeypress(key='s',fun=l_paddle.down)


while game_is_on:
    screen.update()
    if sleep_timer < 0.00009:
        sleep_timer = 0.00009
        time.sleep(sleep_timer)
        print("max speed")
    else:
        time.sleep(sleep_timer)
    ball.moving()

    if ball.ycor() > 285 or ball.ycor() <-285:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_timer *= .9
        print(sleep_timer)

    #detect r miss
    if ball.xcor() < 450 and ball.xcor() > 445 :
        ball.reset_ball()
        scoreboard.l_point()
        sleep_timer = 0.006

    # detect l miss
    if ball.xcor() < -450 and ball.xcor() < -445:
        ball.reset_ball()
        scoreboard.r_point()
        sleep_timer = 0.006

    if scoreboard.l_score >= 11:
        game_is_on = False
        scoreboard.declare_winner()

    if scoreboard.r_score >= 11:
        game_is_on = False
        scoreboard.declare_winner()











screen.exitonclick()