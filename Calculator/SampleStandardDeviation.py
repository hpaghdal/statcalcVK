import math

from PopulationMean import mean
import statistics


def sampst_dev(lst):
    sum = 0
    dimsum = 0
    i=0

    for x in range(20):
        dimsum = sum + lst[i]
    new_mean = dimsum/20

    for row in lst:
        i=i+1
        error = row - new_mean
        error_sq = error*error
        sum = sum + error_sq
    b=sum/(i-1)
    std = math.sqrt(b)
    #std = float(std)

    return std


    return std