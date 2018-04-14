Getting Started:

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