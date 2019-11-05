import math

from PopulationMean import mean
import statistics


def sampst_dev(lst):
    sum = 0
    dimsum = 0
    i=0
    sum,new_sum = 0,0
    new_list = []
    i,j = 0,0

    for x in range(20):
        dimsum = sum + lst[i]
    new_mean = dimsum/20

    for row in lst:
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
    #std = float(std)

    return std