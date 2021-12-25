from turtle import Turtle

class MiddleLine(Turtle):

    def __init__(self, y_factor):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.pensize(5)
        self.penup()
        self.goto(0, -(y_factor))
        self.setheading(90)
        while self.ycor() < y_factor:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)