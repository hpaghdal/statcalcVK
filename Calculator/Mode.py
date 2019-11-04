def mode(lst):
    if lst == []:
        return None
    else:
        return max(set(lst), key=lst.count)