# This will be the main file for the CLI controller

from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts
from .controller_functions import ControllerFunctions

from model.account import AccountBalance
from model.chequing import Chequing
from model.savings import Savings

class CommandLineController:
    """
    Main command line controller file.
    This is where the controller functions are run.

    The view and model is manipulated and is able to communicate 
    with each other through this controller and its function file.

    """


    def __init__(self):
        self.view = CommandLinePrompts()
        self.functions = ControllerFunctions()
        self.startup = True
        self.cmd = "help"
        self.commands = {
            'help':          self.functions.display_help,
            'logout':        self.functions.logout,
            'user':          self.functions.usercfg,
            'account':       self.functions.accountcfg,
            'withdraw':      self.functions.withdraw,
            'deposit':       self.functions.deposit
        }

    # splits the user's input into separate chunks to process the commands
    def process_cmd(self, args):
        self.cmd = args.split()

    # Runs the CLI
    def run(self):
        # Determines the platform to determine what
        # command will be used to clear the terminal screen
        self.functions.determine_platform()

        while True:
            # User login
            self.functions.login()

            # Login help message
            if self.startup == True:
                print(self.view.startup_prompt())
                self.commands['help']()
                self.startup = False

            try:
                self.process_cmd(self.view.cmd_input(self.functions.teller_id))

                # Runs the commands that are stored in the command dictionary
                if self.cmd[0] == 'exit':
                    system(self.functions.clear_cmd)
                    break
                elif self.cmd[0] == 'logout':
                    self.startup = True
                    self.commands[self.cmd[0]]()
                elif len(self.cmd) == 1:
                    self.commands[self.cmd[0]]()
                elif len(self.cmd) > 1:
                    self.commands[self.cmd[0]](self.cmd)
                else:
                    self.view.error("No command.")

            except KeyError:
                self.view.error('\'{}\' not a command.'.format(' '.join(self.cmd)))
            except IndexError:
                pass


