import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
frame = Frame(root)

def change_i():
    if folder_btn.image == icon:
        #start_recording()

        folder_btn.config(image=icon2)
        folder_btn.image = icon2
    else:
        #stop_recording()

        folder_btn.config(image=icon)
        folder_btn.image = icon

icon = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-file-folder-48.png') # https://icons8.com/icons/set/file-folder
icon2 = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-open-file-folder-48.png') # https://icons8.com/icons/set/file-folder

#folder_btn = tk.Button(root, image=icon, width=70,height=60,relief=FLAT ,command=change_i )
#folder_btn.image = icon
#folder_btn.grid(row=0, column=1)

rows = 10
columns = 5
#example values
for x in range(rows): #rows
    for y in range(columns): #columns
        folder_btn = Button(root, image=icon, width=70,height=60,relief=FLAT ,command=change_i,)
        folder_btn.image = icon
        folder_btn.grid(column=x, row=y, sticky="news")

frame.columnconfigure(tuple(range(rows)), weight=1)
frame.rowconfigure(tuple(range(columns)), weight=1)
root.mainloop()