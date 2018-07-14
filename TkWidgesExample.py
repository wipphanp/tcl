import tkinter as tk
mw = tk.Tk()
mw.title("Showing a few widgets!")

label = tk.Label(mw,text = "I am a label!")
label.pack()
button = tk.Button(mw,text = "I am a button")
button.pack()

radio1 = tk.Radiobutton(mw,text="Male")
radio1.pack()
radio2 = tk.Radiobutton(mw,text="Female")
radio2.pack()

check1 = tk.Checkbutton(mw,text="Veg" )
check1.pack()
check2 = tk.Checkbutton(mw,text="Non Veg" )
check2.pack()
check3 = tk.Checkbutton(mw,text="Vegan" )
check3.pack()

entry1 = tk.Entry(mw)
entry1.pack()
entry2 = tk.Entry(mw)
entry2.pack()

textw = tk.Text(mw, height = 2, width = 100)
textw.pack()

mw.mainloop()