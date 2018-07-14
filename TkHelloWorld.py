import tkinter as tk
from tkinter import *
mw = tk.Tk()
mw.title("Hello World!")
mw.geometry("500x500")

redbutton = Button(mw, text="Red", fg="red")
redbutton.pack( side = LEFT)
mw.mainloop()
