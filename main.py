import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Creating a random car every after .5 second
    cars.create_car()
    cars.move_cars()

    # Detecting collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # if player.ycor() >= 290:
    if player.finished():
        player.reseting()
        score.update_score()
        cars.level_up()












screen.exitonclick()