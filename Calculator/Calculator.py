from PopulationMean import mean
from Median import median
from Mode import mode


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
