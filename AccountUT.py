import unittest
from Account import Account


class AccountUT(unittest.TestCase):
    def setUp(self):
        self.debit_account = Account.open_debit_account()

    def test_get_balance_default_value_001(self):
        """
        GIVEN:Create a Debit Account
        WHEN: call get_balance interface
        THEN: get blance value will be 0
        """
        self.assertEqual(0, self.debit_account.get_balance())

    def test_get_balance_default_value_002(self):
        """
        GIVEN:Create a other Account
        WHEN: call get_balance interface
        THEN: get blance value will be 0
        """
        pass

    def test_deposit_to_account_001(self):
        """
        GIVEN:Create a Debit Account
        WHEN: deposit money 100 and get balance
        THEN: get blance value will be 100
        """

        pass

    def test_deposit_to_account_002(self):
        """
        GIVEN:Create other Account
        WHEN: deposit money 100 and get balance
        THEN: get blance value will be 100
        """
        pass

    def test_deposit_to_account_003(self):
        """
        GIVEN:Create a Debit Account
        WHEN: deposit money -1 and get balance
        THEN:get blance value will be 0
        """
        pass

    def test_deposit_to_account_004(self):
        """
        GIVEN:Create other Account
        WHEN: deposit money -1 and get balance
        THEN:get blance value will be 0
        """
        pass

    def test_withdraw_from_account_001(self):
        """
        GIVEN:Create a Debit Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[0,1,50,99,100] and get balance
        THEN: get blance value will be [100,99,50,1,0]
        """

    def test_withdraw_from_account_002(self):
        """
        GIVEN:Create other Account
        GIVEN:deposit money 100
        WHEN: Withdraw money in case:[0,1,50,99,100] and get balance
        THEN: get blance value will be [100,99,50,1,0]
        """

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
