from wallet import Wallet


class User(object):

    def __init__(self, name: str):
        self.name = name
        self.wallets = {}
        self.expenses_groups = []

    def add_wallet(self, wallet_name: str):
        self.wallets[wallet_name] = Wallet()

    def create_expense_group(self):
        pass


