from account import AccountBalance
from chequing import Chequing
from savings import Savings

FILE = 'account_info.csv'


class Account_DB:
    def __init__(self):
        self._account_dict = {
            'name': {
                'acc_num': ['type', 'balance']
            }
        }