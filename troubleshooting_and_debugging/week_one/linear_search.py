def linear_search(key, list):
    """If key is in the list, returns it's position in the list,
    otherwise returns -1"""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1
