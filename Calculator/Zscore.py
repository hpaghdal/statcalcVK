from PopulationMean import mean
from StandardDeviation import st_dev

def zscore(lst):
    m = mean(lst):
    s = st_dev(lst):
    return (lst - m) / s
