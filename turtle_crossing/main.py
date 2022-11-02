from turtle import Screen
from cars import Car
from player import Player
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
game_on = True
car = Car()
scoreboard = Scoreboard()
while game_on:
    screen.update()
    time.sleep(player.move_speed)
    car.create_car()
    car.move()
# Detect collision with car
    for current_car in car.all_cars:
        if player.distance(current_car) < 20:
            game_on = False
            screen.clear()
            scoreboard.game_over()
# Detect if player has reached the other end
    if player.ycor() > 290:
        player.reset()
        scoreboard.increase_level()
screen.exitonclick()