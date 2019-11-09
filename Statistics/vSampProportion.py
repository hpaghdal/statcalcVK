from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Sqrt import root
from Calculator.Square import square

def v_samp_proportion(lst):
    p = proportion(lst)
    c =  multiplication(p, subtraction(p, 1))
    x = division((c, len(p))
    vp_prop = root(x)
    return vp_prop
