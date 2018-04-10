# This is the file that runs the ATM

from tkinter import *
from controller.atm_controller.atm_controller import ATMController
from controller.atm_controller import *
from views.atm_interface import *


def main():
    root = Tk()
    ATMController(root)
    mainloop()

if __name__ == "__main__":
    main()
