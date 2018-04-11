# This will be the file for the CLI controller

from views.cmd_interface.cmd_views import CommandLinePrompts

class CommandLineController:

    def __init__(self):
        self.view = CommandLinePrompts()

    def run(self):
        print('running')
