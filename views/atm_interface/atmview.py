from tkinter import *


class ATMWindow:

    def __init__(self, master):

        self.master = master


        # set main window attributes such as title, geometry etc
        self.master.title('Name Management Window')
        # self.master.geometry('1000x1000')
        # self.master.config(background='LightGrey')

        # set up menus if there are any

        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)

        # define frames if needed

        self.left_frame = Frame(self.master, width=600, height=400)
        self.mid_frame = Frame(self.master, width=600, height=100)
        self.right_frame = Frame(self.master, width=600, height=100)

        self.left_frame.grid(row=1, column=0)
        self.mid_frame.grid(row=1, column=1)
        self.right_frame.grid(row=1, column=2)

        # define/create widgets

        # welcome screen
        self.welcome_screen = Label(self.mid_frame,
                                    text='Which account would you like to access?')
        self._select_ch_BUTTON = Button(self.left_frame, text='Chequing', width=10, height=5)
        self._select_sa_BUTTON = Button(self.right_frame, text='Savings', width=10, height=5)

        # mid frame
        self.account_name = Label(self.mid_frame, text='')
        self.account_type = Label(self.mid_frame, text='')
        self.account_balance = Label(self.mid_frame, text='')

        self.prompt = Label(self.mid_frame, text='')
        self.prompt.grid(row=0, column=0)

        self.username_label = Label(self.mid_frame, text="Card Number: ")
        self.username_label.grid(row=1, column=0)
        self.username = Entry(self.mid_frame)
        self.username.grid(row=2, column=0, padx=0, pady=50)
        self.PIN_label = Label(self.mid_frame, text="PIN: ")
        self.PIN_label.grid(row=3, column=0)
        self.password = Entry(self.mid_frame, show="*")
        self.password.grid(row=4, column=0, padx=0, pady=50)
        self.submit_button = Button(self.mid_frame, text='Login')
        self.submit_button.grid(row=5, column=0, padx=0, pady=50)


        self.amount_entry = Entry(self.mid_frame)

        # left frame
        self.withdraw_button = Button(self.left_frame, text='Withdraw', width=10, height=5)
        self.deposit_button = Button(self.left_frame, text='Deposit', width=10, height=5)
        self.back_button = Button(self.left_frame, text='Back', width=10, height=5)

        # right frame
        self.switch_button = Button(self.right_frame, text='Switch\nAccount', width=10, height=5)
        self.quit_button = Button(self.right_frame, text='Quit', width=10, height=5)
        self.confirm_button = Button(self.right_frame, text='Confirm', width=10, height=5)

        # WD Buttons
        self.wdBack = Button(self.left_frame, text='Back', width=10, height=5)
        self.wd20 = Button(self.left_frame, text='$20', width=10, height=5)
        self.wd40 = Button(self.left_frame, text='$40', width=10, height=5)

        self.wd60 = Button(self.right_frame, text='$60', width=10, height=5)
        self.wd80 = Button(self.right_frame, text='$80', width=10, height=5)
        self.wd100 = Button(self.right_frame, text='$100', width=10, height=5)

        # mid frame place

        # self.welcome_screen.grid(row=0, column=0, padx=200)
        # self.account_number.grid(row=0, column=0, sticky=E, padx=400)
        # self.account_type.grid(row=1, column=0, sticky=E, padx=400)
        # self.account_balance.grid(row=2, column=0, sticky=E, padx=400)

        # left frame place

        # self._select_ch_BUTTON.grid(row=0, column=0, sticky=W, padx=100, pady=100)
        # self.withdraw_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
        # self.deposit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)

        # right frame place

        # self._select_sa_BUTTON.grid(row=0, column=0, sticky=E, padx=100, pady=100)
        # self.info_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
        # self.quit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)

