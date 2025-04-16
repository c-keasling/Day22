from turtle import Turtle,Screen
from paddle import Paddle

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong')

paddle = Paddle()
screen.listen()
screen.onkeypress(key='Up',fun=paddle.up)
screen.onkeypress(key='Down',fun=paddle.down)


while game_is_on:
    screen.update()











screen.exitonclick()