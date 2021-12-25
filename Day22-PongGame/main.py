from middleLine import MiddleLine
from screen_setup import ScreenSetup

screen = ScreenSetup()

X_FACTOR = int(screen.x_factor())
Y_FACTOR = int(screen.y_factor())

line = MiddleLine(Y_FACTOR)

screen.exitonclick()
