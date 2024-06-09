from tkinter import *

screen = Tk()

red = Label(screen, bg='red', width=20,height=5)
red.grid(row=0, column=0)

green = Label(screen, bg='green', width=20, height=5)
green.grid(row=1, column=1)

blue = Label(screen, bg='blue', width=40, height=5)
blue.grid(row=2, column=0, columnspan=2)

screen.mainloop()
