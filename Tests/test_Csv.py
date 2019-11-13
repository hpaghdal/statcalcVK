import unittest
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/StatCalcData.csv')

    def test_csv_file(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        i = 0
        for row in test_data:
            i = i + 1
            y = int(row['Value 1'])
            lst.append(y)
        self.assertEqual(i, 600)  # To check if the csv reader reads all 600 lines of data


if __name__ == '__main__':
    unittest.main()
