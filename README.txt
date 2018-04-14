Getting Started:

Pyinstaller simply does not work with our project directory. to start using our files. you will be
required to open up a CMD.

path to main project directory and enter <python cli.py> to use the bank cli, or <python atm.py> to
open up the atm GUI.




Command Line Interface
----------------------------------------------------------------------------------------------------
Defaults (Can use these to test):

Username: admin 
Password: 1234

Card Number: 1234123412341234
----------------------------------------------------------------------------------------------------

Once logged in, all system commands will be displayed (example 1).

Example 1:
----------------------------------------------------------------------------------------------------
System Commands:


      user [info / chk / add]                         - Opens the user configuration menu

      account [info / transact / bal / add]           - Opens the account configuration menu

      withdraw [account number] [amount]              - Withdraw money from an account
      deposit  [account number] [amount]              - Deposit money to an account

      logout                                          - Logs out of account
      help                                            - Displays list of all commands
      exit                                            - Closes the program
----------------------------------------------------------------------------------------------------

Enter a command to open a menu related to the command.
Text within brackets, '[]', specify a sub-command to be run with the main command  (example 2).

Example 2:
----------------------------------------------------------------------------------------------------
[admin.BoJoBank]: user chk
----------------------------------------------------------------------------------------------------

You will then be able to choose from the prompts displayed after entering the card number
you wish to use (example 3).

Example 3:
----------------------------------------------------------------------------------------------------
Enter card number: 1234123412341234

Card Number: 1234123412341234

1.) Check Balance
2.) Transaction Logs

Enter Choice:
----------------------------------------------------------------------------------------------------




----------------------------------------------ATM---------------------------------------------------

.EXE not available because pyinstaller is simply too dumb to translate relative file paths to 
absolute file paths.

you log in with a 16 digit login info. default accounts are available in /model/accounts/accounts_login.csv

you can choose which bank account you want to access (chequing or savings). If there is no chequing,

it will alert to you that this account does not have a chequings acc. or vice versa. since its a basic bank acc

it is impossible to have a card, but not have either savings or a chequings


----------------------------------------------MVC---------------------------------------------------

Model:
	Our ATM GUI and CLI both utilizes the same model.
	In our model, there will be four databases:
		- login_db: responsible for client account login credentials
		- teller_db: responsible for teller account login credentials (used for CLI only)
		- account_db: all acount information of the client
		- transaction_log: all account transactions of the client
	These databases are loaded from three separate csv files:
		login_db loads from accoun_login.csv
		teller_db loads from teller_login.csv
		account_db loads from account_info.csv
		transaction logs of each client can be loaded from their own respective xxxxxx_log.csv
			- all of these csv files can be found in /model/accounts or /model/transactions

View:
	two views are offered in this project:
	- cliview.py (for cli)
	- atmview.py (for atm)
		- all views can be found in /views/atm_interface or /views/cmd_interface

controller:
	two controllers are offered in this project:
	- atm_controller.py
	- cmd_controller.py
		- all controllers can be found in /controller/atm_controller or /controller/cmd_controller
