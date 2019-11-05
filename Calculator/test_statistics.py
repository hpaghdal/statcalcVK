import unittest
# from Calculator.Calculator import Calculator
from Calculator import Calculator


# from CsvReader.CsvReader import CsvReader
# import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_mean_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.calculator.popmean(data), 3)

    def test_median_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.calculator.med(data), 3.5)

    def test_mode_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6, 3]
        self.assertEqual(self.calculator.mod(data), 3)

    def test_standard_deviation_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.calculator.stddev(data), 1.5811388300841898)

    def test_confidence_interval_calculator(self):
        data = [1, 2, 3, 4, 5]
        conf = 95
        self.assertEqual(self.calculator.confintv(data, conf), (4.39, 1.61))

    def test_zscore_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.calculator.z_score(data), 1.5811388300841898)


if __name__ == '__main__':
    unittest.main()
