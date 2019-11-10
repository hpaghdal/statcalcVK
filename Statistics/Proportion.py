from Statistics.PopulationMean import mean
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Addition import addition


def proportion(lst):
    count = 0
    for i in lst:
        if (i % 2) == 0:
            count = addition(count, 1)
        prop = division(count, len(lst))
    return prop
