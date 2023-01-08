import pandas as pd
import datatest as dt
import unittest
from datetime import datetime , date
def setUpModule():
    global df
    with dt.working_directory(__file__):
        df = pd.read_csv('F:/UnitTesting/data_hindalco.csv')
        df['date'] = pd.to_datetime(df['date'])



class TestStock(dt.DataTestCase):

    maxDiff = None
    def test_open(self):
        self.assertValid(df['open'] , float)

    def test_high(self):
        self.assertValid(df['close'] , float)

    def test_low(self):
        self.assertValid(df['low'] , float)

    def test_close(self):
        self.assertValid(df['close'] , float)

    def test_volume(self):
        self.assertValid(df['volume'] , int)

    def test_instrument(self):
        self.assertValid(df['instrument'] , str)
    
    def test_datetime(self):
        self.assertValid(df['date'] , datetime)



if __name__ == "__main__":
    unittest.main()