from turtle import Turtle


class Paddles:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.LEFT_PADDLE = [(-(self.x - 40), 0), (-(self.x - 40), 20), (-(self.x - 40), 40), (-(self.x - 40), 60)]
        self.RIGHT_PADDLE = [(self.x - 40, 0), (self.x - 40, 20), (self.x - 40, 40), (self.x - 40, 60)]
        self.leftPaddleSegments = []
        self.rightPaddleSegments = []

    def left_paddle(self):
        for segment in self.LEFT_PADDLE:
            self.create_segments(segment)
            self.leftPaddleSegments.append(segment)

    def right_paddle(self):
        for segment in self.RIGHT_PADDLE:
            self.create_segments(segment)
            self.rightPaddleSegments.append(segment)

    def create_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
