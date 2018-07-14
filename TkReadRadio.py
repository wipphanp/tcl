import tkinter as tk

def showvalue():
    print ("I am this", radioval.get(), radioint.get())

def changevalue():
    if radioval.get() == 'M':
        radioval.set('F')
    else :
        radioval.set('M')


mw = tk.Tk()
mw.title("Showing a few widgets!")
mw.geometry("500x500")
button = tk.Button(mw,text = "I am a button", command=showvalue)
button.pack()

radioval = tk.StringVar()
#radioval.set("F")

radio1 = tk.Radiobutton(mw,text="Male", variable = radioval, value="M")
radio1.pack()
radio2 = tk.Radiobutton(mw,text="Female", variable = radioval, value="F")
radio2.pack()

#button = tk.Button(mw,text = "change value", command=changevalue)
#button.pack()

radioint = tk.IntVar()
radioint.set(0)

radio3 = tk.Radiobutton(mw,text="Vegetarian", variable = radioint, value=0)
radio3.pack()
radio4 = tk.Radiobutton(mw,text="Non-Vegetarian", variable = radioint, value=1)
radio4.pack()


mw.mainloop()