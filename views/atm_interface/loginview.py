from tkinter import *

class LoginWindow:

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
        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)

        self.top_frame.grid(row=0, column=0)
        self.mid_frame.grid(row=1, column=0)
        self.bot_frame.grid(row=2, column=0)

        # define/create widgets
        Label(self.top_frame, text="Card Number: ").grid(row=0, column=0)
        self.username = Entry(self.top_frame)
        self.username.grid(row=0, column=1)
        Label(self.mid_frame, text="PIN: ").grid(row=0, column=0)
        self.password = Entry(self.mid_frame, show="*")
        self.password.grid(row=0, column=1)

        self.submit_button = Button(self.bot_frame, text='Login')
        self.submit_button.grid(row=0, column=0)




