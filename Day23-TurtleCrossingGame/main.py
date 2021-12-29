from turtle import Screen
from littleTurtle import LittleTurtle
from level import Level
from cars import Cars
import random
import time

all_cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

myTurtle = LittleTurtle()
level = Level()
screen.onkey(myTurtle.move_forward, "Up")

loop_number = 1
game_is_on = True

while game_is_on:
    time.sleep(level.move_speed)

    random_y = random.randint(-260, 240)
    if loop_number % 6 == 0:
        car = Cars(random_y)
        all_cars.append(car)

    for car in all_cars:
        # Move cars
        car.move()

        # Erase car from list, when car goes to the edge of screen
        if car.xcor() < -320:
            all_cars.remove(car)

        # Check if cars hits turtle
        if myTurtle.distance(car) < 20:
            level.game_over()
            game_is_on = False

    # Detect if turtle cross the street
    if myTurtle.ycor() > 280:
        level.level_up()
        myTurtle.reset_turtle()

    screen.update()
    loop_number += 1

screen.exitonclick()
