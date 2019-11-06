from Statistics.PopulationMean import mean
from Statistics.StandardDeviation import st_dev

def zscore(lst):
    m = mean(lst)
    s = st_dev(lst)
    for z in lst:
        return (z - m) / s
