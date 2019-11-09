from Statistics.PopulationMean import mean
from Statistics.SampleGenerator import getSample

import random
import statistics


def samp_mean(lst):
    ss = random.randint(1, len(lst))
    new_values = getSample(lst, ss)
    new_mean = mean(new_values)
    actual_mean = statistics.mean(new_values)  # to compare calculated result
    return new_mean, actual_mean
