## Population Standard Deviation

### What is Population Standard Deviation?

Standard deviation is a calculation of the dispersion or variation in a set of numbers. If the standard deviation is a small number, it means the data points are close to their mean value. If the deviation is large, it means the numbers are spread out, further from the mean.

The standard deviation formula is denoted by the following:

    σ = ([Σ(x - u)2]/N)1/2

Where:

    σ is the population standard deviation
    Σ represents the sum or total from 1 to N
    x is an individual value
    u is the average of the population
    N is the total number of the population

### Utilization of Population Standard Deviation in our Code

We already had functions created for the mean, division, addition, square, square root and subtraction.

It was a matter of plugging in the calculations into the formula.

After capturing the mean of the list
    
      m = mean(lst)

We would open a *for loop* to calculate the SD, but broke into two parts for easier calculation.

    for l in lst:
        diffs = addition(diffs,square(subtraction(l, m)))
        sd = division(diffs, subtraction(1, len(lst)))
        x = root(sd)
    return x

### Source
1. [Source #1](https://www.thoughtco.com/population-standard-deviation-calculation-609522)