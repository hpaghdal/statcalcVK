## Z-Score

### What is Z-Score?
A Z-score is a numerical measurement used in statistics of a value's relationship to the mean (*average*) of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean.

The below formula explains each element utilized.

    z = (x – μ) / σ
    where:
    x means each row in the list
    μ = mean.
    σ = the number of items in the group.

### Utilization of Z-Score in our Code

We refereed to the formula listed and created our logic accordingly.

We captured the calculated mean and standard deviation and declared it in variables

    m = mean(lst)
    s = st_dev(lst)
    
After opening a *for loop*, we create our formula according to the one above to get the output
    
    for z in lst:
        return division(subtraction(m, z), s)

### Source
1. [Source #1](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/z-score/)
2. [Source #2](https://www.investopedia.com/terms/z/zscore.asp)
