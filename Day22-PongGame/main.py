from turtle import Screen
from middleLine import MiddleLine
from screen_setup import ScreenSetup
from paddles import Paddles

screen = ScreenSetup()
paddle_move = Screen()

X_FACTOR = int(screen.x_factor())
Y_FACTOR = int(screen.y_factor())

line = MiddleLine(Y_FACTOR)

paddle = Paddles(X_FACTOR, Y_FACTOR)

paddle.left_paddle()
paddle.right_paddle()


screen.exitonclick()
