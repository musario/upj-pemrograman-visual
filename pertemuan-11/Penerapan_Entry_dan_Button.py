from tkinter import *
import tkinter.ttk as ttk
from tkinter import simpledialog

root = Tk()
root.geometry('400x200')

def cetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width=28); entry1.pack()
Button(root, text="Cetak Data", command=cetakData).pack()

root.mainloop()
