import math

from PopulationMean import mean

def sampst_dev(lst):
    sum,new_sum = 0,0
    new_list = []
    i,j = 0,0

    for x in range(20):
        new_list.append(lst)
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
