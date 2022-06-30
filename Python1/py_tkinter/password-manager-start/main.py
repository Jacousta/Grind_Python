from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char


def password_generate():
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_write():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="OOPS", message="Fill all details")
    else:
        is_ok = messagebox.askyesno(title=website_input.get(),
                                    message=f"These are the details you enter \n EMAIL:{email_input.get()}\nPASSWORD:{password_input.get()}:")
        new_data = {
            website_input.get(): {
                "email": email_input.get(),
                "password": password_input.get(),

            }
        }
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    data = new_data
                    json.dump(data, data_file, indent=4)
            else:
                data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)
        else:
            website_input.delete(0, END)
            password_input.delete(0, END)


def data_reader():
    with open("data.json", "r") as read_file:
        loaded_file = json.load(read_file)
        if website_input.get() in loaded_file:
            messagebox.showinfo(title="Your info", message=f"Email: {loaded_file[website_input.get()]['email']}\n" 
                                                           f" Password: {loaded_file[website_input.get()]['password']}")
        else:
            messagebox.showinfo(message="ERROR 69")
        # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=2, column=2)

website_label = Label(text="Website:")
website_label.grid(row=3, column=1)

website_input = Entry(window, width=40)
website_input.focus()
website_input.grid(row=3, column=2, columnspan=3)

email_label = Label(text="Email/Username:")
email_label.grid(row=4, column=1)

email_input = Entry(window, width=40)
email_input.insert(0, "cpunia_be21@thapar.edu")
email_input.grid(row=4, column=2, columnspan=3)

password_label = Label(text="Password")
password_label.grid(row=5, column=1)

password_input = Entry(window, width=25)
password_input.grid(row=5, column=2)

password_button = Button(text="Generate Password", width=11, command=password_generate)
password_button.grid(row=5, column=3)

add_button = Button(text="Add", width=38, command=data_write)
add_button.grid(row=6, column=2, columnspan=3)

search_button = Button(text="Search", width=11,command=data_reader)
search_button.grid(row=3, column=3)

window.mainloop()
