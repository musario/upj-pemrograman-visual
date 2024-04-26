import tkinter as tk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()

middleFrame = tk.Frame(root)
middleFrame.pack()

bottomFrame = tk.Frame(root)
bottomFrame.pack()

buttonR1 = tk.Button(topFrame, text='Top Red', fg='red')
buttonB1 = tk.Button(topFrame, text='Top Blue', fg='blue')
buttonG1 = tk.Button(topFrame, text='Top Green', fg='green')

buttonR1.pack(side='top')
buttonB1.pack(side='top')
buttonG1.pack(side='top', pady=(0, 20))

buttonR2 = tk.Button(middleFrame, text='Middle Red', fg='red')
buttonB2 = tk.Button(middleFrame, text='Middle Blue', fg='blue')
buttonG2 = tk.Button(middleFrame, text='Middle Green', fg='green')

buttonR2.pack(side='left', pady=(0, 20))
buttonB2.pack(side='left', pady=(0, 20))
buttonG2.pack(side='left', pady=(0, 20))

buttonR3 = tk.Button(bottomFrame, text="Bottom Red", fg='red')
buttonB3 = tk.Button(bottomFrame, text="Bottom Blue", fg='blue')
buttonG3 = tk.Button(bottomFrame, text="Bottom Green", fg='green')

buttonR3.pack(side='bottom')
buttonB3.pack(side='bottom')
buttonG3.pack(side='bottom')

root.mainloop()
