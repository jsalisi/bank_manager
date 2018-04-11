from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts


class ControllerFunctions:

    def __init__(self):
        self.view = CommandLinePrompts()
        self.current_user_mod = ""
        self.login_status = False

    def login(self):
        while self.login_status is False:
            system('cls')
            id = self.view.login_id()
            passwd = self.view.login_passwd()

            if int(id) == 12345 and int(passwd) == 12345:
                self.login_status = True
                system('cls')

    def logout(self):
        self.login_status = False

    def main_menu(self):
        system('cls')
        self.view.main_prompt()

    def usercfg(self):
        system('cls')
        self.current_user_mod = self.view.user_id
        self.view.config_user(self.current_user_mod)

    def accountcfg(self):
        system('cls')
        self.view.manage_accounts(self.current_user_mod)

    def useradd(self):
        system('cls')
        self.view.add_user_num()
        self.view.add_user_pin()

    def userdel(self):
        system('cls')
        self.view.del_user(self.current_user_mod)

    def withdraw(self):
        system('cls')
        print('withdraw')

    def deposit(self):
        system('cls')
        print('deposit')

    def display_help(self):
        system('cls')
        print(self.view.help())
