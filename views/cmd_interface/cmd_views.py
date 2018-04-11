import getpass
import os

class CommandLinePrompts:
    """ 
    
    Prompts that are displayed on the command line interface.

    """

    
    # Level 0 Menu
    def login_id(self):
        os.system('cls')
        return input("\nLogin: ")

    def login_passwd(self):
        return getpass.getpass("Password: ")

    # Level 1 Menu
    def main_prompt(self):
        os.system('cls')
        return int(input("\nBank Manager\n\n1.) Manage Users\n2.) Logout\n\nEnter Command: "))

    # Level 2 Menu
    def manage_users(self):
        os.system('cls')
        return int(input("\nManage Users\n\n1.) Configure Existing User\n2.) Add User\n3.) Delete User\n\n0.) Return\n\nEnter Command: "))

    # Level 3 Menus
    def add_user_num(self):
        os.system('cls')
        return input("\nNew Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("New PIN: ")

    def del_user(self, user_id):
        os.system('cls')
        return str(input("Delete {}? (Y/N)".format(user_id)))

    def user_id(self):
        os.system('cls')
        return input("User ID: ")

    def config_user(self, user_id):
        os.system('cls')
        return int(input("\nConfiguring {}\n\n1.) Manage Accounts\n2.) Transaction Logs\n3.) Delete User\n\n0.) Return\n\nEnter Command: ".format(user_id)))

    # Level 4 Menus
    def manage_accounts(self):
        os.system('cls')
        return int(input("\nManage Accounts\n\n1.) Display Accounts\n2.) Add Account\n3.) Delete Account\n\n0.) Return\n\nEnter Command: "))

    # Level 5 Menu
    def display_accounts(self, accounts):
        os.system('cls')
        print("\nManage Accounts\n")
        for account in accounts:
            print(str(accounts.index(account)) + ".)", account)
        return int(input("\n\nEnter Command: "))

    def accounts(self):
        os.system('cls')
        return input("\nAccounts\n\n1.) Chequing\n\2.) Savings\n\3.) Term Savings\n\n0.) Return\n\nEnter Command: ")

    def error(self, err):
        return err
