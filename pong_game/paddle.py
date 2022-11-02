from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)

    def move_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)