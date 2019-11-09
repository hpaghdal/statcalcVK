from Statistics.PopulationMean import mean
from Calculator.Multiplication import multiplication
from Calculator.Division import division


def proportion(lst):
    # Any number 20% above or 20% below the mean is being considered as outlier.
    # This function returns the proportion of the population which is outlier.
    m = mean(lst)
    lower_limit = multiplication(0.8, m)
    higher_limit = multiplication(1.2, m)
    count = 0
    for i in lst:
        if (i > higher_limit) or (i < lower_limit):
            count = count + 1
    p = round(division(count, float(len(lst))), 8)
    return p
