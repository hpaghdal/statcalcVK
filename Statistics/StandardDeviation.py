import math

from Statistics.PopulationMean import mean


def st_dev(lst):
    diffs = 0
    m = mean(lst)
    for l in lst:
        diffs += (l - m) ** 2
    return (diffs / (len(lst) - 1)) ** 0.5
