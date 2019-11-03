import math

n = 100 #sample size
def confidenceinterval(mean, sd, confidence):
    #confidence =[90,95,99] #for sample size 100
    t_value =[1.66,1.984,2.626]
    standard_error =  sd/(math.sqrt(n))
    confidence_lower = []
    confidence_upper = []
    for i in len(t_value):
        conf_low = mean - t_value*standard_error
        confidence_lower.append(conf_low)
        conf_up = mean + t_value*standard_error
        confidence_upper.append(conf_up)
    print(confidence_lower,confidence_upper)