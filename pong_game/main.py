from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
# collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
# collision with the paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or \
            (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.bounce_x()
# ball goes out of boundaries
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_player1()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_player2()
    if scoreboard.score_player1 == 3 or scoreboard.score_player2 == 3:
        scoreboard.game_over()
        game_on = False
screen.exitonclick()