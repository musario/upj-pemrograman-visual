from tkinter import *

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Apple")
Lb1.insert(2, "Banana")
Lb1.insert(3, "Grapes")
Lb1.insert(4, "Orange")
Lb1.insert(5, "Strawberry")
Lb1.insert(6, "Cherry")

Lb1.pack()
top.mainloop()
