from Calculator.Calculator import Calculator
from Statistics.PopulationMean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import st_dev
from Statistics.ConfidenceInterval import confidenceinterval
from Statistics.Zscore import zscore
from Statistics.PopulationVariance import pop_variance
from Statistics.SampleStandardDeviation import sampst_dev
from Statistics.SampleMean import samp_mean
from CsvReader.CsvReader import CsvReader
from Statistics.Proportion import proportion
from Statistics.vPopProportion import v_pop_proportion
from Statistics.vSampProportion import v_samp_proportion
from Statistics.CorrelationCoefficient import Pop_correlation_coefficient
from Statistics.PValue import pvalue


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/StatCalcData.csv').data
        super().__init__()

    def newmean(self, a):
        self.result = mean(a)
        return self.result

    def sammean(self, a):
        self.result = samp_mean(a)
        return self.result

    def med(self, a):
        self.result = median(a)
        return self.result

    def mod(self, a):
        self.result = mode(a)
        return self.result

    def stddev(self, a):
        self.result = st_dev(a)
        return self.result

    def sampstdev(self, a):
        self.result = sampst_dev(a)
        return self.result

    def confintv(self, a, b):
        self.result = confidenceinterval(a, b)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)
        return self.result

    def pvariance(self, a):
        self.result = pop_variance(a)
        return self.result

    def proportion(self, a):
        self.result = proportion(a)
        return self.result

    def vpop_proportion(self, a):
        self.result = v_pop_proportion(a)
        return self.result

    def vsamp_proportion(self, a):
        self.result = v_samp_proportion(a)
        return self.result

    def corcof(self):
        return Pop_correlation_coefficient()

    def p_value(self):
        return pvalue()
