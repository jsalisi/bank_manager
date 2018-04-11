import getpass

class CommandLinePrompts:
    """ 
    
    Prompts that are displayed on the command line interface.

    """

    # Command Input
    def cmd_input(self):
        return input("\n\nCommand: ")

    # Help
    def help(self):
        cmd_main =       '      main               - Opens the main menu'
        cmd_usercfg =    '      userconfig         - Opens the user configuration menu'
        cmd_accountcfg = '      accountconfig      - Opens the account configuration menu'
        cmd_useradd =    '      useradd            - Opens the add user interface'
        cmd_userdel =    '      userdel            - Opens the delete user interface'
        cmd_withdraw =   '      withdraw           - Withdraw money from an account'
        cmd_deposit =    '      deposit            - Deposit money to an account'
        cmd_logout =     '      logout             - Logs out of account'
        cmd_help =       '      help               - Displays list of all commands'
        return "System Commands: \n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(cmd_main, cmd_usercfg, cmd_accountcfg, cmd_useradd, cmd_userdel, cmd_withdraw, cmd_deposit, cmd_logout, cmd_help)

    # Display Error
    def error(self, err):
        print("\n" + err, end = ' ')
        return input('Press Enter to continue.')


    # Level 0 Menu
    def login_id(self):
        return input("Login: ")

    def login_passwd(self):
        return getpass.getpass("Password: ")


    # Level 1 Menu
    def main_prompt(self):
        return int(input("Bank Manager\n\n1.) Manage Users\n2.) Logout\n\nEnter Command: "))

    # Level 2 Menu
    def manage_users(self):
        return int(input("Manage Users\n\n1.) Configure Existing User\n2.) Add User\n3.) Delete User\n\n0.) Return\n\nEnter Command: "))


    # Level 3 Menus

    # Configure Existing User
    def user_id(self):
        return int(input("User ID: "))

    def config_user(self, user_id):
        return int(input("Configuring {}\n\n1.) Manage Accounts\n2.) Transaction Logs\n3.) Delete User\n\n0.) Return\n\nEnter Command: ".format(user_id)))

    # Add User
    def add_user_num(self):
        return input("New Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("New PIN: ")

    # Delete User
    def del_user(self, user_id):
        return str(input("Delete {}? (Y/N)".format(user_id)))

 
    # Level 4 Menus

    # Manage Accounts
    def manage_accounts(self, user_id):
        return int(input("Manage Accounts\n\n1.) Display Accounts\n2.) Add Account\n3.) Delete Account\n\n0.) Return\n\nEnter Command: "))

 
    # Level 5 Menu

    # Display Accounts
    def display_accounts(self, accounts):
        print("Manage Accounts\n")
        for account in accounts:
            print(str(accounts.index(account)) + ".)", account)
        return int(input("\n\nEnter Command: "))

    # Add / Delete Account
    def accounts(self):
        return input("Accounts\n\n1.) Chequing\n\2.) Savings\n\3.) Term Savings\n\n0.) Return\n\nEnter Command: ")
