from turtle import Turtle, Screen

tim = Turtle()
tim.shape("square")
tim.speed(1)
tim.penup()
tim.color("white")
tim.shapesize(1, 3)
screen = Screen()
screen.setup()
screen.bgcolor("black")


def left():
    tim.left(90)


def right():
    tim.right(90)


tim_moving = True
while tim_moving:
    tim.forward(10)
    screen.listen()
    screen.onkey(left, "a")
    screen.onkey(right, "d")

screen.exitonclick()
