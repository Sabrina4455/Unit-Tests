import unittest
import datetime


class Test(unittest.TestCase):

    def test_symbol(self):
        stocksymbol = 'GOOGL'
        self.assertLessEqual(len(stocksymbol), 7, msg="Symbol is greater than 7 alphabetical characters.")
        self.assertTrue(stocksymbol.isupper(), msg="Symbol is lowercase.")

    def test_chart(self):
        charttype = 2
        self.assertLessEqual(charttype, 2, msg="Chart type is greater than 2.")
        self.assertGreaterEqual(charttype, 1, msg="Chart type is less than 1.")
        self.assertTrue(type(charttype) == int, msg="Chart type must be numeric.")

    def test_time(self):
        timeseries = 3
        self.assertLessEqual(timeseries, 4, msg="Time series is greater than 4.")
        self.assertGreaterEqual(timeseries, 1, msg="Time series is less than 1.")
        self.assertTrue(type(timeseries) == int, msg="Time series must be numeric.")

    def test_start(self):
        start = datetime.datetime.strptime("2002-01-08", "%Y-%m-%d").date()
        test = datetime.date
        self.assertIsInstance(start, test, msg="Start date is not YYYY-MM-DD.")

    def test_end(self):
        end = datetime.datetime.strptime("2002-01-08", "%Y-%m-%d").date()
        test = datetime.date
        self.assertIsInstance(end, test, msg="End date is not YYYY-MM-DD.")


if __name__ == '__main__':
    unittest.main()
    
