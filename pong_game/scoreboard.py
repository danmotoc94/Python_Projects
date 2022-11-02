from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f'Player 1: {self.score_player1} | Player 2: {self.score_player2} ', move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def increase_score_player1(self):
        self.score_player1 += 1
        self.clear()
        self.hideturtle()
        self.write(arg=f'Player 1: {self.score_player1} | Player 2: {self.score_player2} ', move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def increase_score_player2(self):
        self.score_player2 += 1
        self.clear()
        self.hideturtle()
        self.write(arg=f'Player 1: {self.score_player1} | Player 2: {self.score_player2} ', move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        if self.score_player2 == 3:
            self.write(arg=f'Game over! Player 2 won with {self.score_player2} points', move=False, align='center',
                       font=('Arial', 20, 'normal'))
        elif self.score_player1 == 3:
            self.write(arg=f'Game over! Player 1 won with {self.score_player1} points', move=False, align='center',
                       font=('Arial', 20, 'normal'))