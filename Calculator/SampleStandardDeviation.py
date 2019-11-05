import math

from PopulationMean import mean

def sampst_dev(lst):
    sum,new_sum = 0,0
    new_list = []
    i = 0

    for x in range(10):
        new_list = lst[0:10]

    new_mean = mean(new_list)
    for row in new_list:
        i=i+1
        error = row - new_mean
        error_sq = error*error
        sum = sum + error_sq
    b=sum/(i-1)
    std = math.sqrt(b)
    return std
