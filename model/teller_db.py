import csv
import os
import os.path

FILE = 'teller_account.csv'

class Teller_DB:
    def __init__(self):
        self._tellerdb = {}
        self._id = ''
        self._pass = ''

    def read_file(self, file):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', file)), 'r',
                  newline='') as myfile:
            reader = csv.reader(myfile)
            next(reader, None)
            for lines in reader:
                self._tellerdb[lines[0]] = lines[1]
        return

if __name__ == '__main__':
    db = Teller_DB()
    db.read_file(FILE)
    print(db._tellerdb)
