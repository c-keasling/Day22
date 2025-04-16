from turtle import Turtle
COLOR = 'white'
WIDTH = 20
HEIGHT = 100
UP = 90
DOWN = 180


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.color(COLOR)
        self.paddle.shape('square')
        self.paddle.goto(x=0, y=0)
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.goto(x=350,y=0)

    def up(self):
        new_y_pos = self.paddle.ycor() +20
        if new_y_pos <=260:
            self.paddle.goto(y=new_y_pos,x=350)



    def down(self):
        new_y_pos = self.paddle.ycor() -20
        if new_y_pos >= -240:
            self.paddle.goto(y=new_y_pos, x=350)


