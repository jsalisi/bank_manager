from time import localtime, strftime
from accounts.constants.transaction_types import *


class TransactionLog:
    """ Records transactions per user and stores data in a file. """

    def __init__(self):
        self.tr_logs = []

    def add_log(self, acc_num, tr_type, amount, c_balance):
        if (tr_type == DEPOSITING) or (tr_type == PAYING_INTEREST):
            n_balance = c_balance + amount
        elif (tr_type == WITHDRAWING) or (tr_type == CHARGING_FEE) or (tr_type == CHARGING_INTEREST):
            n_balance = c_balance - amount

        log_str = ("{},{},{},{},{},{}\n"
                   .format(strftime("%d %b %Y %H:%M:%S", localtime()),
                           str(acc_num),
                           str(c_balance),
                           str(tr_type),
                           str(amount),
                           str(n_balance)))

        self.tr_logs.append(log_str)

        fh = open("./accounts/transactions/logs/{}_logs.csv".format(acc_num), "a")
        fh.writelines(self.tr_logs)
        fh.close()

    def show_transactions(self, acc_num):
        try:
            with open("./accounts/transactions/logs/{}_logs.csv".format(acc_num), "r") as user_logs:
                for line in user_logs:
                    acc_log = line.rstrip().split(",")
                    print(acc_log)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    a = TransactionLog()
    a.add_log(1234, "Withdraw", 40, 50)
    a.add_log(1234, "Deposit", 20, 50)
    a.add_log(1234, "Withdraw", 10, 20)
    print(a.tr_logs)
