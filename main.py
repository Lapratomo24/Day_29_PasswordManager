from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_numbers = [(random.choice(numbers)) for number in range(nr_numbers)]
    password_symbols = [(random.choice(symbols)) for symbol in range(nr_symbols)]

    pw = password_letters + password_numbers + password_symbols

    random.shuffle(pw)
    passwords = "".join(pw)
    field3.delete(0, END)
    field3.insert(0, f"{passwords}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = field1.get()
    user = field2.get()
    passw = field3.get()

    if len(site) == 0 or len(user) == 0 or len(passw) == 0:
        messagebox.showinfo(message="Please fill out all the fields.")
    else:
        select = messagebox.askokcancel(title=site, message=f" {user}\n {passw}\n Proceed with save?")

        if select:
            with open("data.txt", "a") as data:
                data.write(f"{site} | {user} | {passw}\n")
                field1.delete(0, END)
                field2.delete(0, END)
                field3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website = Label(text="Website:", fg="red")
website.grid(column=0, row=1)
field1 = Entry(width=52)
field1.insert(END, string="")
field1.grid(column=1, row=1, columnspan=2)
field1.focus()

email = Label(text="Email/Username:", fg="red")
email.grid(column=0, row=2)
field2 = Entry(width=52)
field2.insert(END, string="example@outlook.com")
field2.grid(column=1, row=2, columnspan=2)
field2.insert(0, "")

password = Label(text="Password:", fg="red")
password.grid(column=0, row=3)
field3 = Entry(width=34)
field3.insert(END, string="")
field3.grid(column=1, row=3)
generate = Button(text="Generate Password", command=generate_pass)
generate.grid(column=2, row=3)

btn = Button(text="Add", command=save)
btn.config(width=45)
btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
