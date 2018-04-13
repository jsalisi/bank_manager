import csv
import os
import os.path

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
                    self._accountdb[lines[0]].append([lines[1], lines[2], lines[3], lines[4]])
                except KeyError:
                    self._accountdb[lines[0]] = [[lines[1], lines[2], lines[3], lines[4]]]
        return

if __name__ == '__main__':
    db = Account_DB()
    db.read_file(FILE)
    print(db._accountdb)
