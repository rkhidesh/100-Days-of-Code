import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.reach_finish_line():
        player.goto(0, -280)
        car.level_up()
        score.increase_level()


screen.exitonclick()