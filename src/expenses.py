
import pandas as pd
from wallet import Wallet, Transaction
from user import User


class ExpensesGroup(object):

    def __init__(self, owner_wallet: User):
        self.__group_wallet = Wallet()
        self.__members_list = {owner_wallet.name: Wallet()}
        self.__expenses = pd.DataFrame(columns=['paid_by', 'participants', 'transaction'])
        self.next_id = 1

    def get_group_balance(self):
        print(self.__expenses)
        return self.__group_wallet.get_balance()

    def add_expense(self, value, paid_by, participants, reason):
        new_transaction = Transaction(description=reason, value=value)
        self.__expenses.loc[self.next_id] = [paid_by, participants, new_transaction]
        self.next_id += 1

        self.__group_wallet.grab_money(new_transaction)

    def delete_expense(self, expense_id):
        expense_transaction = self.__expenses.loc[expense_id, 'transaction']
        self.__group_wallet.put_money(expense_transaction)

        self.__expenses.drop(index=expense_id, inplace=True)

    def add_member(self, new_member: str):
        self.__members_list[new_member] = Wallet()

    def remove_member(self, user_name):
        # Removing a member excludes him from all transactions
        pass

    def get_members(self):
        return self.__members_list
