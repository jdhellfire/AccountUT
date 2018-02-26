import unittest
from Account import Account


class AccountUT(unittest.TestCase):
    Withdraw_test_normal_test_data = [(0, 100), (1, 99), (50, 50), (99, 1), (100, 0)]

    def setUp(self):
        self.debit_account = Account.open_debit_account()
        self.account = Account.open_account()

    def check_debit_account_balance(self, value):
        self.assertEqual(value, self.debit_account.get_balance())

    def check_account_balance(self, value):
        self.assertEqual(value, self.account.get_balance())

    def test_get_balance_default_value_001(self):
        """
        GIVEN:Create a Debit Account
        WHEN: call get_balance interface
        THEN: get blance value will be 0
        """
        self.check_debit_account_balance(0)

    def test_get_balance_default_value_002(self):
        """
        GIVEN:Create a other Account
        WHEN: call get_balance interface
        THEN: get blance value will be 0
        """
        self.check_account_balance(0)

    def test_deposit_to_account_001(self):
        """
        GIVEN:Create a Debit Account
        WHEN: deposit money 100 and get balance
        THEN: get blance value will be 100
        """
        self.debit_account.deposit(100)
        self.check_debit_account_balance(100)

    def test_deposit_to_account_002(self):
        """
        GIVEN:Create other Account
        WHEN: deposit money 100 and get balance
        THEN: get blance value will be 100
        """
        self.account.deposit(100)
        self.check_account_balance(100)

    def test_deposit_to_account_003(self):
        """
        GIVEN:Create a Debit Account
        WHEN: deposit money -1 and get balance
        THEN:get blance value will be 0
        """
        self.debit_account.deposit(-1)
        self.check_debit_account_balance(0)

    def test_deposit_to_account_004(self):
        """
        GIVEN:Create other Account
        WHEN: deposit money -1 and get balance
        THEN:get blance value will be 0
        """
        self.account.deposit(-1)
        self.check_debit_account_balance(0)

    def test_withdraw_from_account_001(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[0,1,50,99,100] and get balance
        THEN: get blance value will be [100,99,50,1,0]
        """
        self.debit_account.deposit(100)

        for withdraw, balance in AccountUT.Withdraw_test_normal_test_data:
            self.debit_account.withdraw(withdraw)
            self.check_debit_account_balance(balance)
            self.debit_account.deposit(withdraw)

    def test_withdraw_from_account_002(self):
        """
        GIVEN:Create other Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[0,1,50,99,100] and get balance
        THEN: get blance value will be [100,99,50,1,0]
        """
        self.account.deposit(100)
        for withdraw, balance in AccountUT.Withdraw_test_normal_test_data:
            self.account.withdraw(withdraw)
            self.check_account_balance(balance)
            self.account.deposit(withdraw)

    def test_withdraw_from_account_003(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[-1,] and get balance
        THEN: get blance value will be 100
        """

    def test_withdraw_from_account_004(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[-1,] and get balance
        THEN: get blance value will be 100
        """

    def test_withdraw_from_account_005(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[101,] and get balance
        THEN: software will throw exception
        THEN:get blance value will be 100
        """

    def test_withdraw_from_account_006(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[101,] and get balance
        THEN: software will throw exception
        THEN:get blance value will be -1
        """


if __name__ == '__main__':
    unittest.main()
