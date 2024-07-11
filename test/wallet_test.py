
from unittest import main, TestCase
from src.wallet import Wallet


class WalletTest(TestCase):

    def setUp(self):
        self.my_wallet = Wallet()

    def test_deposit(self):
        # If money is added the balance should increase by the same amount
        self.assertEqual(0, self.my_wallet.get_balance(), "Initial balance should always be 0")
        self.my_wallet.deposit(155)
        self.assertEqual(155, self.my_wallet.get_balance(), "The new balance should be 155")

    def test_withdraw(self):
        # If money is withdrawn the balance should decrease by the same amount
        self.my_wallet.deposit(155)
        self.my_wallet.withdraw(80)
        self.assertEqual(75, self.my_wallet.get_balance(), "The new balance should be 75")


if __name__ == "__main__":
    main()
