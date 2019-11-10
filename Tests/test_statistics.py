import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/StatCalcData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Population_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['mean']))
        self.assertEqual(self.statistics.newmean(lst), result)

    def test_Sample_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        x, z = self.statistics.sammean(lst)

        self.assertEqual(x, z)

    def test_Median_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['median']))
        self.assertEqual(self.statistics.med(lst), result)

    def test_Mode_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['mode']))
        self.assertEqual(self.statistics.mod(lst), result)

    def test_Population_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['stdev']))
        self.assertEqual(self.statistics.stddev(lst), result)

    def test_Sample_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        x, z = self.statistics.sampstdev(lst)
        x = round(x, 3)
        z = round(z, 3)

        self.assertEqual(x, z)

    def test_confidence_interval_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        conf = 95
        self.assertEqual(self.statistics.confintv(lst, conf), (132.67, 121.07))

    def test_zscore_calculator(self):
        data = [1, 2, 3, 4, 5]
        x = round(-1.2649110640673518, 7)
        self.assertEqual(self.statistics.z_score(data), x)

    def test_population_variance_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['pop_variance']))
        self.assertEqual(self.statistics.pvariance(lst), result)

    def test_proportion_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        for column in answer:
            result = float((column['proportion']))
        self.assertEqual(self.statistics.proportion(lst), result)


if __name__ == '__main__':
    unittest.main()
