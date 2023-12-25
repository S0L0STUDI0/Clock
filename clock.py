#   _  _    _____       _       _____ _             _ _       
# _| || |_ / ____|     | |     / ____| |           | (_)      
#|_  __  _| (___   ___ | | ___| (___ | |_ _   _  __| |_  ___  
# _| || |_ \___ \ / _ \| |/ _ \\___ \| __| | | |/ _` | |/ _ \ 
#|_  __  _|____) | (_) | | (_) |___) | |_| |_| | (_| | | (_) |
#  |_||_| |_____/ \___/|_|\___/_____/ \__|\__,_|\__,_|_|\___/  

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('clock by #SoloStudio')

def time():
    string = strftime('%H:%M:%S')
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root, font=('ds-digital', 150), background= 'black', foreground= 'white')
Label.pack(anchor='center')
time()

mainloop()

#Developed in 2022 - SoloStudio
#SoloStudio
