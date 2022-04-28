from tkinter import *
from tkinter.ttk import *

# import time
from time import strftime

# create window and add title
root = Tk()
root.title('Clock')

# Define function gets current time
def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)


# set font, bg, fg for label and pack the label.
label = Label(root, font=('ds-digital', 80),background ='green', foreground='black')
label.pack(anchor='center')
time()

# create a mainloop which keeps running
mainloop()
