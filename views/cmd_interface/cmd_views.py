import getpass

class CommandLinePrompts:
    """ 
    
    Prompts that are displayed on the command line interface.

    """

    # Command Input
    def cmd_input(self, teller_id):
        return input('\n{}@Bank: '.format(teller_id))

    # Help
    def help(self):
        cmd_usercfg =    '      usercfg [OPTIONS]                           - Opens the user configuration menu'
        cmd_useradd =    '          - adduser [card number]                 - Add new bank user'
        cmd_userdel =    '          - deluser [card number]                 - Delete existing bank user\n'

        cmd_accountcfg = '      accountcfg [OPTIONS]                        - Opens the account configuration menu'
        cmd_chkbalance = '          - chkbal [account number]               - Returns the balance of the specified account'
        cmd_createacc =  '          - addaccount [account number]           - Add a new account to a user'
        cmd_deleteacc =  '          - delaccount [account number]           - Delete existing account from user\n'
        
        cmd_withdraw =   '      withdraw [account number] [amount]          - Withdraw money from an account'
        cmd_deposit =    '      deposit  [account number] [amount]          - Deposit money to an account\n'

        cmd_logout =     '      logout                                      - Logs out of account'
        cmd_help =       '      help                                        - Displays list of all commands'
        cmd_exit =       '      exit                                        - Closes the program'
        return "System Commands: \n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(cmd_usercfg, cmd_useradd, cmd_userdel, cmd_accountcfg, cmd_chkbalance, cmd_createacc, cmd_deleteacc, cmd_withdraw, cmd_deposit, cmd_logout, cmd_help, cmd_exit)

    # Display Error
    def error(self, err):
        print("\n" + err, end = ' ')
        return input('Press Enter to continue.')

    # Login
    def login_id(self):
        return input("Login: ")

    def login_passwd(self):
        return getpass.getpass("Password: ")

    # usrcfg prompt
    def manage_users(self):
        return int(input("Manage Users\n\n1.) Edit User\n2.) Add User\n3.) Delete User\n\nEnter Choice: "))

    # Configure Existing User
    def user_id(self):
        return int(input("User ID: "))

    def config_user(self, user_id):
        return int(input("Configuring {}\n\n1.) Manage Accounts\n2.) Check Balance\n3.) Transaction Logs\n4.) Delete User\n\nEnter Choice: ".format(user_id)))

    # Add User
    def add_user_num(self):
        return input("New Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("New PIN: ")

    # Delete User
    def del_user(self, user_id):
        return str(input("Delete {}? (Y/N)".format(user_id)))

    # Manage Accounts
    def manage_accounts(self, user_id):
        return int(input("Manage Accounts\n\n1.) Display Accounts\n2.) Add Account\n3.) Delete Account\n\nEnter Choice: "))

    # Display Accounts
    def display_accounts(self, accounts):
        print("Manage Accounts\n")
        for account in accounts:
            print(str(accounts.index(account)) + ".)", account)
        return int(input("\n\nEnter Command: "))

    # Add / Delete Account
    def accounts(self):
        return input("Accounts\n\n1.) Chequing\n\2.) Savings\n\3.) Term Savings\n\nEnter Choice: ")

    # Check Balance
    def get_balance(self, account, balance):
        return input("{} account balance: ${}. Press Enter to continue.".format(account, balance))
