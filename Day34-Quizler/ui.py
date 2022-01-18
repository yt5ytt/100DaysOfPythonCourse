from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.box_text = self.canvas.create_text(150, 125, text="Here goes text of question", font=CANVAS_FONT,
                                                width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right = Button()
        right_image = PhotoImage(file="images/true.png")
        self.right.config(image=right_image, highlightthickness=0)
        self.right.grid(column=0, row=2)

        self.wrong = Button()
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong.config(image=wrong_image, highlightthickness=0)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.box_text, text=q_text)
