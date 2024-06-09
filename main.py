import random as rd
from ttkbootstrap import *
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ------- GENERATE PASSWORD -------
#Password Generator Project

def generate_password():
    try:
        password_entry.delete(0, END)
    except:
        pass
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ------- SAVE PASSWORD ------
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showinfo('Oops..', "Please Fill out all the details.")
    else:
        is_ok = messagebox.askokcancel('Confirmation',
                                       message=f'Confirm the details.'
                                               f'\nWebsite: {website_entry.get()}'
                                               f'\nEmail: {email_entry.get()}'
                                               f'\nPassword: {password_entry.get()}')
        if is_ok:
            with open('savePassword.txt', 'a') as file:
                file.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


# ----- GUI -------

screen = Window()
screen.title('Password Manager')
screen.config(padx=20, pady=20)

# ------> Image Processing
canvas = Canvas(screen, width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# -------> Labels
website_label = Label(screen, text='Website:')
website_label.grid(row=1, column=0, pady=3)
email_label = Label(screen, text='Email/Username:')
email_label.grid(row=2, column=0, pady=3)
password_label = Label(screen, text='Password:')
password_label.grid(row=3, column=0, pady=3)

# -------> Entry
website_entry = Entry(screen, width=50)
website_entry.grid(row=1, column=1, columnspan=2, pady=3)
email_entry = Entry(screen, width=50)
email_entry.grid(row=2, column=1, columnspan=2, pady=3)
email_entry.insert(0, 'ranahimanshu335@gmail.com')
password_entry = Entry(screen, width=32)
password_entry.grid(row=3, column=1, pady=3)

# --------> Buttons
generate_password = Button(screen, text='Generate Password', command=generate_password)
generate_password.grid(row=3, column=2, pady=3)
add = Button(screen, text='Add', width=43, command=save)
add.grid(row=4, column=1, columnspan=2, pady=3)
screen.mainloop()
