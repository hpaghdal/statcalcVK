from Statistics.PopulationMean import mean
from Statistics.SampleGenerator import getSample
from Calculator.Addition import addition
from Calculator.Division import division


def samp_mean(lst):
    new_list = []
    for x in range(5):
        new_list = lst[0:5]
    new_mean = mean(new_list)
    return new_mean


#def sammean(data, sample_size):
 #   total = 0
  #  sample = getSample(data, sample_size)
   ##for num in sample:
     #   total = addition(total, num)
    #return division(total, num_values)