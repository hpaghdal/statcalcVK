from Calculator.Addition import addition
from Calculator.Division import division
def median(lst):
    lst.sort()
    half = len(lst) // 2  # integer division
    b = lst[half]
    c = lst[-half - 1]  # for odd lengths, b == c
    return division(2, addition(b , c))
