from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            current_high_score = file.read()
        self.high_score = int(current_high_score)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score} ', move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode='w') as file:
                file.write(f'{self.score}')
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

