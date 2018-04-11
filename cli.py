# This is the file that runs the Command Line Interface

import getpass
from controller.cmd_controller import *
from views.cmd_interface import *

test = getpass.getpass("\nPassword: ")

print("\n", test)
