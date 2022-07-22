import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
root = tk.Tk()
def change_i():
    if sound_btn.image == icon:
        #start_recording()

        sound_btn.config(image=icon2)
        sound_btn.image = icon2
    else:
        #stop_recording()

        sound_btn.config(image=icon)
        sound_btn.image = icon

icon = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-file-folder-48.png') # https://icons8.com/icons/set/file-folder
icon2 = PhotoImage(file='C:/Users/AAoGr/Downloads/command-line-acnl/experiments/puzzle game/icons/icons8-open-file-folder-48.png') # https://icons8.com/icons/set/file-folder

sound_btn = tk.Button(root, image=icon, width=70,height=60,relief=FLAT ,command=change_i )
sound_btn.image = icon
sound_btn.grid(row=0, column=1)
root.mainloop()