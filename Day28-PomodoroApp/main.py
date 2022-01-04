from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check_mark = ""
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global check_mark
    reps = 1
    check_mark = ""
    window.after_cancel(my_timer)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text=check_mark)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if reps % 2 == 1:
        count_down(WORK_MIN*60)
        timer.config(fg=GREEN, text="Work")
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(fg=PINK, text="Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global my_timer
    count_min = int(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        global check_mark
        reps += 1
        if reps <= 8:
            start_timer()
            if reps % 2 == 0:
                check_mark += "✔"
                checks.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=200, pady=100, bg=YELLOW)
window.title("Pomodoro Application")

# Label "Timer" text
timer = Label(text="Timer")
timer.config(fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checks Label area

checks = Label(text=check_mark, fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
checks.grid(column=1, row=3)

window.mainloop()
