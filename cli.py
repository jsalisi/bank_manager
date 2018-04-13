# This is the file that runs the Command Line Interface

from controller.cmd_controller import CommandLineController

def main():
    cmd_ctrl = CommandLineController()
    cmd_ctrl.run()

if __name__ == "__main__":
    main()

