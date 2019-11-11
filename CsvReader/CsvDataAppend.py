def data_add(test_data):
    lst = []
    for row in test_data:
        y = int(row['Value 1'])
        lst.append(y)
    return lst
