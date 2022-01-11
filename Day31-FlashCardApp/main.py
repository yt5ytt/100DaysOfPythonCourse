from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 80, "bold")

# Read csv file


def read_csv():
    """Read csv file and iterate trough rows of file. Returns rows generator"""
    data = pandas.read_csv("./data/french_words.csv")
    rows = data.iterrows()
    return rows

# UI experience


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_card_image)
lang = canvas.create_text(400, 150, text="English", fill="black", font=LANG_FONT)
word = canvas.create_text(400, 263, text="Chair", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button()
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button.config(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_button = Button()
right_image = PhotoImage(file="./images/right.png")
right_button.config(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)











window.mainloop()
