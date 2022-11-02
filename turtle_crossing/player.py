from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)
        self.move_speed = self.move_speed * 0.9