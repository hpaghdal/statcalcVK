from Statistics.PopulationMean import mean
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Addition import addition

def proportion(lst):
    m = mean(lst)
    lower_limit = multiplication(0.8, m)
    higher_limit = multiplication(1.2, m)
    count = 0
    for i in lst:
        if (i > higher_limit) or (i < lower_limit):
            count = addition(count, 1)
    p = round(division(count, float(len(lst))), 8)
    return p
