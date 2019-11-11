## Variance of Population Proportion

### What is Variance of Population Proportion?

The Variance of Population proportion means the parts of a variance as a whole. It is the probability of a chance of a success or a failure within a whole data set. 

### Utilization of Variance of Population Proportion in our Code

We started off with delcaring a success and a failure variable. 

    prob_will = proportion(lst)
    prob_wont = subtraction(prob_will, 1)
    
 We then multiplied both variables to get the whole variance. 
 
    result = multiplication(prob_wont,prob_will)
 
 And then dividing by the complete count in the data set.
 
    vpp = division(result, len(lst))