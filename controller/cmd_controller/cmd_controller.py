# This will be the file for the CLI controller

from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts
from .controller_functions import ControllerFunctions


class CommandLineController:

    def __init__(self):
        self.view = CommandLinePrompts()
        self.functions = ControllerFunctions()
        self.cmd = "help"
        self.commands = {
            'help':          self.functions.display_help,
            'logout':        self.functions.logout,
            'main':          self.functions.main_menu,
            'userconfig':    self.functions.usercfg,
            'useradd':       self.functions.useradd,
            'userdel':       self.functions.userdel,
            'accountconfig': self.functions.accountcfg,
            'withdraw':      self.functions.withdraw,
            'deposit':       self.functions.deposit
        }

    def run(self):
        try:
            while True:
                self.functions.login()
                
                try:
                    self.cmd = self.view.cmd_input()
                    self.commands[self.cmd]()

                except KeyError:
                    self.view.error('\'{}\' not a command.'.format(self.cmd))

        except:
            system('cls')
            self.view.error("Something went wrong.")

            
