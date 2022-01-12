from tkinter import Button, PhotoImage

import const


class Buttons:

    def __init__(self):
        self.right_image = PhotoImage(file="./images/right.png")
        self.wrong_image = PhotoImage(file="./images/wrong.png")
        self.right_button = Button(image=self.right_image)
        self.right_button.config(bg=const.BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.wrong_button = Button(image=self.wrong_image)
        self.wrong_button.config(bg=const.BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)

