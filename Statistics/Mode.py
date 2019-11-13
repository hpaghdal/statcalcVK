def mode(lst):
    lst.sort()
    if lst == []:
        return None
    else:
        return max(set(lst), key=lst.count)
