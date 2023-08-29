import unittest

import pandas as pd

from chalicelib.challenge import Challenge


class TestChallenge(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame(
            {
                "Id": [0, 1, 2, 3],
                "Date": ["7/15", "7/28", "8/2", "8/13"],
                "Tansaction": [+60.5, -10.3, -20.46, +10],
            }
        )
        self.challenge = Challenge(self.df)

    def test_total_balance(self):
        self.assertEqual(self.challenge.total_balance(), 39.74)

    def test_count_transaction_by_month(self):
        months = self.challenge.count_transaction_by_month()
        self.assertEqual(months["August"], 2)
        self.assertEqual(months["July"], 2)

    def test_average_credit_amount(self):
        self.assertEqual(self.challenge.average_credit_amount(), 35.25)

    def test_average_debit_amount(self):
        self.assertEqual(self.challenge.average_debit_amount(), -15.38)

