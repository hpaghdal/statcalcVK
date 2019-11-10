from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Sqrt import root
from Statistics.SampleGenerator import getSample
import random


def v_samp_proportion(lst):
    ss = random.randint(1,len(lst))
    new_values = getSample(lst, ss)
    p = proportion(new_values)
    c = multiplication(p, subtraction(p, 1))
    y = subtraction(len(new_values), 1)
    x = division(c, y)
    return x
