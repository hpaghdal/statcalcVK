def mean(lst):
    total = 0.0
    for t in lst:
        total += t
    m = float(sum(lst)) / len(lst)
    return m