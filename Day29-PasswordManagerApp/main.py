from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_data = website_input.get()
    email_data = email_input.get()
    pass_data = pass_input.get()
    data = f"{website_data} | {email_data} | {pass_data}\n"

    message_ok = f'''
Website: {website_data},
Email: {email_data},
Password: {pass_data}.
Is this right data?
    '''

    if not website_data or not pass_data:
        is_empty = messagebox.showerror(title="Oooops", message="Some of your fields are empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=message_ok)    

    if is_ok:
        with open("data.txt", "a") as f:
            f.write(data)
            website_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:", height=2)
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password", height=2)
password.grid(column=0, row=3)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "yt5ytt@gmail.com")

pass_input = Entry(width=25)
pass_input.grid(column=1, row=3)

generate = Button(text="Generate password", width=13, font=("", 8, "normal"))
generate.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
