##def mean(lst):
##    sum = 0
##   i = 0
##   for row in lst:
##       i = i + 1
## sum = sum + row
##   return sum / i

def mean(lst):
    if len(lst) < 1:
        raise ValueError('List not long enough')
    return sum(lst) / len(lst)
