from PopulationMean import mean

def samp_mean(lst):
    new_list = []
    for x in range(10):
        new_list = lst[0:10]
    new_mean = mean(new_list)

    return new_mean