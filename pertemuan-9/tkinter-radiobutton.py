import tkinter as tk 

root = tk.Tk()

radioButtonVar = tk.IntVar()
label = tk.Label(root)
label.pack()

def sel():
    selection = "Kamu telah memilih Opsi " + str(radioButtonVar.get())
    label.config(text=selection)

R1 = tk.Radiobutton(root, text="Opsi 1", variable=radioButtonVar, value=1, command=sel)
R1.pack(anchor='w')
R2 = tk.Radiobutton(root, text="Opsi 2", variable=radioButtonVar, value=2, command=sel)
R2.pack(anchor='w')
R3 = tk.Radiobutton(root, text="Opsi 3", variable=radioButtonVar, value=3, command=sel)
R3.pack(anchor='w')

root.mainloop()
