import getpass

class CommandLinePrompts:
    """ 
    
    Prompts that are displayed on the command line interface.

    """

    # Command Input
    def cmd_input(self, teller_id):
        return input('\n[{}.BoJoBank]: '.format(teller_id))

    def  startup_prompt(self):
        return "\nSystem Commands:\n"

    # Help view functions
    def help(self):        
        cmd_withdraw =   '      withdraw [account number] [amount]              - Withdraw money from an account'
        cmd_deposit =    '      deposit  [account number] [amount]              - Deposit money to an account\n'

        cmd_logout =     '      logout                                          - Logs out of account'
        cmd_help =       '      help                                            - Displays list of all commands'
        cmd_exit =       '      exit                                            - Closes the program'
        return "\n{}\n{}\n{}\n{}\n{}".format(cmd_withdraw, cmd_deposit, cmd_logout, cmd_help, cmd_exit)

    def usercfg_help(self):
        cmd_usercfg =    '      user [info / chk / add]                         - Opens the user configuration menu'
        return "\n{}".format(cmd_usercfg)

    def accountcfg_help(self):
        cmd_accountcfg = '      account [info / transact / bal / add]           - Opens the account configuration menu'
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
        return input("\nCard Number: {}\n\n1.) Check Balance\n2.) Transaction Logs\n\nEnter Choice: ".format(user_id))

    # Add User
    def new_fname(self):
        return input('\nFirst name: ')

    def new_lname(self):
        return input('Last name: ')

    def add_user_num(self):
        return input("\nNew Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("New PIN: ")

    # Display Accounts
    def display_accounts(self, accounts, user_id):
        print("\nAccounts\nCard Number: {}\n".format(user_id))
        for account in accounts:
            print(str(accounts.index(account)+1) + ".)", account)
        return int(input("\nEnter Choice: "))

    # Add a type of account
    def accounts(self):
        return input("\nAccounts\n\n1.) Chequing\n2.) Savings\n\nEnter Choice: ")

    # Check Balance
    def get_balance(self, account, balance):
        return input("\n{} Balance: ${}. Press Enter to continue.".format(account, balance))

    # Display user info
    def user_info(self, acc_db):
        print()
        for ac in acc_db:
            print(ac)