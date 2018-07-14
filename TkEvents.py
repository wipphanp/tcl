import tkinter as tk
def someaction():
    print ("Yayy!! Somebody clicked me!")
#    tkm.showinfo("Click action", "Yay!! Somebody clicked me!")

def sayHello(event):
    print (type(event))
    print (dir(event))
    print ("Hello There!")

def byeBye(event):
    print ("Bye Bye")
    mw.destroy()

mw = tk.Tk()
mw.title("Hello World!")
mw.geometry("500x500")
b1 = tk.Button(mw,text="OK", command=someaction)
b1.pack(fill=tk.X)
b2 = tk.Button(mw,text="QUIT", command=mw.destroy)
b2.pack(fill=tk.X)

b3 = tk.Button(mw, text="Say Hello!")
b3.pack(fill=tk.X)
b3.bind('<Button-1>', sayHello)
b3.bind('<Button-3>', byeBye)

mw.mainloop()