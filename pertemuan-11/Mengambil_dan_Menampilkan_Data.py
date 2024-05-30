from tkinter import *

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=1, column=0)

        frame4 = Frame(frame1)
        frame4.grid(row=2, column=1)

        FirstNum = StringVar()
        SecondNum = StringVar()
        Hasil = StringVar()

        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=Hasil)
        self.txtHasil.grid(row=2, column=1)

        def JUMLAHKAN():
            pertama = float(FirstNum.get())
            kedua = float(SecondNum.get())
            hasil = pertama + kedua
            Hasil.set(hasil)

        def RESET():
            FirstNum.set('0')
            SecondNum.set('0')
            Hasil.set('0')

        def EXIT():
            self.root.destroy()

        self.btnJumlahkan = Button(frame3, text='Jumlahkan', command=JUMLAHKAN).grid(row=0, column=0)
        self.btnReset = Button(frame3, text='Reset', command=RESET).grid(row=0, column=1)
        self.btnKeluar = Button(frame3, text='Keluar', command=EXIT).grid(row=0, column=2)
        
if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
