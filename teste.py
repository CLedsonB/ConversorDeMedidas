from tkinter import *
from tkinter.ttk import *

root = Tk()

Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(pady = 10)

photo = PhotoImage(file = r"img/peso.png")

photoimage = photo.subsample(3, 3)
b1 = Button(root, text="Peso", image=photoimage, coumpond=LEFT)
b1.grid(row=0, column=0, sticky=NSEW)

mainloop() 