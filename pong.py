from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong')

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
    time.sleep(0.006)
    ball.moving()

    if ball.ycor() > 285 or ball.y_move <-285:
        ball.bounce()











screen.exitonclick()