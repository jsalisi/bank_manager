import getpass

class CommandLinePrompts:
    """ 
    
    This is file that contains all the prompts displayed on the command line interface.
        
    """

    
    # Level 0 Menu
    def login_id(self):
        return input("\nID: ")

    def login_passwd(self):
        return getpass.getpass("Password: ")

    # Level 1 Menu
    def main_prompt(self):
        return input("\n\
                      Bank Manager\n\
                      \n\
                      1.) Manage Users\n\
                      2.) Logout\n\
                      \n\
                      Enter Command: ")

    # Level 2 Menu
    def manage_users(self):
        return input("\n\
                      Manage Users\n\
                      \n\
                      1.) Configure Existing User\n\
                      2.) Add User\n\
                      3.) Delete User\n\
                      \n\
                      7.) Return\n\
                      \n\
                      Enter Command: ")

    # Level 3 Menus
    def add_user_num(self):
        return input("\nNew Bank Number: ")

    def add_user_pin(self):
        return getpass.getpass("\nNew PIN: ")

    def del_user(self, user_id):
        return input("Delete {}? (Y/N)".format(user_id))

    def user_id(self):
        return input("User ID: ")

    def config_user(self, user_id):
        return input("\n\
                     Configuring {}\n\
                     \n\
                     1.) Manage Accounts\n\
                     2.) Transaction Logs\n\
                     3.) Delete User\n\
                     \n\
                     7.) Return\n\
                      \n\
                      Enter Command: ".format(user_id))

    # Level 4 Menus
    def manage_accounts(self):
        return input("\n\
                     Manage Accounts\n\
                     \n\
                     1.) Display Accounts\n\
                     2.) Add Account\n\
                     3.) Delete Account\n\
                     \n\
                     7.) Return\n\
                      \n\
                      Enter Command: ")

    # Level 5 Menu
    def display_accounts(self, accounts):
        print("\nManage Accounts\n")
        for account in accounts:
            print(str(accounts.index(account)) + ".)", account)
        return input("\n\nEnter Command: ")

    def accounts(self):
        input("\n\
              Accounts\n\
              \n\
              1.) Chequing\n\
              2.) Savings\n\
              3.) Term Savings\n\
              \n\
              7.) Return\n\
              \n\
              Enter Command: ")
