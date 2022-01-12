from buttons import Buttons
from cards import Cards
from window import Window
from data import Data
from random import randint

timer = ""
lang = None
index = None

data = Data()

window = Window()


def right_on():
    global index
    data.guessed_rows[index] = data.words_list[index]
    del data.words_list[index]
    start()


def counter(count):
    global index, lang, timer

    if count > 0:
        timer = window.after(1000, counter, count - 1)
    elif lang == "English":
        card.flip_to_back(english=data.words_list[index][1])
        lang = "French"
        counter(5)
    elif lang == "French":
        start()


def start():
    global index, lang, timer

    if timer != "":
        window.after_cancel(timer)

    index = randint(0, len(data.words_list))
    while index not in data.words_list:
        index = randint(0, len(data.words_list))

    card.flip_to_front(french=data.words_list[index][0])
    lang = "English"

    counter(3)


card = Cards()
card.canvas.grid(column=0, row=0, columnspan=2)

buttons = Buttons()
buttons.right_button.config(command=right_on)
buttons.wrong_button.config(command=start)
buttons.wrong_button.grid(column=0, row=1)
buttons.right_button.grid(column=1, row=1)

start()


window.mainloop()
