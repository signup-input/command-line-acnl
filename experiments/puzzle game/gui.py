import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
window = tk.Tk()
X = 500
Y = 350
window.geometry(f"{X}x{Y}")
#Get the current screen width and height
#screen_width = window.winfo_screenwidth()
#screen_height = window.winfo_screenheight()

def change_i():
    if folder_btn.image == icon:
        #start_recording()

        folder_btn.config(image=icon2)
        folder_btn.image = icon2
    else:
        #stop_recording()

        folder_btn.config(image=icon)
        folder_btn.image = icon

def change_i2():
    if folder_btn2.image == icon:
        #start_recording()

        folder_btn2.config(image=icon2)
        folder_btn2.image = icon2
    else:
        #stop_recording()

        folder_btn2.config(image=icon)
        folder_btn2.image = icon


icon = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-file-folder-48.png') # https://icons8.com/icons/set/file-folder
icon2 = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-open-file-folder-48.png') # https://icons8.com/icons/set/file-folder

#!todo: make folder_btn an object
folder_btn = tk.Button(window, image=icon, width=70,height=60,relief=FLAT ,command=change_i )
folder_btn.image = icon
folder_btn.grid(row=0, column=1)

folder_btn2 = tk.Button(window, image=icon, width=70,height=60,relief=FLAT ,command=change_i2 )
folder_btn2.image = icon
folder_btn2.grid(row=0, column=2)

window.mainloop()