from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts
from model import (Chequing, Savings, TermSavings)


class ControllerFunctions:

    def __init__(self):
        self.view = CommandLinePrompts()
        self.teller_id = ""
        self.current_user_mod = ""
        self.login_status = False

    def display_help(self):
        system('cls')
        print(self.view.help())

    def login(self):
        while self.login_status is False:
            system('cls')
            id = self.view.login_id()
            passwd = self.view.login_passwd()

            if int(id) == 12345 and int(passwd) == 12345:
                self.teller_id = int(id)
                self.login_status = True
                system('cls')
            else:
                self.view.error("Login Failed.")

    def logout(self):
        self.login_status = False

    def usercfg(self, *args):
        try:
            if args[0][1] == 'adduser':
                system('cls')
                self.view.add_user_num()
                self.view.add_user_pin()
            elif args[0][1] == 'deluser':
                system('cls')
                self.view.del_user(self.current_user_mod)

        except IndexError:
            system('cls')
            res = self.view.manage_users()
            
            if res == 1:
                system('cls')
                self.current_user_mod = self.view.user_id()
                system('cls')
                self.view.config_user(self.current_user_mod)

            elif res == 2:
                system('cls')
                self.view.add_user_num()
                self.view.add_user_pin()
            
            elif res == 3:
                system('cls')
                self.view.del_user(self.current_user_mod)

    def accountcfg(self, *args):
        try:
            if args[0][1] == 'addaccount':
                system('cls')
                choice = self.view.accounts()
            elif args[0][1] == 'delaccount':
                system('cls')
                choice = self.view.accounts()
        except IndexError:
            system('cls')
            self.view.manage_accounts(self.current_user_mod)
        
    def withdraw(self, *args):
        system('cls')
        print('withdraw', " ".join(args[0]))

    def deposit(self, *args):
        system('cls')
        print('deposit', " ".join(args[0]))
