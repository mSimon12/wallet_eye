
import pandas as pd
from wallet import Wallet
from user import User


class ExpensesGroup(object):

    def __init__(self, owner_wallet: User):
        self.__group_wallet = Wallet()
        self.members_list = {owner_wallet.name}

    def get_group_balance(self):
        return self.__group_wallet.get_balance()

    def add_expense(self):
        pass

    def delete_expense(self, expense_name):
        pass

    def add_member(self):
        pass

    def delete_member(self, user_name):
        pass

    def get_members(self):
        return self.members_list