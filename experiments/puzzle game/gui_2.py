from tkinter import *

root = Tk()
frame = Frame(root)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.grid(row=0, column=0, sticky="news")
grid = Frame(frame)
grid.grid(sticky="news", column=0, row=7, columnspan=2)
frame.rowconfigure(7, weight=1)
frame.columnconfigure(0, weight=1)

rows = 10
columns = 5
#example values
for x in range(rows): #rows
    for y in range(columns): #columns
        btn = Button(frame)
        btn.grid(column=x, row=y, sticky="news")

frame.columnconfigure(tuple(range(rows)), weight=1)
frame.rowconfigure(tuple(range(columns)), weight=1)

root.mainloop()

