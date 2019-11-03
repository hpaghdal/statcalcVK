def mean(lst):
    sum = 0
    i = 0
    for row in lst:
        i = i + 1
        sum = sum + row
    return sum / i

