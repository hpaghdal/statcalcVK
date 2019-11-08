import math
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Sqrt import root
from Statistics.PopulationMean import mean

def sampst_dev(lst):
    sum,new_sum = 0,0
    new_list = []

    for x in range(5):
        new_list = lst[0:5]
        new_sum = addition(new_sum, new_list[x])
    j = len(new_list)
    new_mean = division(j, new_sum)

    for row in new_list:
        error = subtraction(row, new_mean)
        error_sq = square(error)
        sum = addition(sum, error_sq)
    i = len(new_list)
    b = division(subtraction(1,i), sum)
    std = math.sqrt(b)  #works
    #std = root(b)      #Doesn't work
    return std


