## Median

### What is Median?
A Median is a middle number in a data set. It is a sorted list in ascending order. 

For an odd list of numbers, there will always be a singular middle number. 
For an even list of numbers, there will be two values which can be further calculated by adding the two numbers and dividing by two to extract the median.

The below formula explains each element utilized.

### Utilization of Median in our Code

We initially sorted out list of data

    lst.sort()

Then, if the length of the list when divided by 2 had a remainder of '0', we would add the two values and divide by 2.

    if len(lst) % 2 == 0:
       first_median = lst[len(lst) // 2]
        second_median = lst[len(lst) // 2 - 1]
        median = division(addition(first_median, second_median), 2)

If the list does not have a remainder of 0, it is a odd number and we would take the singular median.
   
   
    else:
        median = lst[len(lst) // 2]
