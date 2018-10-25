from tkinter import *
import sys

def close():
    exit()

def calc():
    print("cunt")

MW = Tk()
MW.title("Pay Calculator")

MW.geometry("640x480")
MW.resizable(0, 0)

menubar = Menu(MW)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Calc", command=calc)
filemenu.add_command(label="Close", command=close)
menubar.add_cascade(label="File", menu=filemenu)

lbl = Label(MW, text ="Dog")
ent = Entry(MW)
btn = Button(MW, text ="Button")

lbl.pack()
ent.pack()
btn.pack()

MW.config(menu=menubar)
MW.mainloop()
