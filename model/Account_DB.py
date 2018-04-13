from model.account import AccountBalance
from model.chequing import Chequing
from model.savings import Savings

FILE = 'account_info.csv'


class Account_DB:
    def __init__(self):
        self._account_dict = {
            'name': {
                'acc_num': ['type', 'balance']
            }
        }