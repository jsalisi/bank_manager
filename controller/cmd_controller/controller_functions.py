import os
from os import system
import os.path
import csv
import platform

from views.cmd_interface.cmd_views import CommandLinePrompts

from model.account import AccountBalance
from model.chequing import Chequing
from model.savings import Savings

from model.teller_db import Teller_DB
from model.account_db import Account_DB
from model.login_db import Login_DB

from model.transactions.transaction_log import TransactionLog

# Static file names
FILE = 'account_login.csv'
DB_FILE = 'account _info.csv'


class ControllerFunctions:
    """
    This class contains the functions used in the CLI controller
    and adheres to the MVC model.

    """


    def __init__(self):
        self.log_db = Teller_DB()
        self.acc_db = Account_DB()
        self.acc_login_db = Login_DB()
        self.transact_log = TransactionLog()
        self.view = CommandLinePrompts()
        
        self.teller_id = ""
        self.current_card_num = ""
        self.login_status = False

        self.clear_cmd = 'cls'

    def determine_platform(self):
        if platform.system() == 'Windows':
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

    def display_help(self):
        print(self.view.usercfg_help())
        print(self.view.accountcfg_help())
        print(self.view.help())

    def login(self):
        while self.login_status is False:
            system(self.clear_cmd)
            id = self.view.login_id()
            passwd = self.view.login_passwd()

            if (id in self.log_db._tellerdb) and (self.log_db._tellerdb[id] == passwd):
                self.teller_id = id
                self.login_status = True
                system(self.clear_cmd)
            
            else:
                self.view.error("Login Failed.")

    def logout(self):
        self.login_status = False

    def usercfg(self, *args):
        try:
            # Display all user information: Name, Accounts, Account Types, Balances
            if args[0][1] == 'info':
                self.current_card_num = self.view.user_id()
                self.view.user_info(self.acc_db._accountdb[self.current_card_num])
            
            # Check specific user information
            elif args[0][1] == 'chk':
                self.current_card_num = self.view.user_id()
                choice = int(self.view.config_user(self.current_card_num))
                
                # Check balance of specific account
                if choice == 1:
                    accs = []
                    for ac in self.acc_db._accountdb[self.current_card_num]:
                        accs.append(ac.acc_type)
                    c = self.view.display_accounts(accs, self.current_card_num)
                    
                    acc_type =  self.acc_db._accountdb[self.current_card_num][c-1].acc_type
                    c_bal = self.acc_db._accountdb[self.current_card_num][c-1].get_balance

                    self.view.get_balance(acc_type, c_bal)
                
                # Display transactions of specified account
                elif choice == 2:
                    for acc in self.acc_db._accountdb[self.current_card_num]:
                        self.transact_log.show_transactions(acc.acc_num)
            
            # Add a new user to the system
            elif args[0][1] == 'add':
                # Collect new user information
                new_fname = self.view.new_fname()
                new_lname = self.view.new_lname()
                new_num = self.view.add_user_num()
                new_pin = self.view.add_user_pin()

                new_acc = ''
                ch = int(self.view.accounts())

                # initialize an account with the new user
                if ch == 1:
                    new_acc = Chequing(new_fname, new_lname, 0, new_num)
                elif ch == 2:
                    new_acc = Savings(new_fname, new_lname, 0, new_num)

                # Adding user to the database
                self.acc_db._accountdb[new_num].append(new_acc)
                self.acc_login_db.update_login(FILE, new_num, new_pin)

        except (KeyError, IndexError):
            self.view.error("Command not specified.")
            print(self.view.usercfg_help())
        

    def accountcfg(self, *args):
        try:
            # Show specific account info
            if args[0][1] == 'info':
                self.current_card_num = self.view.user_id()
                accs = []
                for ac in self.acc_db._accountdb[self.current_card_num]:
                    accs.append(ac.acc_type)
                c = int(self.view.display_accounts(accs, self.current_card_num))
                print(self.acc_db._accountdb[self.current_card_num][c])
           
           # Show specific account transactions
            elif args[0][1] == 'transact':
                self.current_card_num = self.view.user_id()
                c = self.view.display_accounts(accs, self.current_card_num)
                acc_num =  self.acc_db._accountdb[self.current_card_num][c-1].acc_num
                self.transact_log.show_transactions(acc_num)
            
            # Show specific account balance
            elif args[0][1] == 'bal':
                self.current_card_num = self.view.user_id()
                accs = []
                for ac in self.acc_db._accountdb[self.current_card_num]:
                    accs.append(ac.acc_type)
                c = int(self.view.display_accounts(accs, self.current_card_num))
                a = self.acc_db._accountdb[self.current_card_num][c].acc_type
                b = self.acc_db._accountdb[self.current_card_num][c].get_balance
                self.view.get_balance(a, b)
            
            # Add a new account to a user
            elif args[0][1] == 'add':
                new_acc = ''
                self.current_card_num = self.view.user_id()
                name = self.acc_db._accountdb[self.current_card_num][0].acc_name.split()
                ch = int(self.view.accounts())

                if ch == 1:
                    new_acc = Chequing(name[0], name[0], 0, self.current_card_num)
                elif ch == 2:
                    new_acc = Savings(name[0], name[0], 0, self.current_card_num)

                self.acc_db._accountdb[self.current_card_num].append(new_acc)

        except (KeyError, IndexError):
            self.view.error("Command not specified.")
            print(self.view.accountcfg_help())
        
    # Withdraw from a user specified account
    def withdraw(self, *args):
        try:
            accs = []
            for ac in self.acc_db._accountdb[args[0][1]]:
                accs.append(ac.acc_type)
            c = int(self.view.display_accounts(accs, self.current_card_num))
            self.acc_db._accountdb[args[0][1]][c-1].withdraw(float(args[0][2]))

            self.acc_db.write_new_file(DB_FILE)

        except (KeyError, IndexError):
            self.view.error("Error.")
            print(self.view.withdraw_help())

    # Deposit to a user specified account
    def deposit(self, *args):
        try:
            accs = []
            for ac in self.acc_db._accountdb[args[0][1]]:
                accs.append(ac.acc_type)
            c = int(self.view.display_accounts(accs, self.current_card_num))
            self.acc_db._accountdb[args[0][1]][c-1].deposit(float(args[0][2]))
        
            self.acc_db.write_new_file(DB_FILE)

        except (KeyError, IndexError):
            self.view.error("Error.")
            print(self.view.deposit_help())
