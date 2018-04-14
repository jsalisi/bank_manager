import csv
import os
import os.path

FILE = 'account_login.csv'

class Login_DB:
    def __init__(self):
        self._logindb = {}
        self._card_num = ''
        self._PIN = ''
        self.read_file(FILE)

    def read_file(self, file):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', file)), 'r',
                  newline='') as myfile:
            reader = csv.reader(myfile)
            next(reader, None)
            for lines in reader:
                self._logindb[lines[0]] = lines[1]
        return

    def update_login(self, FILE, card_number, pin_pass):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE)), 'a',
                  newline='') as myfile:
            card_num = card_number
            PIN = pin_pass
            row = [card_num, PIN]
            header = ['CARD_NUM, PIN']
            writer = csv.writer(myfile)

            if not os.path.isfile(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE))):
                writer.writerow(header)
                writer.writerow(row)
            else:
                writer.writerow(row)
        return

if __name__ == '__main__':
    db = Login_DB()
    db.read_file(FILE)
    print(db._logindb)
