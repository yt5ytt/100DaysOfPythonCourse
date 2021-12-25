from turtle import Screen
from middleLine import MiddleLine

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
X_FACTOR = int(screen.window_width()/2)
Y_FACTOR = int(screen.window_height()/2)

line = MiddleLine(Y_FACTOR)




screen.exitonclick()