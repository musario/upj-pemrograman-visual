from tkinter import *
import tkinter
top = Tk()
top.geometry('400x200')
mb= Menubutton ( top, text="Gender", relief=RAISED )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton (label="Laki-laki", variable=mayoVar)
mb.menu.add_checkbutton (label="Perempuan", variable=ketchVar)
mb.pack()
top.mainloop()
