def pvalue(z_data,p_data):
    score = -1.73
    i = 0
    for var in z_data:
        i += 1
        if var == score:
            b = i
    return p_data[b]
