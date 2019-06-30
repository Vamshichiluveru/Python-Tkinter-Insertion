from tkinter import *
import db.db


class IncomeWindow:

    def __init__(self):
        self.win = Tk()
        canvas = Canvas(self.win, width=600, height=500, bg='white')
        canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()

        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)

        str1 = "600x400+"+str(x)+"+"+ str(y)
        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)
        self.win.title("Add Income | Administrator")


    def add_frame(self):

        self.frame = Frame(self.win, height=350, width=450)
        self.frame.place(x=80, y=20)

        x, y = 70, 20

        self.label = Label(self.frame, text="Add Income Source")
        self.label.config(font=('Courier', 20, 'bold'))
        self.label.place(x = x + 30, y = y + 50)

        self.income = Label(self.frame, text='Enter Source')
        self.income.config(font=('Courier', 12, 'bold'))
        self.income.place(x = 40, y = y + 100)

        self.inc = Entry(self.frame, font='Courier 12')
        self.inc.place(x=220, y = y + 100)

        self.income = Label(self.frame, text='Enter Description')
        self.income.config(font=('Courier', 12, 'bold'))
        self.income.place(x=40, y=y + 130)

        self.des = Entry(self.frame, font='Courier 12')
        self.des.place(x=220, y=y + 130)

        self.button = Button(self.frame, text='SUBMIT', font='Courier 12 bold',
                             command=self.add_income)
        self.button.place(x=170, y = y + 180)

        self.labelmsg = Label(self.frame, text='')
        self.labelmsg.config(font=('Courier', 12, 'bold'))
        self.labelmsg.place(x = 120, y = y + 210)

        self.win.mainloop()

    def add_income(self):
        data = (
            self.inc.get(),
            self.des.get()
        )

        if self.inc.get() == '':
            self.labelmsg.config(fg='red')
            self.labelmsg.config(text='Please Enter Income')

        elif self.des.get() == '':
            self.labelmsg.config(fg='red')
            self.labelmsg.config(text='Please Enter Description')

        else:
            res = db.db.add_income(data)
            if res:
                self.labelmsg.config(fg='green')
                self.labelmsg.config(text='Data Added Successfully')
                # code to clear the data from input box after submission
                self.inc.delete(0, 'end')
                self.des.delete(0, 'end')
            else:
                self.labelmsg.config(fg='red')
                self.labelmsg.config(text='Alert! Please try again')

