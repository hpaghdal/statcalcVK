from Calculator.Addition import addition
from Calculator.Division import division


def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        first_median = lst[len(lst) // 2]
        second_median = lst[len(lst) // 2 - 1]
        median = division(addition(first_median, second_median), 2)
    else:
        median = lst[len(lst) // 2]
    return median
