import tkinter as tk

root = tk.Tk()

checkvar1 = tk.IntVar()
checkvar2 = tk.IntVar()
C1 = tk.Checkbutton(root, text="Volleyball", variable=checkvar1, onvalue=1, offvalue=0, height=1, width=20)
C2 = tk.Checkbutton(root, text="Badminton", variable=checkvar2, onvalue=1, offvalue=0, height=5, width=20)
C1.pack(side="left")
C2.pack(side="right")

root.mainloop()
