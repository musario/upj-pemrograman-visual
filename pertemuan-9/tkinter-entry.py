import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")

def showEntry():
    nameLabel.config(text="Halo " + entry.get() + " 👋!")

label = tk.Label(frame, text="Username: ")
entry = tk.Entry(frame, bd=5)
button = tk.Button(bottomFrame, text="Submit", command=showEntry)
nameLabel = tk.Message(bottomFrame, text="")

label.pack(side='left')
entry.pack(side='left')
button.pack(side='top')
nameLabel.pack(side='bottom')

root.mainloop()
