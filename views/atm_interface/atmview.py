from tkinter import *

class ATMWindow:

    def __init__(self, master):

        self.master = master

        # set main window attributes such as title, geometry etc
        self.master.title('Name Management Window')
        # self.master.geometry('1000x1000')
        # self.master.config(background='LightGrey')

        # set up menus if there are any
        #
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)

        # define frames if needed
        #
        self.top_frame = Frame(self.master, width=600, height=400)
        self.mid_frame = Frame(self.master, width=600, height=100)
        self.bot_frame = Frame(self.master, width=600, height=100)

        self.top_frame.grid(row=0, column=0)
        self.mid_frame.grid(row=1, column=0)
        self.bot_frame.grid(row=2, column=0)

        # define/create widgets
        # self.account_info = Label(self.top_frame, text='Account Info')
        self.account_number = Label(self.top_frame, text='')
        self.account_type = Label(self.top_frame, text='')
        self.account_balance = Label(self.top_frame, text='')

        self.withdraw_button = Button(self.mid_frame, text='Withdraw')
        self.deposit_button = Button(self.mid_frame, text='Deposit')
        self.info_button = Button(self.bot_frame, text='Print Receipt')
        self.quit_button = Button(self.bot_frame, text='Quit')

        # top frame
        # self.account_info.grid(row=0, column=0, sticky=E, padx=620)
        self.account_number.grid(row=0, column=0, sticky=E, padx=620)
        self.account_type.grid(row=1, column=0, sticky=E, padx=620)
        self.account_balance.grid(row=2, column=0, sticky=E, padx=620)

        # mid frame
        self.withdraw_button.grid(row=0, column=0, sticky=W, padx=300, pady=50)
        self.deposit_button.grid(row=0, column=1, sticky=E, padx=300, pady=50)

        # bot frame
        self.info_button.grid(row=0, column=0, sticky=W, padx=300, pady=50)
        self.quit_button.grid(row=0, column=1, sticky=E, padx=300, pady=50)

