from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('clock by JZM.dev')

def time():
    string = strftime('%H:%M:%S')
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root, font=('ds-digital', 150), background= 'black', foreground= 'white')
Label.pack(anchor='center')
time()

mainloop()