from time import localtime, strptime
from .account import AccountBalance
from .savings import Savings
from .constants import *


class TermSavings(Savings):
    """ Manages the term savings account class. """

    _TIME_PERIOD = 60

    def __init__(self, acc_fname: str = "", acc_lname: str = "", acc_bal: float = 0):
        super().__init__(acc_fname, acc_lname, acc_bal)

        self.acc_type = AccountBalance._TERM_SAViNGS

        AccountBalance._TERM_SAVINGS_ACC_NUM += 1
        self.acc_num = AccountBalance._TERM_SAVINGS_ACC_NUM

    def ts_withdraw(self, amount: float):
        tr_type = WITHDRAWING

        try:
            if (amount <= self.acc_bal) and (amount > 0):
                time_left = localtime().tm_yday - strptime(self.t_logs.tr_logs[0].split(",")[0], "%d %b %Y %H:%M:%S").tm_yday
                if time_left >= TermSavings._TIME_PERIOD:
                    self.t_logs.add_log(self.acc_num, tr_type, amount, self.acc_bal)
                    self.acc_bal -= amount
                else:
                    print("Wait {} more days before withdrawing".format(TermSavings._TIME_PERIOD - time_left))
            elif amount > self.acc_bal:
                print("Insufficient Funds")
            elif amount < 0:
                print("Invalid withdraw amount.")
        except (ValueError, TypeError):
            print("Invalid input.")

