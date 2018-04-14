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

    def write_new_file(self, file):
        header = ['card_num', 'acc_name', 'acc_number', 'acc_type', 'balance']
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', file)), 'w',
                  newline='') as myfile:
            writer = csv.writer(myfile)
            writer.writerow(header)

            for key, val in self._accountdb.items():
                for item in val:
                    if item.acc_type == 'Savings':
                        row = [key, item.acc_name, str(item.acc_num), item.acc_type, str(item.acc_bal)]
                        writer.writerow(row)
                    elif item.acc_type == 'Chequing':
                        row = [key, item.acc_name, str(item.acc_num), item.acc_type, str(item.acc_bal)]
                        writer.writerow(row)
        return


if __name__ == '__main__':
    db = Account_DB()
    db._accountdb['1234123412341234'][0].deposit(100)
    db.write_new_file(FILE)
