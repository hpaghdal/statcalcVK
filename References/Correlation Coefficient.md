## Population Correlation Coefficient

### What is Population Correlation Coefficient?
Population Correlation coefficients measure the strength of association between two variables or a set of variables.There are different methods for calcualting the correlation coefficient. The most common method of finding the correlation coefficient is called the Pearson product-moment correlation coefficient. It measures the strength of the linear association between variables measured on an interval or ratio scale.


### Calculating the Correlation Coefficient

The formula to calulate the Correlation Coefficient is given by: 
```
r = ∑ (Zx)i(Zy)i

(Zx)i =  (xi – x̄) / Sx 

(Zy)i =  (zy)i = (yi – ȳ) / Sy
 ```
 Here, xi , yi are the elements in 2 lists
 
        x̄ is the mean of all the values in the x list
        
        ȳ is the mean of all the values in the y list
        
        (Zx)i is the  standardized value for each xi
        
        (Zy)i is the  standardized value for each yi
        
        r = correlation coffecient is the sum of the products of (Zx)i and (Zy)i
    
### Utilization of Correlation Coefficient in our Code
In order to calculate the correlation coefficient, we make use of 2 list from the SampleData.csv file. We referred to the formula listed above and calculated the standardised score for each of the list. 

Then we calculated the sum of the product of the corresponding elements in the standardized value list to obatain the correlation coefficient. 

### Source
1. [Source #1](https://www.thoughtco.com/how-to-calculate-the-correlation-coefficient-3126228)