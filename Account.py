class Account:
    def __init__(self, is_debit):
        self.__is_debit = is_debit
        self.__balance = 0

    @staticmethod
    def open_debit_account():
        return Account(True)

    @staticmethod
    def open_account():
        return Account(False)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance = self.__balance if amount < 0 else self.__balance + amount

    def withdraw(self, amount):
        if amount < 0:
            return

        if self.__is_debit and self.get_balance() < amount:
            raise InsufficientFundsException()

        self.__balance -= amount


class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Account Exception'
