# This will be the file for the CLI controller

from views.cmd_interface.cmd_views import CommandLinePrompts as prompts


class CommandLineController:

    def __init__(self):
        self.view = prompts()

    def login(self):
        logged_in = False
        while logged_in is False:
            id = self.view.login_id()
            passwd = self.view.login_passwd()
            print(id, passwd)

            if int(id) == 12345 and int(passwd) == 12345:
                logged_in = True
                return True

    def run(self):
        try:
            # Login
            logged_in = self.login()

            if logged_in is True:
                p1 = self.view.main_prompt()

                # Managing Users
                if p1 == 1:
                    p2 = self.view.manage_users()

                    # Configuring Users
                    if p2 == 1:
                        u_id = self.view.user_id()
                        c_user = self.view.config_user(u_id)
                    
                    # Adding User
                    elif p2 == 2:
                        new_user = self.view.add_user_num()
                        new_pin = self.view.add_user_pin()
                        print(new_user, new_pin)
                    
                    # Deleting User
                    elif p2 == 3:
                        u_id = self.view.user_id
                        res = self.view.del_user(u_id)

                    # Return to previous setting
                    elif p2 == 0:
                        pass


        except ValueError:
            print(self.view.error(str(ValueError)))
