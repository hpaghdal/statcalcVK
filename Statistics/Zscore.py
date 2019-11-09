from Statistics.PopulationMean import mean
from Statistics.StandardDeviation import st_dev
from Calculator.Division import division
from Calculator.Subtraction import subtraction


def zscore(lst):
    m = mean(lst)
    s = st_dev(lst)
    for z in lst:
        return division(subtraction(m, z), s)