from turtle import Turtle
current_level = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f'LEVEL {self.current_level}', move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_level(self):
        self.clear()
        self.current_level += 1
        self.write(arg=f'LEVEL {self.current_level}', move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg=f'GAME OVER AT LEVEL {self.current_level}', move=False, align='center', font=('Arial', 20,
                                                                                                     'normal'))