## Mode

### What is Mode?
A Mode is the most recurring number in a given list. 

### Utilization of Mode in our Code
The below logic would take the maximum count of a number in the list we used to capture the mode. 
    
    return max(set(lst), key=lst.count)