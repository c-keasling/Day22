from turtle import Turtle
COLOR = 'white'
WIDTH = 5
HEIGHT = 1
UP = 90
DOWN = 180


class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]
        self.penup()
        self.color(COLOR)
        self.shape('square')
        self.shapesize(stretch_wid=WIDTH,stretch_len=HEIGHT)
        self.goto(x=self.x_coordinate, y=self.y_coordinate)

    def up(self):
        new_y_pos = self.ycor() +20
        if new_y_pos <=260:
            self.goto(y=new_y_pos, x=self.x_coordinate)



    def down(self):
        new_y_pos = self.ycor() -20
        if new_y_pos >= -240:
            self.goto(y=new_y_pos, x=self.x_coordinate)


