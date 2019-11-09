from Statistics.StandardDeviation import st_dev
from Calculator.Square import square
from Statistics.PopulationMean import mean


def pop_variance(lst):
    s = st_dev(lst)
    return square(s)