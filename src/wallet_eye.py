from wallet import Wallet
from expenses import ExpensesGroup
from user import User

if __name__ == "__main__":
    my_user = User("main")
    my_user.add_wallet("pocket")

    print(f"User {my_user.name} balance on wallets:")
    for w in my_user.wallets:
        print(f"\tWallet '{w}': {my_user.wallets[w].get_balance()}")

    eurotrip = ExpensesGroup(my_user)
