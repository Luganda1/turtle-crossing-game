import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_ch = random.randint(1, 5)
        if random_ch == 2:
            timmy = Turtle()
            timmy.shape("square")
            timmy.penup()
            timmy.shapesize(stretch_wid=1, stretch_len=2)
            timmy.color(random.choice(COLORS))
            new_y = random.randrange(-240, 240)
            timmy.goto(300, new_y)
            self.all_cars.append(timmy)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
