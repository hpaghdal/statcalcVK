import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from CsvReader.CsvDataAppend import data_add


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/StatCalcData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Population_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.newmean(lst), float((column['mean'])))
            self.assertNotEqual(self.statistics.newmean(lst), float((column['mean'])) * 2, "Mean does not match")

    def test_Sample_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = data_add(test_data)
        x, z = self.statistics.sammean(lst)
        self.assertEqual(x, z)
        self.assertNotEqual(x, z * 2, "Sample Mean does not match")

    def test_Median_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.med(lst), float((column['median'])))
            self.assertNotEqual(self.statistics.med(lst), float((column['median'])) + 2, "Incorrect Median")

    def test_Mode_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.mod(lst), float((column['mode'])))
            self.assertNotEqual(self.statistics.mod(lst), float((column['mode'])) - 2, "Incorrect Mode")

    def test_Population_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.stddev(lst), float((column['stdev'])))
            self.assertNotEqual(self.statistics.stddev(lst), float((column['stdev'])) * 3, "Wrong Pop Std Deviation")

    def test_Sample_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = data_add(test_data)
        x, z = self.statistics.sampstdev(lst)
        x = round(x, 3)
        z = round(z, 3)
        self.assertEqual(x, z)
        self.assertNotEqual(x, z * 2, "Sample Std Deviation is incorrect")

    def test_confidence_interval_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = data_add(test_data)
        conf = 95
        self.assertEqual(self.statistics.confintv(lst, conf), (132.67, 121.07))
        self.assertNotEqual(self.statistics.confintv(lst, conf), (134.67, 123.07), "Incorrect Confidence Interval")

    def test_zscore_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.z_score(lst), float((column['zscore'])))
            self.assertNotEqual(self.statistics.z_score(lst), float((column['zscore'])) * 2, "Incorrect Z Score")

    def test_population_variance_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.pvariance(lst), float((column['pop_variance'])))
            self.assertNotEqual(self.statistics.pvariance(lst), float((column['pop_variance'])) - 3, "Wrong Pop Var")

    def test_proportion_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.proportion(lst), float((column['proportion'])))
            self.assertNotEqual(self.statistics.proportion(lst), float((column['proportion'])) - 2, "Wrong Proportion")

    def test_variance_population_proportion_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.vpop_proportion(lst), float((column['var_pop_prop'])))
            self.assertNotEqual(self.statistics.vpop_proportion(lst), float((column['var_pop_prop'])) - 2,
                                "WrongResult")

    def test_variance_sample_proportion_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = data_add(test_data)
        x = self.statistics.vsamp_proportion(lst)
        self.assertEqual(x, x)
        self.assertNotEqual(x, x + 2, "Wrong Var Samp Proportion")

    def test_correlation_coefficient_calculator(self):
        test_data = CsvReader('Tests/Data/SampleData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        x_data = []
        y_data = []
        for row in test_data:
            x = int(row['x'])
            x_data.append(x)
            y = int(row['y'])
            y_data.append(y)
        z = self.statistics.corcof(x_data, y_data)
        for column in answer:
            self.assertEqual(z, float((column['corr_coff'])))
            self.assertNotEqual(z, float((column['corr_coff'])) + 1, "Wrong Corr Coefficient")

    def test_pvalue_calculator(self):
        test_data = CsvReader('Tests/Data/Ztable.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        z_data = []
        p_data = []
        for row in test_data:
            x = float(row['z_score'])
            z_data.append(x)
            y = float(row['p_value'])
            p_data.append(y)
        x = self.statistics.p_value(z_data, p_data)
        for column in answer:
            self.assertEqual(x, float((column['p_value'])))
            self.assertNotEqual(x, float((column['p_value'])) - 3, "Incorrect P Value")


if __name__ == '__main__':
    unittest.main()
