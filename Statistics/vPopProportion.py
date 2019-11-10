from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division


def v_pop_proportion(lst):
    prob_will = proportion(lst)
    prob_wont = subtraction(prob_will, 1)
    result = multiplication(prob_wont,prob_will)
    vpp = division(result, len(lst))
    return vpp