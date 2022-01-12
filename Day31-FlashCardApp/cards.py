from tkinter import Canvas, PhotoImage

import const


class Cards:

    def __init__(self):
        self.front_card_image = PhotoImage(file="./images/card_front.png")
        self.back_card_image = PhotoImage(file="./images/card_back.png")
        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg=const.BACKGROUND_COLOR)
        self.image_container = self.canvas.create_image(400, 263, image=self.front_card_image)
        self.lang = self.canvas.create_text(400, 150, text="French", fill="black", font=const.LANG_FONT)
        self.word = self.canvas.create_text(400, 263, text="French", fill="black", font=const.WORD_FONT)

    def flip_to_back(self, english):
        self.canvas.itemconfig(self.image_container, image=self.back_card_image)
        self.canvas.itemconfig(self.lang, text="English")
        self.canvas.itemconfig(self.word, text=english)

    def flip_to_front(self, french):
        self.canvas.itemconfig(self.image_container, image=self.front_card_image)
        self.canvas.itemconfig(self.lang, text="French")
        self.canvas.itemconfig(self.word, text=french)

