from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side='right')

mylist = Listbox(root, yscrollcommand = scrollbar.set)
for line in range(20):
    mylist.insert(END, "This is line number " + str(line))

mylist.pack(side = 'left', fill='x', background='blue')
scrollbar.config(command = mylist.yview )

label = Label(root, text="This is a label", background='yellow')
label.pack(fill='x')

mainloop()
