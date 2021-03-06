from model.account import AccountBalance
from model.transactions.transaction_log import TransactionLog
from model.constants.fees_consts import *
from model.constants.interest_consts import *
from model.constants.transaction_types import *
import os.path

FILE = 'account_info.csv'


class Savings(AccountBalance):
    """ Manages the savings account balance of the account """

    def __init__(self, acc_fname, acc_lname, acc_bal, card_num):
        """
        Initializes an account with specified names, balance, 
        and card number it's tied to.
        
        Args:
            acc_fname (string): The first name of a user
            acc_lname (string): The last name of a user
            acc_bal (float): The account balance of the user
            card_num (string): User's bank card number
        """
        super().__init__(acc_fname, acc_lname, acc_bal, card_num)

        self.acc_type = AccountBalance._SAVINGS

        AccountBalance._SAVINGS_ACC_NUM += 1
        self.acc_num = AccountBalance._SAVINGS_ACC_NUM

        # if os.path.isfile(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE))):
        #     self.update_init(FILE)
        # elif not os.path.isfile(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE))):
        #     self.write_new_file(FILE)
        #     self.update_init(FILE)
        return

    def charge_service_fee(self):
        tr_type = CHARGING_FEE

        if self.acc_bal < MIN_SAVINGS_BALANCE:
            self.t_logs.add_log(self.acc_num, tr_type, SERVICE_FEE, self.acc_bal)
            self.acc_bal -= SERVICE_FEE

    def pay_interest(self):
        tr_type = PAYING_INTEREST

        if self.acc_bal >= MIN_SAVINGS_BALANCE:
            self.t_logs.add_log(self.acc_num, tr_type, (SAVINGS_INTEREST_RATE * self.acc_bal), self.acc_bal)
            self.acc_bal += (SAVINGS_INTEREST_RATE * self.acc_bal)
        else:
            print("Not enough money in savings.")

if __name__ == '__main__':
    m1 = Savings('steve', 'cheng', 999, 999999)
    print(m1.acc_name)
