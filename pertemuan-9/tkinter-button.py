import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def sayHello():
    msg = tk.messagebox.showinfo("Info", "Halo Dunia!")

label = tk.Label(root, text="Button in Tkinter!", font=("Poppins", 12))
button = tk.Button(root, text="Click me!", command=sayHello)

label.pack()
button.pack()

root.mainloop()
