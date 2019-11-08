import math
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Sqrt import root
from Statistics.PopulationMean import mean

def sampst_dev(lst):
    sum,new_sum = 0,0
    new_list = []
    i,j = 0,0

    for x in range(5):
        new_list = lst[0:5]
        new_sum+= new_list[x]
        j += 1
    new_mean = new_sum/j
    for row in new_list:
        i=i+1
        error = row - new_mean
        error_sq = error*error
        sum = sum + error_sq
    b=sum/(i-1)
    std = math.sqrt(b)
    return std
