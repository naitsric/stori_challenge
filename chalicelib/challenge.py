import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader


class Challenge:
    """
    A class used to represent a Challenge.

    ...

    Attributes
    ----------
    _df : DataFrame | TextFileReader
        a Pandas DataFrame or TextFileReader object representing the data

    Methods
    -------
    total_balance():
        Returns the total balance of all transactions.
    count_transaction_by_month():
        Returns a dictionary with the number of transactions per month.
    average_credit_amount():
        Returns the average amount of credit transactions.
    average_debit_amount():
        Returns the average amount of debit transactions.
    """

    def __init__(self, df: DataFrame | TextFileReader):
        """
        Constructs all the necessary attributes for the Challenge object.

        Parameters
        ----------
            df : DataFrame | TextFileReader
                a Pandas DataFrame or TextFileReader object representing the data
        """
        self._df = df

    def total_balance(self) -> float:
        """
        Returns the total balance of all transactions.

        Returns
        -------
        float
            The sum of all transactions.
        """
        return self._df["Tansaction"].sum()

    def count_transaction_by_month(self) -> dict:
        """
        Returns a dictionary with the number of transactions per month.

        Returns
        -------
        dict
            A dictionary where keys are months and values are the number of transactions in that month.
        """
        self._df['Date'] = pd.to_datetime(self._df['Date'], format='%m/%d')
        self._df['Month'] = self._df['Date'].dt.strftime('%B')
        return self._df.groupby('Month').size().to_dict()

    def average_credit_amount(self) -> float:
        """
        Returns the average amount of credit transactions.

        Returns
        -------
        float
            The average value of credit transactions.
        """
        debits = self._df[self._df["Tansaction"] >= 0]
        return debits["Tansaction"].mean()

    def average_debit_amount(self) -> float:
        """
        Returns the average amount of debit transactions.

        Returns
        -------
        float
            The average value of debit transactions.
        """
        debits = self._df[self._df["Tansaction"] < 0]
        return debits["Tansaction"].mean()
