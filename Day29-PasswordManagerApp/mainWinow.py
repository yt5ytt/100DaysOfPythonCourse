from tkinter import Tk


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.config(
            width=1000,
            height=800,
            pady=100,
            padx=200
        )
        self.title("Password Manager Application")
