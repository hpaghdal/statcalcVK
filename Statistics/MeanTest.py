def newmean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = total + num
    return total/num_values