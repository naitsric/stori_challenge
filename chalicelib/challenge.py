import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader


class Challenge:
    def __init__(self, df: DataFrame | TextFileReader):
        self._df = df

    def total_balance(self):
        return self._df["Tansaction"].sum()

    def count_transaction_by_month(self):
        self._df['Date'] = pd.to_datetime(self._df['Date'], format='%m/%d')
        self._df['Month'] = self._df['Date'].dt.strftime('%B')
        return self._df.groupby('Month').size().to_dict()

    def average_credit_amount(self):
        debits = self._df[self._df["Tansaction"] >= 0]
        return debits["Tansaction"].mean()

    def average_debit_amount(self):
        debits = self._df[self._df["Tansaction"] < 0]
        return debits["Tansaction"].mean()
