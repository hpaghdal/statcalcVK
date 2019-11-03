from Mean import mean

from StandardDeviation import st_dev

class Calculator:
    result = 0

    def __init__(self):
        pass

    def popmean(self, a):
        self.result = mean(a)
        return self.result

    def stdev(self, a):
        self.result = st_dev(a)
        return self.result
