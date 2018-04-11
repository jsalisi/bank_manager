# This will be the file for the CLI controller

from os import system
from views.cmd_interface.cmd_views import CommandLinePrompts
from .controller_functions import ControllerFunctions
from model import (Chequing, Savings, TermSavings)

class CommandLineController:

    def __init__(self):
        self.view = CommandLinePrompts()
        self.functions = ControllerFunctions()
        self.show_help = True
        self.cmd = "help"
        self.commands = {
            'help':          self.functions.display_help,
            'logout':        self.functions.logout,
            'usrcfg':        self.functions.usercfg,
            'accountcfg':    self.functions.accountcfg,
            'withdraw':      self.functions.withdraw,
            'deposit':       self.functions.deposit
        }

    def process_cmd(self, args):
        self.cmd = args.split()

    def run(self):
        while True:
            self.functions.login()

            if self.show_help == True:
                self.commands['help']()
                self.show_help = False
            else:
                system('cls')

            try:
                self.process_cmd(self.view.cmd_input(self.functions.teller_id))

                if self.cmd[0] == 'exit':
                    system('cls')
                    break
                elif self.cmd[0] == 'logout':
                    self.commands[self.cmd[0]]()
                    self.show_help = True
                elif self.cmd[0] == 'help':
                    self.show_help = True
                elif len(self.cmd) == 1:
                    self.commands[self.cmd[0]]()
                elif len(self.cmd) > 1:
                    self.commands[self.cmd[0]](self.cmd)
                else:
                    self.view.error("No command.")

            except KeyError:
                self.view.error(
                    '\'{}\' not a command.'.format(' '.join(self.cmd)))
