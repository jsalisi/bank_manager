from .transactions.transaction_log import TransactionLog
from .constants import *


class AccountBalance:
    """ Manages the account balance of a bank account """

    #  Account types
    _SAVINGS = "Savings"
    _TERM_SAViNGS = "Term Savings"
    _CHEQUING = "Chequing"
    _DEFAULT_TYPE = "Chequing"

    #  Account Numbers
    _SAVINGS_ACC_NUM = 555000
    _TERM_SAVINGS_ACC_NUM = 655000
    _CHEQUING_ACC_NUM = 444000

    def __init__(self, acc_fname: str = "", acc_lname: str = "", acc_bal: float = 0.0):
        try:
            self.acc_name = "{} {}".format(acc_fname, acc_lname)
            self.acc_bal = acc_bal
        except (ValueError, TypeError):
            print("Invalid input.")

        self.acc_type = AccountBalance._DEFAULT_TYPE
        self.t_logs = TransactionLog()
        return

    def __str__(self):
        acc_info = ("Account Number: {}, Name: {}, Balance: ${}, Type: {}") \
            .format(self.acc_num, self.acc_name, self.acc_bal, self.acc_type)
        return acc_info

    @property
    def get_balance(self):
        return self.acc_bal

    def deposit(self, amount: float):
        tr_type = DEPOSITING
        try:
            if amount <= 0:
                print("Invalid deposit amount.")
            else:
                self.t_logs.add_log(self.acc_num, tr_type, amount, self.acc_bal)
                self.acc_bal += amount
        except (TypeError, ValueError):
            print("Invalid input.")
        return

    def withdraw(self, amount: float):
        tr_type = WITHDRAWING

        try:
            if (amount <= (self.acc_bal+OVERDRAFT)) and (amount > 0) and (self.acc_type == AccountBalance._CHEQUING):
                self.t_logs.add_log(self.acc_num, tr_type, amount, self.acc_bal)
                self.acc_bal -= amount
            elif (amount <= self.acc_bal) and (amount > 0) and (self.acc_type == AccountBalance._SAVINGS):
                self.t_logs.add_log(self.acc_num, tr_type, amount, self.acc_bal)
                self.acc_bal -= amount
            elif amount > self.acc_bal:
                print("Insufficient Funds")
            elif amount < 0:
                print("Invalid withdraw amount.")
        except (ValueError, TypeError):
            print("Invalid input.")
        return

    def change_name(self, new_fname: str = "", new_lname: str = ""):
        try:
            self.acc_name = "{} {}".format(new_fname, new_lname)
        except (ValueError, TypeError):
            print("Invalid input.")
        return
