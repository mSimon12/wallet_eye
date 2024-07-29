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
    eurotrip.add_expense(150, paid_by="Marcelo", participants=["Marcelo, Carlos, Joao, Camila"], reason="lunch")
    eurotrip.add_expense(10, paid_by="Marcelo", participants=["Carlos, Camila"], reason="ice cream")
    eurotrip.add_expense(20, paid_by="x", participants=["a, Camila"], reason="potatoes")

    balance = eurotrip.get_group_balance()
    print(f"Expense balance is € {balance}")

    eurotrip.delete_expense(3)

    balance = eurotrip.get_group_balance()
    print(f"Expense balance is € {balance}")

