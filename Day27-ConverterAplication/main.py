from tkinter import *

# Creating a window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=50)

# Create entry widget
input_text = Entry()
input_text.grid(column=1, row=0)
input_text.config(width=10)

# Creating "Miles" Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# Creating "Km" Label
km = Label(text="Km")
km.grid(column=2, row=1)

# Creating "is equal to" Label
equal = Label(text="is equal to")
equal.grid(column=0, row=1)

# Creating result Label
result = Label(text="0")
result.config(padx=50, pady=20)
result.grid(column=1, row=1)

# Creating "Calculate" button


def action():
    miles_num = float(input_text.get())
    km_num = round(miles_num * 1.60934, 2)
    result.config(text=f"{km_num}")


calculate = Button(text="Calculate", command=action)
calculate.grid(column=1, row=2)

window.mainloop()
