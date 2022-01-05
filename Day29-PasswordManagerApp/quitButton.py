from tkinter import Button


class QuitButton(Button):

    def __init__(self):
        super().__init__()
        self.config(
            text="Quit",
            padx=20, pady=10,
            fg="white", bg="blue",
            borderwidth=10,
            font=("Arial", 20, "bold"),
        )
        self.grid(column=0, row=0)
