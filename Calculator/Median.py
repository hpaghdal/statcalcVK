def median(lst):
    lst.sort()
    half = len(lst)//2  # integer division
    b = lst[half]
    c = lst[-half-1]  # for odd lengths, b == c
    return (b + c) / 2