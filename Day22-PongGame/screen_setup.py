from turtle import Screen


class ScreenSetup:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1.0, height=1.0)

        # remove close, minimize, maximize buttons:
        canvas = self.screen.getcanvas()
        root = canvas.winfo_toplevel()
        root.overrideredirect(True)

        self.screen.bgcolor("black")

    def exitonclick(self):
        self.screen.exitonclick()

    def x_factor(self):
        return int(self.screen.window_width() / 2)

    def y_factor(self):
        return int(self.screen.window_height() / 2)
