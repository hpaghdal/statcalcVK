## P value

### What is P value?
P value is a number that lies between 0 and 1. The P value is a statistical measure that helps researchers to determine whether their hypothesis is correct. It is the level of marginal significance within a statistical hypothesis test representing the probability of the occurrence of a given event. The p-value is used as an alternative to rejection points to provide the smallest level of significance at which the null hypothesis would be rejected. A smaller p-value means that there is stronger evidence in favor of the alternative hypothesis.

### Calculating the P value

In order to calculate the P value, we need to find the zscore of the population. Using the z score calculated in the z_score function, we find the corresponding P value for that z score from the Z table. The corresponding P value donotes the P value of the population. 

Here is an example of the Z score vs P value table. 

| Z score | P value |
| ------------------- | - |
| -1.98 |	0.023851764 |
| -1.97 |	0.024419185 |
| -1.96 | 0.024997895 |
| -1.95 |	0.02558806 |
| -1.94 |	0.026189845 |
| -1.93 | 0.026803419 |
| -1.73 | 0.042716221 |

For our population, we obtained a zcore of -1.73. The corresponding P value is 0.042716221

```
P value  ∝ Zscore
```


### Source
1. [Source #1](https://www.investopedia.com/terms/p/p-value.asp)