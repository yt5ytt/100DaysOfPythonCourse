from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    pass_word = pass_letters + pass_numbers + pass_symbols
    random.shuffle(pass_word)

    lozinka = "".join(pass_word)

    pass_input.delete(0, END)
    pass_input.insert(0, lozinka)
    pyperclip.copy(lozinka)


def search():
    website_data = website_input.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oooops!", message=f"There isn't any data for {website_data} in db")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oooops!", message=f"There isn't any data for {website_data} in db")
    else:
        if website_data in data:
            db_email = data[website_data]["email"]
            db_pass = data[website_data]["password"]
            messagebox.showinfo(title="Your login data for {website_data}", message=f'Your login email: {db_email}\n'
                                                                                    f'Your login password: {db_pass}')
        else:
            messagebox.showinfo(title="Oooops!", message=f"There isn't any data for {website_data} in db")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_data = website_input.get()
    email_data = email_input.get()
    pass_data = pass_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": pass_data,
        }
    }

    message_ok = f'''
Website: {website_data}
Email: {email_data}
Password: {pass_data}
Is this right data?
    '''

    if not website_data or not pass_data:
        messagebox.showerror(title="Oooops", message="Some of your fields are empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=message_ok)    

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # Read from json
                    data = json.load(f)

            except FileNotFoundError:
                with open("data.json", "w") as f:
                    # Saving updated data
                    json.dump(new_data, f, indent=4)

            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as f:
                    # Saving updated data
                    json.dump(new_data, f, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as f:
                    # Saving updated data
                    json.dump(data, f, indent=4)

            finally:
                website_input.delete(0, END)
                pass_input.delete(0, END)

            messagebox.showinfo(title=website_data, message=f"Website: {website_data}\nPassword: {pass_data}\n"
                                                            f"has added to your database.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:", height=2)
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password", height=2)
password.grid(column=0, row=3)

website_input = Entry(width=39)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "yt5ytt@gmail.com")

pass_input = Entry(width=39)
pass_input.grid(column=1, row=3)

search_button = Button(text="Search", width=8, command=search)
search_button.grid(column=2, row=1)

generate = Button(text="Generate", width=8, font=("Courier", 8, "normal"), command=generate_password)
generate.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
