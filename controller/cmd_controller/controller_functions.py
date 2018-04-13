from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts

from model.account import AccountBalance
from model.chequing import Chequing
from model.savings import Savings
from model.term_savings import TermSavings
import os
import os.path
import csv
from model.teller_db import Teller_DB
from model.account_db import Account_DB
from model.login_db import Login_DB

FILE = 'account_login.csv'


class ControllerFunctions:

    def __init__(self):
        # self.chq = Chequing("Justin", "j", 12345)
        # self.sav = Savings("Justin", "j", 12345)
        # self.tsav = TermSavings("Justin", "j", 12345)

        # self.model = {
        #     444001: self.chq,
        #     555001: self.sav,
        #     655001: self.tsav
        # }
        self.log_db = Teller_DB()
        self.acc_db = Account_DB()
        self.acc_login_db = Login_DB()

        self.view = CommandLinePrompts()
        self.teller_id = ""
        self.current_card_num = ""
        self.login_status = False

    def display_help(self):
        print(self.view.usercfg_help())
        print(self.view.accountcfg_help())
        print(self.view.help())

    def login(self):
        while self.login_status is False:
            system('cls')
            id = self.view.login_id()
            passwd = self.view.login_passwd()

            if (id in self.log_db._tellerdb) and (self.log_db._tellerdb[id] == passwd):
                self.teller_id = id
                self.login_status = True
                system('cls')
            else:
                self.view.error("Login Failed.")

    def logout(self):
        self.login_status = False

    def usercfg(self, *args):
        try:
            if args[0][1] == 'info':
                print("\nDisplaying User Info: ")
            elif args[0][1] == 'edit':
                print(self.acc_db._accountdb)
                self.current_card_num = self.view.user_id()
                choice = self.view.config_user(self.current_card_num)

                if choice == 1:
                    self.view.display_accounts(self.acc_db._accountdb[self.current_card_num], self.current_card_num)
                elif choice == 2:
                    print('Displaying Transaction Logs ')
                elif choice == 3:
                    self.view.del_user(self.current_card_num)
            elif args[0][1] == 'add':
                self.view.add_user_num()
                self.view.add_user_pin()
            elif args[0][1] == 'del':
                self.current_card_num = self.view.user_id()
                self.view.del_user(self.current_card_num)

        except IndexError:
            self.view.error("Command not specified.")

    def accountcfg(self, *args):
        try:
            if args[0][1] == 'info':
                self.current_card_num = self.view.user_id()
                c = self.view.display_accounts(['Chq', 'Sav'], self.current_card_num)
                print(c)
            elif args[0][1] == 'transact':
                self.current_card_num = self.view.user_id()
                c = self.view.display_accounts(['Chq', 'Sav'], self.current_card_num)
                print(c)
            elif args[0][1] == 'bal':
                self.current_card_num = self.view.user_id()
                a = self.acc_db._accountdb[self.current_card_num][0][2]
                b = self.acc_db._accountdb[self.current_card_num][0][3]
                self.view.get_balance(a, b)
            elif args[0][1] == 'add':
                self.view.accounts()
            elif args[0][1] == 'del':
                self.view.accounts()
        except IndexError:
            self.view.error("Command not specified.")
        
    def withdraw(self, *args):
        try:
            self.model[float(args[0][1])].withdraw(float(args[0][2]))
        except:
            self.view.error("Error: Parameters were not met.")
            print(self.view.withdraw_help())

    def deposit(self, *args):
        try:
            print(args)
            self.model[float(args[0][1])].deposit(float(args[0][2]))
        except:
            self.view.error("Error: Parameters were not met.")
            print(self.view.deposit_help())

    def update_login(self, FILE):
        with open(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE)), 'a',
                  newline='') as myfile:
            card_num = self.chq._card_num
            PIN = self.chq._PIN
            row = [card_num, PIN]
            header = ['CARD_NUM, PIN']
            writer = csv.writer(myfile)

            if not os.path.isfile(os.path.join(os.path.dirname(__file__), os.path.join('Accounts', FILE))):
                writer.writerow(header)
                writer.writerow(row)
            else:
                writer.writerow(row)
        return
