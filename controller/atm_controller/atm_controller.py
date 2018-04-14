from tkinter import *
from tkinter import messagebox

import os
from model.chequing import *
from model.savings import *
from model.transactions.transaction_log import TransactionLog
from model.teller_db import Teller_DB
from model.login_db import Login_DB
from model.account_db import Account_DB
from views.atm_interface.atmview import ATMWindow
from views.atm_interface.loginview import LoginWindow

LOGIN_FLAG = 0
LOG_ACCNUM = 0
ACC_DISPLAYED = ''
ACC_DB_FILE = 'account_info.csv'

class ATMController:

    def __init__(self, master):
        self._login_db = Login_DB()
        print(self._login_db._logindb)
        self._acc_db = Account_DB()
        print(self._acc_db._accountdb)


        # bindings and master creation
        self.master = master
        self.atm_gui = ATMWindow(self.master)
        self.atm_gui.submit_button.config(command=self._login)
        # self.atm_gui._select_sa_BUTTON.config(command=self.display_sa_info)
        # self.atm_gui._select_ch_BUTTON.config(command=self.display_ch_info)

        # transactions
        self.transactions = []
        self.wd_pend = 0
        self.dep_pend = 0

        self.atm_gui.file_menu.add_command(label='Quit', command=self.master.quit)


    def _login(self):
        user_info = str(self.atm_gui.username.get())
        pass_info = str(self.atm_gui.password.get())


        if (user_info in self._login_db._logindb) and (self._login_db._logindb[user_info] == pass_info):
            self.atm_gui.username.delete(0, 'end')
            self.atm_gui.password.delete(0, 'end')
            global LOG_ACCNUM
            LOG_ACCNUM = user_info
            self.transition_welcome()

        else:
            self.atm_gui.username.delete(0, 'end')
            self.atm_gui.password.delete(0, 'end')
            self.atm_gui.prompt['text'] = 'Invalid Card Number or Password. Please Try Again!'
            self.atm_gui.prompt.grid(row=0, column=0)

    def transition_welcome(self):
        self.atm_gui.prompt.grid_remove()
        self.atm_gui.username_label.grid_remove()
        self.atm_gui.username.grid_remove()
        self.atm_gui.PIN_label.grid_remove()
        self.atm_gui.password.grid_remove()
        self.atm_gui.submit_button.grid_remove()

        self.atm_gui.welcome_screen.grid(row=0, column=0, padx=200)
        self.atm_gui._select_ch_BUTTON.grid(row=0, column=0, sticky=W, padx=100, pady=100)
        self.atm_gui._select_sa_BUTTON.grid(row=0, column=0, sticky=E, padx=100, pady=100)

        self.atm_gui._select_sa_BUTTON.config(command=self.display_sa_info)
        self.atm_gui._select_ch_BUTTON.config(command=self.display_ch_info)

    def display_ch_info(self):
        acc = '\n'
        balance = ''

        for items in self._acc_db._accountdb[LOG_ACCNUM]:
            if items.acc_type == 'Chequing':
                acc += items.acc_type
                balance += str(items.acc_bal)
                self.atm_gui.welcome_screen.grid_remove()
                self.atm_gui._select_ch_BUTTON.grid_remove()
                self.atm_gui._select_sa_BUTTON.grid_remove()

                self.atm_gui.account_name['text'] = 'Welcome Back, {}!'.format(self._acc_db._accountdb[LOG_ACCNUM][0].acc_name)
                self.atm_gui.account_type['text'] = 'Account Type: {}'.format(acc)
                self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(balance)

                self.atm_gui.account_name.grid(row=0, column=0, padx=200)
                self.atm_gui.account_type.grid(row=1, column=0, padx=200)
                self.atm_gui.account_balance.grid(row=2, column=0, padx=200)

                self.atm_gui.withdraw_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
                self.atm_gui.deposit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)
                self.atm_gui.switch_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
                self.atm_gui.quit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)

                self.main_sreen_binds()
                global ACC_DISPLAYED
                ACC_DISPLAYED = 'CH'

            else:
                self.atm_gui.welcome_screen['text']='This account does not have a Chequing Account!'
                self.atm_gui.welcome_screen.grid(row=0, column=0, padx=200)


    def display_sa_info(self):
        acc = '\n'
        balance = ''

        for items in self._acc_db._accountdb[LOG_ACCNUM]:
            if items.acc_type == 'Savings':
                acc += items.acc_type
                balance += str(items.acc_bal)
                self.atm_gui.welcome_screen.grid_remove()
                self.atm_gui._select_ch_BUTTON.grid_remove()
                self.atm_gui._select_sa_BUTTON.grid_remove()

                self.atm_gui.account_name['text'] = 'Welcome Back, {}!'.format(self._acc_db._accountdb[LOG_ACCNUM][0].acc_name)
                self.atm_gui.account_type['text'] = 'Account Type: {}'.format(acc)
                self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(balance)

                self.atm_gui.account_name.grid(row=0, column=0, padx=200)
                self.atm_gui.account_type.grid(row=1, column=0, padx=200)
                self.atm_gui.account_balance.grid(row=2, column=0, padx=200)

                self.atm_gui.withdraw_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
                self.atm_gui.deposit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)
                self.atm_gui.switch_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
                self.atm_gui.quit_button.grid(row=1, column=0, sticky=E, padx=100, pady=50)

                self.main_sreen_binds()
                global ACC_DISPLAYED
                ACC_DISPLAYED = 'SA'

            else:
                self.atm_gui.welcome_screen['text'] = 'This account does not have a Savings Account!'
                self.atm_gui.welcome_screen.grid(row=0, column=0, padx=200)

    def main_sreen_binds(self):
        self.atm_gui.withdraw_button.config(command=self.withdraw_screen)
        self.atm_gui.deposit_button.config(command=self.deposit_screen)
        self.atm_gui.switch_button.config(command=self._switch)
        self.atm_gui.quit_button.config(command=self._quit)

    def withdraw_screen(self):
        self.atm_gui.account_name.grid_remove()
        self.atm_gui.account_type.grid_remove()
        self.atm_gui.account_balance.grid_remove()
        self.atm_gui.withdraw_button.grid_remove()
        self.atm_gui.deposit_button.grid_remove()
        self.atm_gui.switch_button.grid_remove()
        self.atm_gui.quit_button.grid_remove()

        self.atm_gui.prompt['text'] = 'How much would you like to withdraw?'
        self.atm_gui.prompt.grid(row=0, column=0, padx=200)

        self.atm_gui.wdBack.grid(row=0, column=0, sticky=W, padx=100, pady=33)
        self.atm_gui.wd20.grid(row=1, column=0, sticky=W, padx=100, pady=33)
        self.atm_gui.wd40.grid(row=2, column=0, sticky=W, padx=100, pady=33)

        self.atm_gui.wd60.grid(row=0, column=0, sticky=E, padx=100, pady=33)
        self.atm_gui.wd80.grid(row=1, column=0, sticky=E, padx=100, pady=33)
        self.atm_gui.wd100.grid(row=2, column=0, sticky=E, padx=100, pady=33)
        self.wd_binds()

    def deposit_screen(self):
        self.atm_gui.account_name.grid_remove()
        self.atm_gui.account_type.grid_remove()
        self.atm_gui.account_balance.grid_remove()
        self.atm_gui.withdraw_button.grid_remove()
        self.atm_gui.deposit_button.grid_remove()
        self.atm_gui.switch_button.grid_remove()
        self.atm_gui.quit_button.grid_remove()

        self.atm_gui.prompt['text'] = 'How much would you like to deposit?'
        self.atm_gui.prompt.grid(row=0, column=0, padx=200)
        self.atm_gui.amount_entry.grid(row=1, column=0, padx=200)

        self.atm_gui.back_button.grid(row=0, column=0, sticky=W, padx=100, pady=50)
        self.atm_gui.confirm_button.grid(row=0, column=0, sticky=E, padx=100, pady=50)
        self.dep_binds()

    def wd_binds(self):
        self.atm_gui.wdBack.config(command=self.wd_back)
        self.atm_gui.wd20.config(command=lambda: self._withdraw(20))
        self.atm_gui.wd40.config(command=lambda: self._withdraw(40))
        self.atm_gui.wd60.config(command=lambda: self._withdraw(60))
        self.atm_gui.wd80.config(command=lambda: self._withdraw(80))
        self.atm_gui.wd100.config(command=lambda: self._withdraw(100))

    def dep_binds(self):
        self.atm_gui.back_button.config(command=self.dep_back)
        self.atm_gui.confirm_button.config(command=self._deposit)

    def wd_back(self):
        self.atm_gui.wdBack.grid_remove()
        self.atm_gui.wd20.grid_remove()
        self.atm_gui.wd40.grid_remove()
        self.atm_gui.wd60.grid_remove()
        self.atm_gui.wd80.grid_remove()
        self.atm_gui.wd100.grid_remove()

        if ACC_DISPLAYED == 'CH':
            self.display_ch_info()
        elif ACC_DISPLAYED == 'SA':
            self.display_sa_info()

    def dep_back(self):
        self.atm_gui.back_button.grid_remove()
        self.atm_gui.confirm_button.grid_remove()
        self.atm_gui.amount_entry.grid_remove()
        self.atm_gui.prompt.grid_remove()

        if ACC_DISPLAYED == 'CH':
            self.display_ch_info()
            self.atm_gui.amount_entry.delete(0, 'end')
        elif ACC_DISPLAYED == 'SA':
            self.display_sa_info()
            self.atm_gui.amount_entry.delete(0, 'end')

    def _withdraw(self, amount):
        if ACC_DISPLAYED == 'CH':
            for acc in self._acc_db._accountdb[LOG_ACCNUM]:
                if (acc.acc_type == 'Chequing') and (float(acc.acc_bal) > -500):
                    acc.withdraw(float(amount))
                    self.wd_back()
                else:
                    self.atm_gui.prompt['text'] = 'Insufficient Funds!'
                    self.atm_gui.prompt.grid(row=0, column=0)

        if ACC_DISPLAYED == 'SA':
            for acc in self._acc_db._accountdb[LOG_ACCNUM]:
                if (acc.acc_type == 'Savings') and (float(acc.acc_bal) > -500):
                    acc.withdraw(float(amount))
                    self.wd_back()
                else:
                    self.atm_gui.prompt['text'] = 'Insufficient Funds!'
                    self.atm_gui.prompt.grid(row=0, column=0)

    def _deposit(self):
        amount = self.atm_gui.amount_entry.get()

        if ACC_DISPLAYED == 'CH':
            for acc in self._acc_db._accountdb[LOG_ACCNUM]:
                if (acc.acc_type == 'Chequing'):
                    acc.deposit(float(amount))
                    self.atm_gui.amount_entry.delete(0, 'end')
                    self.dep_back()

        if ACC_DISPLAYED == 'SA':
            for acc in self._acc_db._accountdb[LOG_ACCNUM]:
                if (acc.acc_type == 'Savings'):
                    acc.deposit(float(amount))
                    self.atm_gui.amount_entry.delete(0, 'end')
                    self.dep_back()


    def _switch(self):
        self.atm_gui.account_name.grid_remove()
        self.atm_gui.account_type.grid_remove()
        self.atm_gui.account_balance.grid_remove()
        self.atm_gui.withdraw_button.grid_remove()
        self.atm_gui.deposit_button.grid_remove()
        self.atm_gui.switch_button.grid_remove()
        self.atm_gui.quit_button.grid_remove()

        self.atm_gui.welcome_screen.grid(row=0, column=0, padx=200)
        self.atm_gui._select_ch_BUTTON.grid(row=0, column=0, sticky=W, padx=100, pady=100)
        self.atm_gui._select_sa_BUTTON.grid(row=0, column=0, sticky=E, padx=100, pady=100)



    def _quit(self):
        self.atm_gui.account_name.grid_remove()
        self.atm_gui.account_type.grid_remove()
        self.atm_gui.account_balance.grid_remove()
        self.atm_gui.withdraw_button.grid_remove()
        self.atm_gui.deposit_button.grid_remove()
        self.atm_gui.switch_button.grid_remove()
        self.atm_gui.quit_button.grid_remove()

        self._acc_db.write_new_file(ACC_DB_FILE)

        self.atm_gui.prompt['text'] = ''
        self.atm_gui.prompt.grid(row=0, column=0)
        self.atm_gui.username_label.grid(row=1, column=0)
        self.atm_gui.username.grid(row=2, column=0, padx=0, pady=50)
        self.atm_gui.PIN_label.grid(row=3, column=0)
        self.atm_gui.password.grid(row=4, column=0, padx=0, pady=50)
        self.atm_gui.submit_button.grid(row=5, column=0, padx=0, pady=50)
























    # def _withdraw(self):
    #     self.click_wd()
    #
    # def _deposit(self):
    #     self.click_dep()
    #
    # def _quit(self):
    #     ROOT.destroy()
    #
    # def _print_receipt(self):
    #     receipt = 'Initial Balance: ${}\n'.format(self.initial_bala)
    #     for trans in self.transactions:
    #         receipt += ('{}: ${}\n'.format(trans[0], trans[1]))
    #     receipt += 'Ending Balance: ${}\n'.format(self.account_db[LOG_ACCNUM]['acc_balance'])
    #
    #     messagebox.showinfo(title='Receipt', message=receipt)
    #     pass
    #
    # def click_wd(self):
    #
    #     def confirm_wd():
    #         self.wd_pend = float(wd_amount.get())
    #         if self.account_db[LOG_ACCNUM]['acc_balance'] - self.wd_pend < 0:
    #             messagebox.showinfo(title='Insufficient Funds',
    #                                 message="You do not have enough funds for that withdrawal.")
    #             return
    #         else:
    #             self.account_db[LOG_ACCNUM]['acc_balance'] -= self.wd_pend
    #             self.transactions.append(['Withdrew', self.wd_pend])
    #             self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(
    #                 self.account_db[LOG_ACCNUM]['acc_balance'])
    #             ROOT.update()
    #
    #         toplevel.destroy()
    #         return
    #
    #     toplevel = Toplevel()
    #
    #     prompt = Label(toplevel, text='How much would you like to withdraw?', height=0, width=100)
    #     prompt.pack()
    #
    #     wd_amount = Entry(toplevel)
    #     wd_amount.pack()
    #
    #     confirm = Button(toplevel, text='Confirm')
    #     confirm.config(command=confirm_wd)
    #     confirm.pack()
    #     return
    #
    # def click_dep(self):
    #
    #     def confirm_dep():
    #         self.dep_pend = float(dep_amount.get())
    #         self.account_db[LOG_ACCNUM]['acc_balance'] += self.dep_pend
    #         self.transactions.append(['Deposited', self.dep_pend])
    #         self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(
    #             self.account_db[LOG_ACCNUM]['acc_balance'])
    #         ROOT.update()
    #
    #         toplevel.destroy()
    #         return
    #
    #     toplevel = Toplevel()
    #
    #     prompt = Label(toplevel, text='How much would you like to deposit?', height=0, width=100)
    #     prompt.pack()
    #
    #     dep_amount = Entry(toplevel)
    #     dep_amount.pack()
    #
    #     confirm = Button(toplevel, text='Confirm')
    #     confirm.config(command=confirm_dep)
    #     confirm.pack()
    #     return
