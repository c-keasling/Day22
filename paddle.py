from turtle import Turtle
COLOR = 'white'
WIDTH = 20
HEIGHT = 100
UP = 90
DOWN = 180


class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.x_coodinate = coordinates[0]
        self.y_cordinate = coordinates[1]
        self.penup()
        self.color(COLOR)
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x=self.x_coodinate,y=self.y_cordinate)

    def up(self):
        new_y_pos = self.ycor() +20
        if new_y_pos <=260:
            self.goto(y=new_y_pos,x=self.x_coodinate)



    def down(self):
        new_y_pos = self.ycor() -20
        if new_y_pos >= -240:
            self.goto(y=new_y_pos, x=self.x_coodinate)


