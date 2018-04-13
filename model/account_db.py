import csv
import os
import os.path

from model.account import AccountBalance
from model.chequing import Chequing
from model.savings import Savings

FILE = 'account_info.csv'


class Account_DB:
    def __init__(self):
        self._accountdb = {}
        self.read_file(FILE)

    def read_file(self, file):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', file)), 'r',
                  newline='') as myfile:
            reader = csv.reader(myfile)
            next(reader, None)
            for lines in reader:
                try:
                    new_acc = ''
                    if lines[3] == 'Chequing':
                        split_name = lines[1].split()
                        new_acc = Chequing(split_name[0], split_name[1], float(lines[4]), lines[0])
                    elif lines[3] == 'Savings':
                        new_acc = Savings(split_name[0], split_name[1], float(lines[4]), lines[0])
                    self._accountdb[lines[0]].append(new_acc)
                except KeyError:
                    new_acc = ''
                    if lines[3] == 'Chequing':
                        split_name = lines[1].split()
                        new_acc = Chequing(split_name[0], split_name[1], float(lines[4]), lines[0])
                    elif lines[3] == 'Savings':
                        new_acc = Savings(split_name[0], split_name[1], float(lines[4]), lines[0])
                    self._accountdb[lines[0]] = [new_acc]
        return

if __name__ == '__main__':
    db = Account_DB()
    db.read_file(FILE)
    print(db._accountdb)
