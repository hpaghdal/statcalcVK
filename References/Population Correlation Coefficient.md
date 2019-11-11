## Correlation Coefficient

### What is Correlation Coefficient?

The correlation coefficient is a statistical measure that calculates the strength of the relationship between the relative movements of two variables. The values range between -1.0 and 1.0. A calculated number greater than 1.0 or less than -1.0 means that there was an error in the correlation measurement. A correlation of -1.0 shows a perfect negative correlation, while a correlation of 1.0 shows a perfect positive correlation. A correlation of 0.0 shows no relationship between the movement of the two variables.

1. 1 indicates a strong positive relationship.
2. -1 indicates a strong negative relationship.
3. A result of zero indicates no relationship at all.

### Utilization of Correlation Coefficient in our Code

We created a data set with two columns and named them *x* and *y*.

After calculating the mean and standard deviation of the above input parameters, we opened *for loops* to do each particular calculation.

    for i in x_data:
        new1 = subtraction(x_mean, i)
        zx = division(new1, x)
        a.append(zx)

    for i in y_data:
        new2 = subtraction(y_mean, i)
        zy = division(new2, y)
        b.append(zy)
        
    for i in range(len(x_data)):
       ab = a[i] * b[i]
       tot_sum = tot_sum + ab

    cal_result = tot_sum / 4
    
 There are several approaches that other links handle. This approach was manageable and worked for us. 

### Source
1. [Source #1](https://www.investopedia.com/terms/c/correlationcoefficient.asp)
2. [Source #2](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/)