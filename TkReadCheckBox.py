#import Tkinter as tk
import tkinter as tk

def showvalue():
    currval = map(lambda x:x.get(), valcb)
    print ((mw.winfo_height(), mw.winfo_width()))
    print (list(currval))

mw = tk.Tk()
mw.title("Showing a few widgets!")
mw.geometry("500x500")
button = tk.Button(mw,text = "I am a button", command=showvalue).pack()

valcb = [tk.IntVar() for i in range(3)]
texts = ['Veg', 'Non Veg', 'Vegan']

for v,t in zip(valcb,texts):
    c = tk.Checkbutton(mw,text=t, variable=v )
    c.pack()


#check1 = tk.Checkbutton(mw,text="Veg", variable=valcb[0] )
#check1.pack()
#check2 = tk.Checkbutton(mw,text="Non Veg", variable=valcb[1] )
#check2.pack()
#check3 = tk.Checkbutton(mw,text="Vegan", variable=valcb[2] )
#check3.pack()
mw.mainloop()


