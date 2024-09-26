from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as data:
        data.write(f"{field1.get()} | {field2.get()} | {field3.get()}\n")
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
generate = Button(text="Generate Password")
generate.grid(column=2, row=3)

btn = Button(text="Add", command=save)
btn.config(width=45)
btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
