from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Sqrt import root


def v_pop_proportion(lst):
    p = proportion(lst)
    c = multiplication(p, subtraction(p, 1))
    #l = len(lst)
    x = division(c, len(lst))
    vp_prop = root(x)
    return vp_prop