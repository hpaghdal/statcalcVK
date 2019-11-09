from Statistics.StandardDeviation import st_dev
from Calculator.Square import square


def pop_variance(lst):
    s = st_dev(lst)
    return square(s)
