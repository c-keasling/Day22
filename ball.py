from turtle import Turtle
COLOR = 'white'
WIDTH = 1
HEIGHT = 1
UP = 90
DOWN = 180

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape('circle')
        self.goto(0,0)
        self.shapesize(stretch_wid=WIDTH,stretch_len=HEIGHT)
        self.hit = False
        self.moving_up = True
        self.x_move = 1
        self.y_move = 1



    def moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1


