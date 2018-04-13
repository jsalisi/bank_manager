import csv
import os
import os.path

FILE = 'account_login.csv'

class Login_DB:
    def __init__(self):
        self._logindb = {}
        self._card_num = ''
        self._PIN = ''

    def read_file(self, file):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', file)), 'r',
                  newline='') as myfile:
            reader = csv.reader(myfile)
            next(reader, None)
            for lines in reader:
                self._logindb[lines[0]] = lines[1]
        return

if __name__ == '__main__':
    db = Login_DB()
    db.read_file(FILE)
    print(db._logindb)
