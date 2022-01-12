from tkinter import Tk
import const


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("Flashy")
        self.config(padx=50, pady=50, bg=const.BACKGROUND_COLOR)
