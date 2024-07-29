
from unittest import main, TestCase
from src.wallet import Wallet, Transaction


class WalletTest(TestCase):

    def setUp(self):
        self.my_wallet = Wallet()

    def test_deposit(self):
        # If money is added the balance should increase by the same amount
        self.assertEqual(0, self.my_wallet.get_balance(), "Initial balance should always be 0")
        test_transaction = Transaction(155, "withdraw_value")
        self.my_wallet.put_money(test_transaction)
        self.assertEqual(155, self.my_wallet.get_balance(), "The new balance should be 155")

    def test_withdraw(self):
        # If money is withdrawn the balance should decrease by the same amount
        test_transaction = Transaction(155, "withdraw_value")
        self.my_wallet.put_money(test_transaction)
        test_transaction = Transaction(80, "withdraw_value")
        self.my_wallet.grab_money(test_transaction)
        self.assertEqual(75, self.my_wallet.get_balance(), "The new balance should be 75")


if __name__ == "__main__":
    main()
