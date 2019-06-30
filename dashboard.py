from tkinter import *
import income.add_income


class DashboardWindow:
    def __init__(self):
        self.win = Tk()

        # reset the window and background color
        self.canvas = Canvas(self.win, width=1000, height=600, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 1000 / 2)
        y = int(height / 2 - 600 / 2)
        str1 = "1000x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("WELCOME | Home Window | ADMINISTRATOR")

    def add_menu(self):
        #create main menu
        self.mainmenu = Menu(self.win)
        self.win.config(menu=self.mainmenu)

        #create first menu list
        self.income = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Income", menu=self.income)

        self.income.add_command(label="Add Income Source", command=self.add_income)
        self.income.add_command(label="Manage Income Source")

        #create second menu
        self.expense = Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Expense",menu=self.expense)

        self.expense.add_command(label="Add Expense")
        self.expense.add_command(label="Manage Expense")
        self.expense.add_separator()
        self.expense.add_command(label="Quit",command=self.win.quit)

    def add_frame(self):

        self.img = PhotoImage(file='./images/dashboard.png')
        self.label = Label(self.win, image=self.img)
        self.label.place(x=0, y=0)
        self.win.mainloop()

    def add_income(self):
        x = income.add_income.IncomeWindow()
        x.add_frame()


if __name__ == "__main__":
    x = DashboardWindow()
    x.add_menu()
    x.add_frame()