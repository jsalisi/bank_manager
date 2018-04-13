from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts
from model import (Chequing, Savings, TermSavings)


class ControllerFunctions:

    def __init__(self):
        self.chq = Chequing()
        self.sav = Savings()
        self.tsav = TermSavings()

        self.model = {
            444001: self.chq,
            555001: self.sav,
            655001: self.tsav
        }

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

            if id == 'admin' and int(passwd) == 1234:
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
                self.current_card_num = self.view.user_id()
                choice = int(self.view.config_user(self.current_card_num))

                if choice == 1:
                    self.view.display_accounts(['Chq', 'Sav'], self.current_card_num)
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
                self.view.get_balance("Chequing", 400)
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
