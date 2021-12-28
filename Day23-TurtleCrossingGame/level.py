from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.move_speed = 0.1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "bold"))

    def level_up(self):
        self.level += 1
        self.move_speed *= 0.9
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", align="center", font=("Courier", 20, "bold"))