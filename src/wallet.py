import datetime


class Transaction(object):
    """
        Each transaction is unique by a timestamp and is composed by description and absolute value
    """

    def __init__(self, description: str, value: float):
        now = datetime.datetime.now()
        self.date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.description = description
        self.value = abs(value)


class Wallet(object):

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value


if __name__ == "__main__":
    trans = Transaction("my_first_payment", 15)
