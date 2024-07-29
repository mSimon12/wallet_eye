import datetime


class Transaction(object):
    """
        Each transaction is unique by a timestamp and is composed by description and absolute value
    """

    def __init__(self, value: float, description: str = "", origin: str = "", dest: str = ""):
        now = datetime.datetime.now()
        self.__date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.__description = description
        self.__value = abs(value)
        self.__source = origin
        self.__destination = dest

    def get_value(self):
        return self.__value


class Wallet(object):

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def put_money(self, exchange: Transaction):
        self.__balance += exchange.get_value()

    def grab_money(self, exchange: Transaction):
        self.__balance -= exchange.get_value()

    def generate_report(self, begin_date, end_date):
        pass


if __name__ == "__main__":
    trans = Transaction("my_first_payment", 15)
