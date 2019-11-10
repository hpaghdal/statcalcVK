from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Square import square
from Statistics.PopulationMean import mean
from Calculator.Sqrt import root


def st_dev(lst):
    diffs = 0
    m = mean(lst)
    for l in lst:
        diffs = addition(diffs,square(subtraction(l, m)))
        sd = division(diffs, subtraction(1, len(lst)))
        x = root(sd)
    return x
