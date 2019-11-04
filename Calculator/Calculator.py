from PopulationMean import mean
from Median import median
from Mode import mode
from StandardDeviation import st_dev
from ConfidenceInterval import confidenceinterval
class Calculator:
    result = 0

    def __init__(self):
        pass

    def popmean(self, a):
        self.result = mean(a)
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

    def confintv(self,a,b):
        self.result = confidenceinterval(a,b)
        return self.result