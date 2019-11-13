from Statistics.PopulationMean import mean
from Statistics.StandardDeviation import st_dev
from Calculator.Division import division
from Calculator.Subtraction import subtraction


def zscore(lst):
    raw_value = 16
    m = mean(lst)
    s = st_dev(lst)
    return division(subtraction(m, raw_value), s)