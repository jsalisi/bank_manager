from tkinter import *
from tkinter import messagebox
import os
from model.chequing import *
from model.savings import *
from model.transactions.transaction_log import TransactionLog
from views.atm_interface.atmview import ATMWindow
from views.atm_interface.loginview import LoginWindow

LOGIN_FLAG = 0
LOG_ACCNUM = 0
ROOT = 0

class ATMController:

    def __init__(self, master):

        # database creation
        self.accounts = {
            '12345': '999999',
            '23456': '999999',
            '34567': '999999'
        }

        self.account_db = {
            '12345': {
                'acc_type': 'Chequing',
                'acc_balance': 5000.00
            },
            '23456': {
                'acc_type': 'Savings',
                'acc_balance': 4000.00
            },
            '34567': {
                'acc_type': 'Savings',
                'acc_balance': 3000.00
            }
        }

        # bindings and master creation
        self.master = master

        # login window (authentication)
        if LOGIN_FLAG == 0:
            self.atm_gui = LoginWindow(master)
            self.atm_gui.submit_button.config(command=self._login)

        # atm window
        elif LOGIN_FLAG == 1:
            self.atm_gui = ATMWindow(self.master)
            self.display_acc_info()
            self.initial_bala = self.account_db[LOG_ACCNUM]['acc_balance']
            self.atm_gui.withdraw_button.config(command=self._withdraw)
            self.atm_gui.deposit_button.config(command=self._deposit)
            self.atm_gui.info_button.config(command=self._print_receipt)
            self.atm_gui.quit_button.config(command=self._quit)

        # transactions
        self.transactions = []
        self.wd_pend = 0
        self.dep_pend = 0

        self.atm_gui.file_menu.add_command(label='Quit', command=self.master.quit)


    def _login(self):
        user_info = str(self.atm_gui.username.get())
        pass_info = str(self.atm_gui.password.get())

        print(user_info)
        print(pass_info)
        if (user_info in self.accounts) and (self.accounts[user_info] == pass_info):
            global LOG_ACCNUM
            LOG_ACCNUM = user_info

            global LOGIN_FLAG
            LOGIN_FLAG = 1

            self.master.destroy()

            global ROOT
            ROOT = Tk()
            ATMController(ROOT)
            mainloop()

        else:
            self.atm_gui.username.delete(0, 'end')
            self.atm_gui.password.delete(0, 'end')
            messagebox.showinfo(title="Login Error", message="Either Card Number, or the PIN number is Wrong! Please Try again!")

    def display_acc_info(self):
        self.atm_gui.account_number['text'] = 'Account Number: {}'.format(LOG_ACCNUM)
        self.atm_gui.account_type['text'] = 'Account Type: {}'.format(self.account_db[LOG_ACCNUM]['acc_type'])
        self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(self.account_db[LOG_ACCNUM]['acc_balance'])

    def _withdraw(self):
        self.click_wd()

    def _deposit(self):
        self.click_dep()

    def _quit(self):
        ROOT.destroy()

    def _print_receipt(self):
        receipt = 'Initial Balance: ${}\n'.format(self.initial_bala)
        for trans in self.transactions:
            receipt += ('{}: ${}\n'.format(trans[0], trans[1]))
        receipt += 'Ending Balance: ${}\n'.format(self.account_db[LOG_ACCNUM]['acc_balance'])

        messagebox.showinfo(title='Receipt', message=receipt)
        pass

    def click_wd(self):

        def confirm_wd():
            self.wd_pend = float(wd_amount.get())
            if self.account_db[LOG_ACCNUM]['acc_balance'] - self.wd_pend < 0:
                messagebox.showinfo(title='Insufficient Funds',
                                    message="You do not have enough funds for that withdrawal.")
                return
            else:
                self.account_db[LOG_ACCNUM]['acc_balance'] -= self.wd_pend
                self.transactions.append(['Withdrew', self.wd_pend])
                self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(
                    self.account_db[LOG_ACCNUM]['acc_balance'])
                ROOT.update()

            toplevel.destroy()
            return

        toplevel = Toplevel()

        prompt = Label(toplevel, text='How much would you like to withdraw?', height=0, width=100)
        prompt.pack()

        wd_amount = Entry(toplevel)
        wd_amount.pack()

        confirm = Button(toplevel, text='Confirm')
        confirm.config(command=confirm_wd)
        confirm.pack()
        return

    def click_dep(self):

        def confirm_dep():
            self.dep_pend = float(dep_amount.get())
            self.account_db[LOG_ACCNUM]['acc_balance'] += self.dep_pend
            self.transactions.append(['Deposited', self.dep_pend])
            self.atm_gui.account_balance['text'] = 'Account Balance: ${}'.format(
                self.account_db[LOG_ACCNUM]['acc_balance'])
            ROOT.update()

            toplevel.destroy()
            return

        toplevel = Toplevel()

        prompt = Label(toplevel, text='How much would you like to deposit?', height=0, width=100)
        prompt.pack()

        dep_amount = Entry(toplevel)
        dep_amount.pack()

        confirm = Button(toplevel, text='Confirm')
        confirm.config(command=confirm_dep)
        confirm.pack()
        return
