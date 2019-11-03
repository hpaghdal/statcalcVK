import math

from Mean import mean

def st_dev(lst):
    sum = 0
    i = 0
    #x = Calculator.popmean(lst)
    x = mean(lst)
    for row in lst:
        i=i+1
        error = row - x
        error_sq = error*error
        sum+= error_sq
    b=sum/(i-1)
    std = math.sqrt(b)
    #std = float(std)

    return std