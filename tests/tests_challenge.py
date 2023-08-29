import unittest

import pandas as pd

from chalicelib.challenge import Challenge


class TestChallenge(unittest.TestCase):
    """
    A class used to test the Challenge class.

    ...

    Methods
    -------
    setUp():
        Sets up the testing environment.
    test_total_balance():
        Tests the total_balance method of the Challenge class.
    test_count_transaction_by_month():
        Tests the count_transaction_by_month method of the Challenge class.
    test_average_credit_amount():
        Tests the average_credit_amount method of the Challenge class.
    test_average_debit_amount():
        Tests the average_debit_amount method of the Challenge class.
    """

    def setUp(self) -> None:
        """
        Sets up the testing environment. This method is called before each test.

        It creates a DataFrame and a Challenge object for use in the tests.
        """
        self.df = pd.DataFrame(
            {
                "Id": [0, 1, 2, 3],
                "Date": ["7/15", "7/28", "8/2", "8/13"],
                "Tansaction": [+60.5, -10.3, -20.46, +10],
            }
        )
        self.challenge = Challenge(self.df)

    def test_total_balance(self):
        """
        Tests the total_balance method of the Challenge class.

        The test asserts that the total balance calculated by the method is correct.
        """
        self.assertEqual(self.challenge.total_balance(), 39.74)

    def test_count_transaction_by_month(self):
        """
        Tests the count_transaction_by_month method of the Challenge class.

        The test asserts that the count of transactions per month calculated by the method is correct.
        """
        months = self.challenge.count_transaction_by_month()
        self.assertEqual(months["August"], 2)
        self.assertEqual(months["July"], 2)

    def test_average_credit_amount(self):
        """
        Tests the average_credit_amount method of the Challenge class.

        The test asserts that the average credit amount calculated by the method is correct.
        """
        self.assertEqual(self.challenge.average_credit_amount(), 35.25)

    def test_average_debit_amount(self):
        """
        Tests the average_debit_amount method of the Challenge class.

        The test asserts that the average debit amount calculated by the method is correct.
        """
        self.assertEqual(self.challenge.average_debit_amount(), -15.38)
