from .account import AccountBalance
from .transactions.transaction_log import TransactionLog
from .constants import *


class Chequing(AccountBalance):
    """ Manages the chequing account balance of the the account """

    def __init__(self, acc_fname: str = "", acc_lname: str = "", acc_bal: float = 0):
        super().__init__(acc_fname, acc_lname, acc_bal)

        self.acc_type = AccountBalance._CHEQUING

        AccountBalance._CHEQUING_ACC_NUM += 1
        self.acc_num = AccountBalance._CHEQUING_ACC_NUM

    def charge_interest(self):
        tr_type = CHARGING_INTEREST

        if self.acc_bal < 0:
            self.t_logs.add_log(self.acc_num, tr_type, CHEQUING_OVERDRAFT_INTEREST_RATE * (self.acc_bal / -1), self.acc_bal)
            self.acc_bal -= (CHEQUING_OVERDRAFT_INTEREST_RATE * (self.acc_bal / -1))

    def cheque_bounce_fee(self):
        tr_type = CHARGING_FEE

        self.t_logs.add_log(self.acc_num, tr_type, CHEQUE_BOUNCE_FEE, self.acc_bal)
        self.acc_bal -= CHEQUE_BOUNCE_FEE
