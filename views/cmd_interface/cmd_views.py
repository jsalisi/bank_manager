import getpass

class CommandLinePrompts:
    """ 
    
    Prompts that are displayed on the command line interface.

    """

    # Command Input
    def cmd_input(self, teller_id):
        return input('\n[{}.BoJoBank]: '.format(teller_id))

    def  startup_prompt(self):
        return "\nType \'help\' for more information."

    # Help
    def help(self):        
        cmd_withdraw =   '      withdraw [account number] [amount]              - Withdraw money from an account'
        cmd_deposit =    '      deposit  [account number] [amount]              - Deposit money to an account\n'

        cmd_logout =     '      logout                                          - Logs out of account'
        cmd_help =       '      help                                            - Displays list of all commands'
        cmd_exit =       '      exit                                            - Closes the program'
        return "\n{}\n{}\n{}\n{}\n{}".format(cmd_withdraw, cmd_deposit, cmd_logout, cmd_help, cmd_exit)

    def usercfg_help(self):
        cmd_usercfg =    '      user [info / edit / add / del]                  - Opens the user configuration menu'
        return "\n{}".format(cmd_usercfg)

    def accountcfg_help(self):
        cmd_accountcfg = '      account [info / transact / bal / add / del]     - Opens the account configuration menu'
        return "\n{}".format(cmd_accountcfg)

    def withdraw_help(self):
        return '\nwithdraw [account number] [amount]              - Withdraw money from an account'

    def deposit_help(self):
        return '\ndeposit  [account number] [amount]              - Deposit money to an account'

    # Display Error
    def error(self, err):
        print("\n" + err, end = ' ')
        return input('Press Enter to continue.')

    # Login
    def login_id(self):
        return input("Login: ")

    def login_passwd(self):
        return getpass.getpass("Password: ")

    # Configure Existing User
    def user_id(self):
        return input("\nEnter card number: ")

    def config_user(self, user_id):
        return input("\nCard Number: {}\n\n1.) Check Balance\n2.) Transaction Logs\n3.) Delete User\n\nEnter Choice: ".format(user_id))

    # Add User
    def add_user_num(self):
        return input("\nNew Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("New PIN: ")

    # Delete User
    def del_user(self, user_id):
        return str(input("\nDelete {}? (Y/N)".format(user_id)))

    # Display Accounts
    def display_accounts(self, accounts, user_id):
        print("\nAccounts\nCard Number: {}\n".format(user_id))
        for account in accounts:
            print(str(accounts.index(account)+1) + ".)", account)
        return account[int(input("\nEnter Choice: "))-1]

    # Add / Delete Account
    def accounts(self):
        return input("\nAccounts\n\n1.) Chequing\n\2.) Savings\n\3.) Term Savings\n\nEnter Choice: ")

    # Check Balance
    def get_balance(self, account, balance):
        return input("{} Balance: ${}. Press Enter to continue.".format(account, balance))
